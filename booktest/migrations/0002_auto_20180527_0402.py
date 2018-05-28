# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='heroinfo',
            old_name='hBook',
            new_name='hbook',
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='bcommet',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='bread',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='heroinfo',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hgender',
            field=models.BooleanField(default=True),
        ),
    ]
