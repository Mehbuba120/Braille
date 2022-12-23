from django.conf import settings

from django.db import models


class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to='img/%y')
    def __str__(self):
     return self.image