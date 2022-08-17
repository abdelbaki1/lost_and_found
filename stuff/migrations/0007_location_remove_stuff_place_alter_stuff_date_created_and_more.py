# Generated by Django 4.0.5 on 2022-08-04 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0006_remove_stuff_image_one'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='stuff',
            name='place',
        ),
        migrations.AlterField(
            model_name='stuff',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='stuff',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stuff.location'),
        ),
    ]
