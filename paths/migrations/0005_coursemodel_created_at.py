# Generated by Django 4.2.7 on 2023-12-05 13:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0004_coursemodel_link_delete_lessonmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
