# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbasket', '0023_auto_20180606_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='imagen',
            field=models.ImageField(upload_to=b'uploads/slider'),
        ),
    ]
