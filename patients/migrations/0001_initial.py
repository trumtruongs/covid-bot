# Generated by Django 3.0.4 on 2020-04-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='Patient Code')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), (None, 'Not defined')], max_length=20, verbose_name='Gender')),
                ('year_of_birth', models.PositiveIntegerField(default=1970, max_length=4, verbose_name='Year of birth')),
                ('address', models.CharField(blank=True, db_index=True, max_length=255, verbose_name='Address')),
                ('detail', models.CharField(blank=True, max_length=512, verbose_name='Detail')),
            ],
        ),
    ]
