# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-09-23 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolOverview',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('url', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('summary', models.TextField()),
                ('level', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=128)),
                ('rank', models.CharField(max_length=128)),
                ('image', models.CharField(max_length=128)),
                ('class_field', models.CharField(db_column='class', max_length=128)),
                ('fenshuxian1', models.CharField(max_length=128)),
                ('fenshuxian2', models.CharField(max_length=128)),
                ('website', models.CharField(max_length=128)),
                ('student', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('xiaoxun', models.CharField(max_length=128)),
                ('province', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('morelink', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': '学校',
                'verbose_name_plural': '学校',
                'db_table': 'school_overview',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Idiom',
            fields=[
                ('idiom_id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('idiom_name', models.CharField(max_length=128, unique=True, verbose_name='成语')),
                ('pinyin', models.CharField(blank=True, max_length=128, null=True, verbose_name='拼音')),
                ('duyin', models.CharField(blank=True, max_length=1024, null=True, verbose_name='读音')),
                ('jyc', models.CharField(blank=True, max_length=1024, null=True)),
                ('fyc', models.CharField(blank=True, max_length=1024, null=True)),
                ('detail_shiyi', models.TextField(blank=True, null=True)),
                ('shiyi', models.TextField(blank=True, null=True)),
                ('chuchu', models.TextField(blank=True, null=True)),
                ('liju', models.TextField(blank=True, null=True)),
                ('tag', models.TextField(blank=True, null=True, verbose_name='标签')),
                ('protagonist', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '成语',
                'verbose_name_plural': '成语',
                'db_table': 'detailed_idiom',
                'managed': 'False',
            },
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('phrase_id', models.CharField(max_length=128, verbose_name='md5')),
                ('phrase_name', models.CharField(max_length=128, verbose_name='词语')),
                ('pinyin', models.CharField(max_length=128, verbose_name='拼音')),
                ('duyin', models.TextField(max_length=128, verbose_name='读音')),
                ('detail_shiyi', models.TextField(blank=True, null=True)),
                ('shiyi', models.TextField(blank=True, null=True)),
                ('chuchu', models.TextField(blank=True, null=True)),
                ('jyc', models.CharField(blank=True, max_length=1024, null=True)),
                ('fyc', models.CharField(blank=True, max_length=1024, null=True)),
                ('liju', models.TextField(blank=True, null=True)),
                ('tag', models.TextField(blank=True, null=True, verbose_name='标签')),
                ('flag', models.CharField(blank=True, max_length=10, null=True)),
                ('xuqiu', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '词语',
                'verbose_name_plural': '词语',
                'db_table': 'detailed_phrase',
                'managed': 'False',
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('word_id', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='md5')),
                ('word_name', models.CharField(max_length=128, verbose_name='字')),
                ('jiaoyan', models.IntegerField(blank=True, null=True, verbose_name='与新华字典对标过为1')),
                ('pinyin', models.CharField(max_length=128, verbose_name='拼音')),
                ('pinyin_source', models.IntegerField(blank=True, null=True, verbose_name='拼音来源 0：阿凡题 1：新华字典 2：阿凡题人工 3：搜狗人工 4：百度汉语 5：百度百科')),
                ('duyin', models.CharField(max_length=1024, verbose_name='读音')),
                ('duyin_source', models.IntegerField(blank=True, null=True, verbose_name='读音来源')),
                ('bushou', models.CharField(max_length=128, verbose_name='部首')),
                ('bushou_source', models.IntegerField(blank=True, null=True, verbose_name='部首来源')),
                ('bihua', models.IntegerField()),
                ('bihua_source', models.IntegerField(blank=True, null=True)),
                ('bishun', models.CharField(max_length=128)),
                ('bishun_source', models.IntegerField(blank=True, null=True)),
                ('wubi', models.CharField(blank=True, max_length=128, null=True)),
                ('wubi_source', models.IntegerField(blank=True, null=True)),
                ('shiyi', models.TextField(verbose_name='释义')),
                ('shiyi_source', models.IntegerField(blank=True, null=True)),
                ('detail_shiyi', models.TextField(verbose_name='详细释义')),
                ('detail_shiyi_source', models.IntegerField(blank=True, null=True)),
                ('relate_ciyu', models.TextField(verbose_name='涉及的词语')),
                ('relate_ciyu_source', models.IntegerField(blank=True, null=True)),
                ('jyc', models.CharField(blank=True, max_length=128, null=True, verbose_name='近义词')),
                ('jyc_source', models.IntegerField(blank=True, null=True)),
                ('fyc', models.CharField(blank=True, max_length=128, null=True, verbose_name='反义词')),
                ('fyc_source', models.IntegerField(blank=True, null=True)),
                ('jiegou', models.CharField(max_length=128)),
                ('jiegou_source', models.IntegerField(blank=True, null=True)),
                ('wuxing', models.CharField(blank=True, max_length=128, null=True)),
                ('wuxing_source', models.IntegerField(blank=True, null=True)),
                ('fanti', models.CharField(blank=True, max_length=128, null=True)),
                ('fanti_source', models.IntegerField(blank=True, null=True)),
                ('tupian', models.CharField(blank=True, max_length=1024, null=True)),
                ('tupian_source', models.IntegerField(blank=True, null=True)),
                ('gif', models.CharField(blank=True, max_length=1024, null=True, verbose_name='动图')),
                ('num', models.CharField(blank=True, max_length=100, null=True)),
                ('xjz', models.TextField(blank=True, null=True)),
                ('xjz_source', models.IntegerField(blank=True, null=True)),
                ('zitou', models.CharField(blank=True, max_length=255, null=True)),
                ('jiayibi', models.TextField(blank=True, null=True)),
                ('jianyibi', models.TextField(blank=True, null=True)),
                ('duoyinzizuci', models.TextField(blank=True, null=True)),
                ('chaifen', models.CharField(blank=True, max_length=255, null=True)),
                ('pinyinjx', models.CharField(blank=True, max_length=255, null=True)),
                ('jppdanzi', models.TextField(blank=True, null=True)),
                ('jppzuci', models.TextField(blank=True, null=True)),
                ('tydanzi', models.TextField(blank=True, null=True)),
                ('duoyinshiyi', models.TextField(blank=True, null=True)),
                ('duoyinshiyi_source', models.IntegerField(blank=True, null=True)),
                ('flag', models.IntegerField(blank=True, null=True)),
                ('rank', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': '汉字',
                'verbose_name_plural': '汉字',
                'db_table': 'detailed_word',
                'managed': 'False',
            },
        ),
    ]
