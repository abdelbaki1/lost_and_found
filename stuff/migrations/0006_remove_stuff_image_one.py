# Generated by Django 4.0.5 on 2022-07-06 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0005_remove_stuff_image_four_remove_stuff_image_three_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stuff',
            name='image_one',
        ),
    ]
