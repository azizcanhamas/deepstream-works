from django.db import models

# Create your models here.
class ChannelModel(models.Model):
    channels=[
        ('0','Atatürk Cad.'),
        ('1','Cumhuriyet Cadç'),
        ('2','Fatih Cad.'),
        ('3','Gül Cad.'),
    ]
    channel=models.CharField(max_length=2,choices=channels,default=channels[0][0])
