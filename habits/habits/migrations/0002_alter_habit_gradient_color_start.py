# Generated by Django 5.0.9 on 2024-10-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='gradient_color_start',
            field=models.CharField(default='#FFFFFF', help_text='Hex code for the gradient start color (default: black)', max_length=7),
        ),
    ]
