# Generated by Django 3.0.4 on 2020-04-04 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='is_admin',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Is Admin'),
        ),
    ]
