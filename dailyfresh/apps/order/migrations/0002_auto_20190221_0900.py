# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
        ('order', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='addr',
            field=models.ForeignKey(verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80', to='users.Address'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95', to='order.OrderInfo'),
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='sku',
            field=models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81SKU', to='goods.GoodsSKU'),
        ),
    ]
