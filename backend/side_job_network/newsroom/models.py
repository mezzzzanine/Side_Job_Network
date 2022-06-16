from django.utils import timezone
from tabnanny import verbose
from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField('Title', max_length=40)
    image = models.ImageField('Image', upload_to='photos/%Y/%m/%d/')
    publication_time = models.DateTimeField('Publication time', default=timezone.now)
    text = models.TextField('Text', max_length=250)
    annons = models.TextField('Annons', max_length=150)
    type = models.CharField('Type', max_length=15)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
