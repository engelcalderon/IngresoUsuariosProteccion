# Generated by Django 2.1.7 on 2019-02-26 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='contrasena',
            field=models.TextField(),
        ),
    ]
