# Generated by Django 2.1.1 on 2018-10-05 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_postear'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=100)),
                ('nuevo', models.CharField(max_length=100)),
            ],
        ),
    ]
