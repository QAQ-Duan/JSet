# Generated by Django 3.1.7 on 2021-05-16 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_remove_topic_t_introduce'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='contact_kind',
            field=models.CharField(default='邮箱', max_length=64, verbose_name='联系方式类型'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='t_contact',
            field=models.CharField(default='QQ:666666', max_length=64, verbose_name='联系方式内容'),
        ),
    ]
