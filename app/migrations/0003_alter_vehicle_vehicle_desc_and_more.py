# Generated by Django 5.0 on 2023-12-30 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_vehicle_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_desc',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_model',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_no',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(choices=[('--select type--', '--select type--'), ('two', 'Two wheelers'), ('three', 'three wheelers'), ('four', 'four wheelers')], default='--select type--', max_length=250),
        ),
    ]
