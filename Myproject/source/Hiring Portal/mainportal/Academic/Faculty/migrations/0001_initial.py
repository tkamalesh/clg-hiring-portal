# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('faculty_portal', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filled_status', models.BooleanField(default=False)),
                ('application', models.ForeignKey(to='faculty_portal.Application')),
                ('faculty', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('strength', models.IntegerField(choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (5, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')])),
                ('area_of_expertize', models.IntegerField(choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (5, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')])),
                ('appropriateness', models.IntegerField(blank=True, choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (5, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')])),
                ('recommendation', models.IntegerField(choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (5, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')])),
                ('specific_recommendation', models.CharField(max_length=200, blank=True)),
                ('comments', models.CharField(max_length=100)),
                ('applications', models.ForeignKey(to='faculty_portal.Application')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='facultyreview',
            unique_together=set([('faculty', 'application')]),
        ),
    ]
