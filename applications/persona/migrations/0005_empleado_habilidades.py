# Generated by Django 3.0 on 2022-04-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_auto_20220402_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='persona.habilidades'),
        ),
    ]
