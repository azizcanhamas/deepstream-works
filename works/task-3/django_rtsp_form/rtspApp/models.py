from django.db import models

# Create your models here.
class ChannelModel(models.Model):
    channels=[
        ('0','sink_0'),
        ('1','sink_1'),
        ('2','sink_2'),
        ('3','sink_3'),
        ('4','sink_4'),
    ]
    channel=models.CharField(max_length=2,choices=channels,default=channels[0][0])
