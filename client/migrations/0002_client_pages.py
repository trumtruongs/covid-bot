# Generated by Django 3.0.4 on 2020-04-04 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanpage', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='pages',
            field=models.ManyToManyField(to='fanpage.Fanpage'),
        ),
    ]
