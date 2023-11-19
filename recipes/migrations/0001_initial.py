# Generated by Django 4.2.7 on 2023-11-19 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('quantity', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('step', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.URLField(blank=True, null=True)),
                ('visibility', models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('PRIVATE', 'PRIVATE'), ('DRAFT', 'DRAFT')], default=('PUBLIC', 'PUBLIC'), max_length=7)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('dificulty', models.CharField(choices=[('EASY', 'EASY'), ('MEDIUM', 'MEDIUM'), ('HARD', 'HARD')], default=('EASY', 'EASY'), max_length=6)),
                ('prep_time', models.CharField(max_length=50)),
                ('cook_time', models.CharField(max_length=50)),
                ('bill_spent', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('likes', models.IntegerField(default=0)),
                ('tags', models.ManyToManyField(to='recipes.tag')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
