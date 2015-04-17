# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rentable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'Default Product Name', max_length=100)),
                ('isRented', models.BooleanField(default=False)),
                ('dateRented', models.DateTimeField(null=True)),
                ('dateDue', models.DateTimeField(null=True)),
                ('dateReturned', models.DateTimeField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cusName', models.CharField(default=b'Default Customer Name', max_length=100)),
                ('cusPhoneNum', models.CharField(default=b'Default Customer Phone Number', max_length=100)),
                ('cusEmail', models.CharField(default=b'Default Customer Email', max_length=100)),
                ('price', models.FloatField(default=0.0)),
                ('rentable', models.ForeignKey(to='RentrApp.Rentable', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Default Store Name', max_length=100)),
                ('address', models.CharField(default=b'Default Store Address', max_length=100)),
                ('phoneNum', models.CharField(default=b'Default Store Phone Number', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='rentable',
            name='store',
            field=models.ForeignKey(to='RentrApp.Store', null=True),
        ),
    ]
