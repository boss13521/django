# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20190110_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='bpub_date',
            field=models.DateTimeField(),
        ),
    ]
