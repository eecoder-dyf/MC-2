# Generated by Django 2.2 on 2022-05-29 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0037_auto_20220529_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='options',
            old_name='user',
            new_name='username',
        ),
    ]