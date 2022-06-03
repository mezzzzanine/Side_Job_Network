from django.utils import timezone
from tabnanny import verbose
from django.db import models

# Create your models here.
class Vacancy(models.Model):
    title = models.CharField('Title', max_length=40)
    image = models.ImageField('Image', upload_to='photos/%Y/%m/%d/')
    country = models.CharField('Country', max_length=40)
    city = models.CharField('City', max_length=40)
    minimum_salary = models.IntegerField('Minimum salary', blank=True)
    maximum_salary = models.IntegerField('Maximum salary', blank=True)
    currency = models.CharField('Currency', max_length=3)
    publication_time = models.DateTimeField('Publication time', default=timezone.now)
    description = models.TextField('Description', max_length=250)
    requirements = models.TextField('Requirements', max_length=150)
    owner = models.CharField('Owner', max_length=70)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'
