# Generated by Django 4.2.7 on 2023-11-19 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Instruction',
            new_name='Step',
        ),
        migrations.AddField(
            model_name='recipe',
            name='bookmarks',
            field=models.IntegerField(default=0),
        ),
    ]
