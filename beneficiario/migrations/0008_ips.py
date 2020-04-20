# Generated by Django 3.0.5 on 2020-04-19 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiario', '0007_auto_20200418_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=255, unique=True)),
                ('nombreApellido', models.CharField(max_length=512)),
            ],
            options={
                'verbose_name_plural': 'ipss',
            },
        ),
    ]