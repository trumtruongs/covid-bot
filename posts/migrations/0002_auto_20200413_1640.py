# Generated by Django 3.0.5 on 2020-04-13 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(blank=True, verbose_name='Message'),
        ),
    ]
