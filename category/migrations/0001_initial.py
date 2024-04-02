# Generated by Django 5.0.3 on 2024-04-02 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='category title')),
                ('description', models.CharField(max_length=500, verbose_name='category description')),
            ],
        ),
    ]