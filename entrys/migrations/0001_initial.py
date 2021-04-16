# Generated by Django 4.0.dev20210410182312 on 2021-04-13 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.CharField(max_length=5000)),
                ('publishedDate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]