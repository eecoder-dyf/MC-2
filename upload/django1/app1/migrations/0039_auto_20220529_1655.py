# Generated by Django 2.2 on 2022-05-29 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0038_auto_20220529_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='enable_sign_up',
            field=models.BooleanField(default=False),
        ),
    ]