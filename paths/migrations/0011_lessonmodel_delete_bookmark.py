# Generated by Django 4.2.7 on 2023-12-06 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0010_rename_bookmarks_bookmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paths.coursemodel')),
            ],
        ),
        migrations.DeleteModel(
            name='Bookmark',
        ),
    ]
