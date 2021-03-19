# Generated by Django 3.1.7 on 2021-03-19 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restourant', '0004_category_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.TextField(blank=True)),
                ('message', models.TextField(blank=True)),
                ('created_at', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=150)),
                ('created_at', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
