# Generated by Django 5.0.1 on 2024-02-12 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_tinetuser_calc_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tinetuser',
            name='calc_key',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
