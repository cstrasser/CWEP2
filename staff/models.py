from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    userid = models.OneToOneField(User)
    number = models.CharField(db_column='Staff_Number', max_length=10, primary_key = True) 
    staffname = models.CharField(db_column='StaffName', max_length=50)  # Field name made lowercase.
    login_id = models.CharField(db_column='Staff_Login_ID', max_length=50, blank=True, null=True)  
     
    phone_ext = models.CharField(db_column='Staff_phone_ext', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cell = models.CharField(db_column='Staff_cell', max_length=50, blank=True, null=True)  # Field name made lowercase.
    home_phone = models.CharField(db_column='Staff_home_phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emg_contact_name = models.CharField(db_column='Staff_contact_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emg_contact_phone = models.CharField(db_column='Staff_contact_phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Staff_Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='Staff_Start_Date', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateTimeField(db_column='Staff_End_Date', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Staff_Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Staff_Note', blank=True, null=True)  # Field name made lowercase.
    default_type = models.CharField(db_column='Staff_Default_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='Staff_First_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Staff_Last_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Staff_E_Mail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(db_column='Staff_Designation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paytype = models.CharField(db_column='Staff_PayType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='Staff_Birthdate', blank=True, null=True)  # Field name made lowercase.
    last_trans = models.CharField(db_column='Staff_Last_Trans', max_length=50, blank=True, null=True)  # Field name made lowercase.
    attendance = models.CharField(db_column='Staff_Attendance', max_length=10, blank=True, null=True)  # Field name made lowercase.
    att_date = models.DateTimeField(db_column='Staff_Att_Date', blank=True, null=True)  # Field name made lowercase.
    pin_req = models.NullBooleanField(db_column='Staff_Pin_Req')  # Field name made lowercase.
    pin = models.CharField(db_column='Staff_PIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    att_time = models.DateTimeField(db_column='Staff_Att_Time', blank=True, null=True)  # Field name made lowercase.
    default_company = models.IntegerField(blank=True, null=True)
    default_ml_loc = models.CharField(db_column='default_ML_Loc', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblStaff'
        
    def __str__(self):
       #return self.name
       return unicode(self.staffname).encode('utf-8')


