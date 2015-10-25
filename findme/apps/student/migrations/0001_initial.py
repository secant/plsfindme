# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('university', models.TextField()),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('department', models.TextField()),
                ('course_number', models.TextField()),
                ('course_type', models.TextField()),
                ('section', models.IntegerField()),
                ('bio', models.TextField()),
            ],
        ),
    ]
