# Generated by Django 4.2.7 on 2023-11-20 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_email_alter_user_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likerecipe',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='likerecipe',
            name='user',
        ),
        migrations.DeleteModel(
            name='Bookmark',
        ),
        migrations.DeleteModel(
            name='LikeRecipe',
        ),
    ]