# Generated by Django 3.1.7 on 2021-05-05 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20210505_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='t_introduce',
        ),
    ]