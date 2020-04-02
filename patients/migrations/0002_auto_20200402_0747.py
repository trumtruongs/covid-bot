# Generated by Django 3.0.4 on 2020-04-02 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='is_healthy',
            field=models.BooleanField(default=False, verbose_name='Patient is healthy?'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('', 'Not defined')], default='', max_length=20, verbose_name='Gender'),
        ),
    ]