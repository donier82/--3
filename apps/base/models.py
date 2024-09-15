from django.db import models

# Create your models here.

class About(models.Model):

    logo=models.ImageField(
        upload_to='logo/',
        verbose_name='фото1',
        null=True, blank=True
        )

    banner=models.ImageField(
        upload_to='banner/',
        verbose_name='фото2',
        null=True, blank=True
        )
    text=models.CharField(max_length=100)

    def __str__(self):
        return self.text