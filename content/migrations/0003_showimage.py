# Generated by Django 3.1 on 2020-09-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20200907_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
