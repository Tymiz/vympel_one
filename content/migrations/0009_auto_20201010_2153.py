# Generated by Django 3.1 on 2020-10-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_auto_20201010_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.FileField(null=True, upload_to='Vympel/media/'),
        ),
    ]