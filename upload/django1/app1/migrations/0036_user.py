# Generated by Django 2.2.7 on 2021-06-01 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0035_auto_20210417_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
