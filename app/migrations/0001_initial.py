# Generated by Django 4.1.1 on 2022-09-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=26)),
                ('Lastname', models.CharField(max_length=26)),
                ('Emails', models.EmailField(max_length=30)),
                ('Gender', models.CharField(max_length=10)),
                ('Contacts', models.BigIntegerField()),
            ],
        ),
    ]
