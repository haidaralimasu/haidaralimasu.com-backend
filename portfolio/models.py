from statistics import mode
from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    demo = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    content = models.TextField()

    def __str__(self):
        return self.title
