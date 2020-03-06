# Generated by Django 2.2.10 on 2020-03-03 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('services', models.CharField(max_length=100)),
                ('subject', models.TextField()),
            ],
        ),
    ]