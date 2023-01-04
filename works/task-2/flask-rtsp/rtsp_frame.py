# import the necessary packages
import cv2
import os

#parametros de acesso da camera
USERNAME = ''
PASSWORD = ''
IP = 'localhost'
PORT = '8554'

#so roda se for ffmpeg
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

#url da camera stream varia conforme o modelo da camera

URL='rtsp://{}:{}@{}:{}/ds-test'.format(USERNAME, PASSWORD, IP, PORT)

path_cascade = "haarcascade_frontalface_alt2.xml"
# defining face detector
face_cascade=cv2.CascadeClassifier(path_cascade)
ds_factor=0.6
class VideoCamera(object):
    def __init__(self):
       #capturing video
       #self.video = cv2.VideoCapture(0)
       self.video = cv2.VideoCapture(URL, cv2.CAP_FFMPEG)
       #self.fgbg = cv2.createBackgroundSubtractorKNN()
    
    def __del__(self):
        #releasing camera
        self.video.release()
    
    def get_frame(self):
       #extracting frames
        ret, frame = self.video.read()

        #encode OpenCV raw frame to jpg and displaying it
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
