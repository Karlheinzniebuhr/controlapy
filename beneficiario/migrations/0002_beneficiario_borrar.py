# Generated by Django 3.0.5 on 2020-04-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiario',
            name='borrar',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
