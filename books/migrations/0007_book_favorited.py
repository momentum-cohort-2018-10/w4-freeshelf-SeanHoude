# Generated by Django 2.1.3 on 2018-11-23 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='favorited',
            field=models.IntegerField(default=0),
        ),
    ]
