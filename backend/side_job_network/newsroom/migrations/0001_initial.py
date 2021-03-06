# Generated by Django 4.0.4 on 2022-06-15 23:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Title')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Image')),
                ('publication_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publication time')),
                ('text', models.TextField(max_length=250, verbose_name='Text')),
                ('annons', models.TextField(max_length=150, verbose_name='Annons')),
                ('type', models.CharField(max_length=70, verbose_name='Type')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
    ]
