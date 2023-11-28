# Generated by Django 4.2.7 on 2023-11-28 04:27

import cloudinary.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(default='jkccejtc06k0elzgia0m', max_length=255, verbose_name='image')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FieldModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FieldTitle', models.CharField(max_length=255)),
                ('FieldDescription', models.TextField()),
                ('Author', models.CharField(max_length=100)),
                ('Duration', models.DurationField(default=datetime.timedelta(0))),
                ('Rating', models.IntegerField(default=0)),
                ('Price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image', cloudinary.models.CloudinaryField(default='jkccejtc06k0elzgia0m', max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='LessonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paths.coursemodel')),
            ],
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paths.fieldmodel'),
        ),
    ]
