from django.urls import path
from . import views

urlpatterns=[
    path("",views.rtspStream,name='rtspStream'),
    path("video_feed",views.video_feed,name='video_feed')
]
