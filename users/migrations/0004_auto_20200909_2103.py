# Generated by Django 3.1 on 2020-09-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_introduction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='introduction',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterField(
            model_name='introduction',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='Email'),
        ),
    ]
