# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import faculty_portal.models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=0)),
                ('applied_researchLab', models.CharField(max_length=100, choices=[(b'SPCRC', b'Signal Processing and Communications Research Center'), (b'CDE', b'Center for Data Engineering'), (b'LTRC', b'Language Technologies Research Center'), (b'RRC', b'Robotics Research Center'), (b'CSTAR', b'Center for Security, Theory and Algorithms'), (b'SERC', b'Software Engineering Research Center')])),
                ('summarysheet', models.CharField(max_length=100, blank=True)),
                ('allowed_level', models.IntegerField(default=0)),
                ('applied_creation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('stage_waiting_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('givenname', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('age', models.SmallIntegerField()),
                ('current_affliation', models.CharField(max_length=100)),
                ('status_of_phd', models.CharField(default=b'complete', max_length=21, choices=[(b'complete', b'Completed'), (b'ongoing', b'Ongoing'), (b'abd', b'All but dissertation'), (b'none', b'None')])),
                ('institue_of_phd', models.CharField(max_length=100, blank=True)),
                ('date_of_completion', models.DateField(default=datetime.date.today, blank=True)),
                ('expected_date_of_completion', models.DateField(default=datetime.date.today, blank=True)),
                ('experience_place', models.CharField(max_length=100, blank=True)),
                ('experience_position', models.CharField(max_length=100, blank=True)),
                ('experience_duration', models.CharField(max_length=20, blank=True)),
                ('resume', models.FileField(upload_to=faculty_portal.models.get_upload_filename_resume, blank=True)),
                ('cover_letter', models.FileField(upload_to=faculty_portal.models.get_upload_filename_cover, blank=True)),
                ('publication1', models.FileField(upload_to=faculty_portal.models.get_upload_filename_pub, blank=True)),
                ('publication2', models.FileField(upload_to=faculty_portal.models.get_upload_filename_pub, blank=True)),
                ('publication3', models.FileField(upload_to=faculty_portal.models.get_upload_filename_pub, blank=True)),
                ('publication4', models.FileField(upload_to=faculty_portal.models.get_upload_filename_pub, blank=True)),
                ('publication5', models.FileField(upload_to=faculty_portal.models.get_upload_filename_pub, blank=True)),
                ('pub_title1', models.CharField(max_length=100, blank=True)),
                ('pub_title2', models.CharField(max_length=100, blank=True)),
                ('pub_title3', models.CharField(max_length=100, blank=True)),
                ('pub_title4', models.CharField(max_length=100, blank=True)),
                ('pub_title5', models.CharField(max_length=100, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='candidate',
            field=models.OneToOneField(blank=True, to='faculty_portal.Candidate'),
        ),
    ]
