from django.forms import models


from .models import ChannelModel
class ChannelForm(models.ModelForm):
    class Meta:
        model=ChannelModel
        fields=['channel']