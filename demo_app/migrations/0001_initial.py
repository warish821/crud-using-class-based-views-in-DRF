# Generated by Django 4.0.1 on 2022-01-11 06:11

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
                ('name', models.CharField(max_length=40, null=True)),
                ('address', models.CharField(max_length=80, null=True)),
                ('contact', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]