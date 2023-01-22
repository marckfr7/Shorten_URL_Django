from django.forms import ModelForm
from .models import Cortar_url

class Shorten_URLForm(ModelForm):
    class Meta:
        model = Cortar_url
        fields = ['long_url', 'description']