# Generated by Django 4.0.5 on 2022-08-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0007_location_remove_stuff_place_alter_stuff_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuff',
            name='preview_image',
            field=models.ImageField(default='stuff\\imgsĺ038.jpg', upload_to='imgs'),
        ),
    ]