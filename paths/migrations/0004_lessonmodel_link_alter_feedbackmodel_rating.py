# Generated by Django 4.2.7 on 2023-12-03 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0003_feedbackmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonmodel',
            name='link',
            field=models.URLField(default='No link available, please report thankn you'),
        ),
        migrations.AlterField(
            model_name='feedbackmodel',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
