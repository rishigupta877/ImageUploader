# Generated by Django 4.0.3 on 2022-03-10 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='pics')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]