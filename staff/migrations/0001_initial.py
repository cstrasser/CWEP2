# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('company', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=50)),
                ('company_currency', models.CharField(max_length=50)),
                ('bill_addr1', models.CharField(max_length=50, null=True, blank=True)),
                ('bill_addr2', models.CharField(max_length=50, null=True, blank=True)),
                ('bill_city', models.CharField(max_length=50, null=True, blank=True)),
                ('bill_prov_state', models.CharField(max_length=50, null=True, blank=True)),
                ('bill_country', models.CharField(max_length=50, null=True, blank=True)),
                ('bill_pc_zip', models.CharField(max_length=50, null=True, blank=True)),
                ('bill_fax', models.CharField(max_length=50, null=True, blank=True)),
                ('bill_email', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'tblCompany',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Staffdesignation',
            fields=[
                ('sd_designation', models.CharField(max_length=50, null=True, db_column=b'SD_Designation', blank=True)),
                ('sd_id', models.AutoField(serialize=False, primary_key=True, db_column=b'SD_ID')),
            ],
            options={
                'db_table': 'tblS_StaffDesignation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Staffworktype',
            fields=[
                ('swt_type', models.CharField(max_length=50, db_column=b'SWT_Type')),
                ('swt_id', models.AutoField(serialize=False, primary_key=True, db_column=b'SWT_ID')),
            ],
            options={
                'db_table': 'tblS_StaffWorkType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('user', models.OneToOneField(related_name='auth_profile', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('number', models.CharField(max_length=10, db_column=b'Staff_Number')),
                ('staffname', models.CharField(max_length=50, db_column=b'StaffName')),
                ('login_id', models.CharField(max_length=50, null=True, db_column=b'Staff_Login_ID', blank=True)),
                ('phone_ext', models.CharField(max_length=50, null=True, db_column=b'Staff_phone_ext', blank=True)),
                ('cell', models.CharField(max_length=50, null=True, db_column=b'Staff_cell', blank=True)),
                ('home_phone', models.CharField(max_length=50, null=True, db_column=b'Staff_home_phone', blank=True)),
                ('emg_contact_name', models.CharField(max_length=50, null=True, db_column=b'Staff_contact_name', blank=True)),
                ('emg_contact_phone', models.CharField(max_length=50, null=True, db_column=b'Staff_contact_phone', blank=True)),
                ('address', models.CharField(max_length=50, null=True, db_column=b'Staff_Address', blank=True)),
                ('start_date', models.DateTimeField(null=True, db_column=b'Staff_Start_Date', blank=True)),
                ('end_date', models.DateTimeField(null=True, db_column=b'Staff_End_Date', blank=True)),
                ('status', models.CharField(max_length=50, null=True, db_column=b'Staff_Status', blank=True)),
                ('note', models.TextField(null=True, db_column=b'Staff_Note', blank=True)),
                ('default_type', models.CharField(max_length=50, null=True, db_column=b'Staff_Default_Type', blank=True)),
                ('first_name', models.CharField(max_length=50, null=True, db_column=b'Staff_First_Name', blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, db_column=b'Staff_Last_Name', blank=True)),
                ('email', models.CharField(max_length=50, null=True, db_column=b'Staff_E_Mail', blank=True)),
                ('paytype', models.CharField(max_length=50, null=True, db_column=b'Staff_PayType', blank=True)),
                ('birthdate', models.DateTimeField(null=True, db_column=b'Staff_Birthdate', blank=True)),
                ('last_trans', models.CharField(max_length=50, null=True, db_column=b'Staff_Last_Trans', blank=True)),
                ('attendance', models.CharField(max_length=10, null=True, db_column=b'Staff_Attendance', blank=True)),
                ('att_date', models.DateTimeField(null=True, db_column=b'Staff_Att_Date', blank=True)),
                ('pin_req', models.NullBooleanField(db_column=b'Staff_Pin_Req')),
                ('pin', models.CharField(max_length=50, null=True, db_column=b'Staff_PIN', blank=True)),
                ('att_time', models.DateTimeField(null=True, db_column=b'Staff_Att_Time', blank=True)),
                ('default_company', models.IntegerField(db_column=b'default_company')),
                ('default_ml_loc', models.CharField(max_length=3, null=True, db_column=b'default_ML_Loc', blank=True)),
                ('designation', models.ForeignKey(to='staff.Staffdesignation', db_column=b'Staff_Designation')),
            ],
            options={
                'db_table': 'tblStaff',
            },
        ),
    ]
