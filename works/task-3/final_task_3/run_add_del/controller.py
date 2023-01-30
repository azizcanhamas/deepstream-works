#!/usr/bin/env python3

from deepstream_rt_src_add_del import TrafficCamDeepstream as tcd
import threading
from fastapi import FastAPI
class Control:
    def __init__(self):
        self.uri_list=[
            'file:///home/azu/Desktop/deepstream/works/task-3/add_del_source_django/rtspApp/cams/v1.h264',
            'file:///home/azu/Desktop/deepstream/works/task-3/add_del_source_django/rtspApp/cams/v2.h264',
            'file:///home/azu/Desktop/deepstream/works/task-3/add_del_source_django/rtspApp/cams/v3.h264',
            'file:///home/azu/Desktop/deepstream/works/task-3/add_del_source_django/rtspApp/cams/v4.h264',
        ]

        self.x=0
        self.t=threading.Thread(target=self.start_deepstream)
        #self.t.daemon=True
        self.t.start()

        

    def start_deepstream(self):
        self.tcd=tcd()
        args=['deepstream_rt_src_add_del.py',self.uri_list[0]]
        self.tcd.main(args)

    def add_source(self,id):
        self.tcd.add_sources(data=None,uri=self.uri_list[id])
    
    def delete_source(self,id):
        self.tcd.delete_sources(data=None,uri=self.uri_list[id])

control=Control()
#### API CONTROL
# Terminal : uvicorn controller:app --reload
app = FastAPI()

@app.get("/add/{camera_id}")
async def add_item(camera_id):
    print("!!!!!!!!!!!!!!!!!!! CAMERA_ID : ",camera_id)
    control.add_source(id=int(camera_id))
    # Bir sey return etmesine gerek yok.
    #return {"camera_id": camera_id}

@app.get("/del/{camera_id}")
async def del_item(camera_id):
    control.delete_source()