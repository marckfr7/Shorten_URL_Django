from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cortar_url(models.Model):
    long_url = models.URLField(null=False)
    description = models.CharField(max_length=100, null=False)
    short_url = models.TextField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description