from tabnanny import verbose
from django.db import models

# Create your models here.
class Vacancy(models.Model):
    title = models.CharField('Title', max_length=40)
    country = models.CharField('Country', max_length=40)
    city = models.CharField('City', max_length=40)
    minimum_salary = models.IntegerField('Minimum salary')
    maximum_salary = models.IntegerField('Maximum salary')
    publication_time = models.DateTimeField('Publication time')
    description = models.TextField('Description', max_length=250)
    owner = models.CharField('Owner', max_length=70)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'
