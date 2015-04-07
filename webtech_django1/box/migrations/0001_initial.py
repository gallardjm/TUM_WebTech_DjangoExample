# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=100)),
                ('storage', models.ForeignKey(to='storage.Storage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
