# Generated by Django 3.2 on 2021-04-19 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placesapi', '0002_remove_place_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='name',
            field=models.CharField(default='chase', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.DecimalField(decimal_places=20, max_digits=23),
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.DecimalField(decimal_places=20, max_digits=23),
        ),
    ]
