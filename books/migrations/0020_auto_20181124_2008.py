# Generated by Django 2.1.3 on 2018-11-24 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0019_auto_20181124_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_accounts', to='books.Book'),
        ),
    ]