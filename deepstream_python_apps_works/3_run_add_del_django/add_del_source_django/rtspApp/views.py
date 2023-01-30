from django.shortcuts import render

from .forms import ChannelForm

from django.http import StreamingHttpResponse
from django.views.decorators import gzip
import cv2
import threading
import os

import requests

class VideoCamera(object):
    USERNAME = ''
    PASSWORD = ''
    IP = 'localhost'
    PORT = '8554'

    os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
    URL='rtsp://{}:{}@{}:{}/ds-test'.format(USERNAME, PASSWORD, IP, PORT)


    def __init__(self):
        self.video=cv2.VideoCapture(self.URL,cv2.CAP_FFMPEG)
        (self.grabbed,self.frame)=self.video.read()
        threading.Thread(target=self.update,args=()).start()


    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        image=self.frame
        _,jpeg=cv2.imencode('.jpg',image)
        return jpeg.tobytes()

    def update(self):
        while(True):
            (self.grabbed,self.frame)=self.video.read()

def gen(camera):
    while(True):
        frame=camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),content_type="multipart/x-mixed-replace;boundary=frame")

def rtspStream(request):
    if request.method=="GET":
        form=ChannelForm(request.GET)

        #Get user selection from form.
        selected=form['channel'].value()

        if selected is not None:
            #Calling Deepstream API.
            # Working URL in browser: http://127.0.0.1:8002/add/3
            requests.get('http://127.0.0.1:8002/add/'+str(selected), params=request.GET)
    
        form=ChannelForm()
    else:
        form=ChannelForm()
    context={
        'form':form
    }
    return render(request,"index.html",context=context)


