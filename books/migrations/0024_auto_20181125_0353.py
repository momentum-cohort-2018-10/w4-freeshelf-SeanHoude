# Generated by Django 2.1.3 on 2018-11-25 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0023_auto_20181125_0236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='is_fantasy',
            new_name='fantasy',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='is_horror',
            new_name='horror',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='is_scifi',
            new_name='scifi',
        ),
        migrations.AlterField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='books.Book'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploads', to='books.Book'),
        ),
    ]
