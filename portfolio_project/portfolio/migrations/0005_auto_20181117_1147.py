# Generated by Django 2.1.2 on 2018-11-17 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20181117_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorieniv1',
            name='nom',
            field=models.CharField(default='category name', max_length=100),
        ),
        migrations.AlterField(
            model_name='categorieniv2',
            name='nom',
            field=models.CharField(default='category name', max_length=100),
        ),
        migrations.AlterField(
            model_name='categorieniv3',
            name='nom',
            field=models.CharField(default='category name', max_length=100),
        ),
    ]