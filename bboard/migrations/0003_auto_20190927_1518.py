# Generated by Django 2.2.5 on 2019-09-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20190924_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubric',
            name='name',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Название'),
        ),
    ]
