# Generated by Django 2.0.7 on 2018-08-27 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': '用户列表', 'verbose_name_plural': '用户列表'},
        ),
        migrations.AlterModelOptions(
            name='competition',
            options={'verbose_name': '赛事列表', 'verbose_name_plural': '赛事列表'},
        ),
        migrations.AlterModelOptions(
            name='photolist',
            options={'verbose_name': '照片列表', 'verbose_name_plural': '照片列表'},
        ),
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default='image/default.png', max_length=200, null=True, upload_to='avatar/%Y/%m', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='photolist',
            name='big_images',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='competition/images/', verbose_name='原图'),
        ),
        migrations.AlterField(
            model_name='photolist',
            name='desc',
            field=models.TextField(max_length=200, verbose_name='图片介绍'),
        ),
    ]