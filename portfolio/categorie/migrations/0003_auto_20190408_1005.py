# Generated by Django 2.1.7 on 2019-04-08 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorie', '0002_auto_20190328_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategorieNiv4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categorie', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='categorieniv3',
            name='has_sub',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='categorieniv4',
            name='cat_sup',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='categorie.CategorieNiv3'),
        ),
    ]