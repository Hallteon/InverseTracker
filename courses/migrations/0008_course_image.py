# Generated by Django 3.2.18 on 2023-04-15 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses', verbose_name='Картинка'),
        ),
    ]
