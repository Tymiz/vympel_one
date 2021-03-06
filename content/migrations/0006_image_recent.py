# Generated by Django 3.1 on 2020-09-11 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_delete_showimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения к последним событиям',
            },
        ),
        migrations.CreateModel(
            name='Recent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.image')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'Последние события',
            },
        ),
    ]
