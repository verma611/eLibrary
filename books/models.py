from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=500)
    Summary = models.TextField(max_length=700)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=500)
    cover = models.ImageField(upload_to='images/', default=None)
    upload = models.FileField(upload_to ='uploads/', blank=True)