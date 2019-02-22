# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_delete', models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81SPU\xe5\x90\x8d\xe7\xa7\xb0')),
                ('detail', tinymce.models.HTMLField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe8\xaf\xa6\xe6\x83\x85', blank=True)),
            ],
            options={
                'db_table': 'df_goods',
                'verbose_name': '\u5546\u54c1SPU',
                'verbose_name_plural': '\u5546\u54c1SPU',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_delete', models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('image', models.ImageField(upload_to=b'goods', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe8\xb7\xaf\xe5\xbe\x84')),
            ],
            options={
                'db_table': 'df_goods_image',
                'verbose_name': '\u5546\u54c1\u56fe\u7247',
                'verbose_name_plural': '\u5546\u54c1\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='GoodsSKU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_delete', models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0')),
                ('desc', models.CharField(max_length=256, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xae\x80\xe4\xbb\x8b')),
                ('price', models.DecimalField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=10, decimal_places=2)),
                ('unite', models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x8d\x95\xe4\xbd\x8d')),
                ('image', models.ImageField(upload_to=b'goods', verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x9b\xbe\xe7\x89\x87')),
                ('stock', models.IntegerField(default=1, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\xba\x93\xe5\xad\x98')),
                ('sales', models.IntegerField(default=0, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe9\x94\x80\xe9\x87\x8f')),
                ('status', models.SmallIntegerField(default=1, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe4\xb8\x8b\xe7\xba\xbf'), (1, b'\xe4\xb8\x8a\xe7\xba\xbf')])),
                ('goods', models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81SPU', to='goods.Goods')),
            ],
            options={
                'db_table': 'df_goods_sku',
                'verbose_name': '\u5546\u54c1',
                'verbose_name_plural': '\u5546\u54c1',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_delete', models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe7\xa7\x8d\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0')),
                ('logo', models.CharField(max_length=20, verbose_name=b'\xe6\xa0\x87\xe8\xaf\x86')),
                ('image', models.ImageField(upload_to=b'type', verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xb1\xbb\xe5\x9e\x8b\xe5\x9b\xbe\xe7\x89\x87')),
            ],
            options={
                'db_table': 'df_goods_type',
                'verbose_name': '\u5546\u54c1\u79cd\u7c7b',
                'verbose_name_plural': '\u5546\u54c1\u79cd\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='IndexGoodsBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_delete', models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('image', models.ImageField(upload_to=b'banner', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('index', models.SmallIntegerField(default=0, verbose_name=b'\xe5\xb1\x95\xe7\xa4\xba\xe9\xa1\xba\xe5\xba\x8f')),
                ('sku', models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81', to='goods.GoodsSKU')),
            ],
            options={
                'db_table': 'df_index_banner',
                'verbose_name': '\u9996\u9875\u8f6e\u64ad\u5546\u54c1',
                'verbose_name_plural': '\u9996\u9875\u8f6e\u64ad\u5546\u54c1',
            },
        ),
        migrations.CreateModel(
            name='IndexPromotionBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_delete', models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe5\x90\x8d\xe7\xa7\xb0')),
                ('url', models.URLField(verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe9\x93\xbe\xe6\x8e\xa5')),
                ('image', models.ImageField(upload_to=b'banner', verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe5\x9b\xbe\xe7\x89\x87')),
                ('index', models.SmallIntegerField(default=0, verbose_name=b'\xe5\xb1\x95\xe7\xa4\xba\xe9\xa1\xba\xe5\xba\x8f')),
            ],
            options={
                'db_table': 'df_index_promotion',
                'verbose_name': '\u4e3b\u9875\u4fc3\u9500\u6d3b\u52a8',
                'verbose_name_plural': '\u4e3b\u9875\u4fc3\u9500\u6d3b\u52a8',
            },
        ),
        migrations.CreateModel(
            name='IndexTypeGoodsBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_delete', models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('display_type', models.SmallIntegerField(default=1, verbose_name=b'\xe5\xb1\x95\xe7\xa4\xba\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(0, b'\xe6\xa0\x87\xe9\xa2\x98'), (1, b'\xe5\x9b\xbe\xe7\x89\x87')])),
                ('index', models.SmallIntegerField(default=0, verbose_name=b'\xe5\xb1\x95\xe7\xa4\xba\xe9\xa1\xba\xe5\xba\x8f')),
                ('sku', models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81SKU', to='goods.GoodsSKU')),
                ('type', models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xb1\xbb\xe5\x9e\x8b', to='goods.GoodsType')),
            ],
            options={
                'db_table': 'df_index_type_goods',
                'verbose_name': '\u4e3b\u9875\u5206\u7c7b\u5c55\u793a\u5546\u54c1',
                'verbose_name_plural': '\u4e3b\u9875\u5206\u7c7b\u5c55\u793a\u5546\u54c1',
            },
        ),
        migrations.AddField(
            model_name='goodssku',
            name='type',
            field=models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xa7\x8d\xe7\xb1\xbb', to='goods.GoodsType'),
        ),
        migrations.AddField(
            model_name='goodsimage',
            name='sku',
            field=models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81', to='goods.GoodsSKU'),
        ),
    ]
