# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-18 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrdep', '0002_auto_20160518_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_type',
            field=models.IntegerField(choices=[(0, 'Прием на работу'), (1, 'Увольнение')], null=True, verbose_name='Тип документа'),
        ),
    ]