from django.db import models
from django.contrib.auth.models import User

class Company(models.Model): # company is newterra co ... LTD INC,SPA
    id = models.AutoField(db_column='id', primary_key=True)
    company = models.CharField("Company Name",max_length=128)
    country = models.CharField(max_length=50)
    company_currency = models.CharField(max_length=50)
    bill_addr1 = models.CharField(max_length=50, blank=True, null=True)
    bill_addr2 = models.CharField(max_length=50, blank=True, null=True)
    bill_city = models.CharField(max_length=50, blank=True, null=True)
    bill_prov_state = models.CharField(max_length=50, blank=True, null=True)
    bill_country = models.CharField(max_length=50, blank=True, null=True)
    bill_pc_zip = models.CharField(max_length=50, blank=True, null=True)
    bill_fax = models.CharField(max_length=50, blank=True, null=True)
    bill_email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblCompany'
        
    def __str__(self):
        print "COMPANY %s" %(self.company)
    
        return (self.company)


class Staffdesignation(models.Model):
    sd_designation = models.CharField(db_column='SD_Designation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sd_id = models.AutoField(db_column='SD_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblS_StaffDesignation'
    def __str__(self):
        return (self.sd_designation)
    
class Staffworktype(models.Model):
    swt_type = models.CharField(db_column='SWT_Type', max_length=50)  # Field name made lowercase.
    swt_id = models.AutoField(db_column='SWT_ID',primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblS_StaffWorkType'
    def __str__(self):
        return (self.swt_type)

class Staff(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='auth_profile')
    '''NOTES on user USER and APES  added the column user_id to the staff table to make the above line work
      added it as int allow null and set it identity specification yes save it .. the save
      autopoputtlates the id's in the existing field then set the seed in the identiy spec to
      greater than the last column and set as primary key '''
    number = models.CharField(db_column='Staff_Number', max_length=10) 
    staffname = models.CharField(db_column='StaffName', max_length=50)  # Field name made lowercase.
    login_id = models.CharField(db_column='Staff_Login_ID', max_length=50, blank=True, null=True)  
    phone_ext = models.CharField(db_column='Staff_phone_ext', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cell = models.CharField(db_column='Staff_cell', max_length=50, blank=True, null=True)  # Field name made lowercase.
    home_phone = models.CharField(db_column='Staff_home_phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emg_contact_name = models.CharField("Emergency contact person",db_column='Staff_contact_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
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
    #designation = models.ForeignKey(Staffdesignation,db_column='Staff_Designation')
    designation = models.CharField(db_column='Staff_Designation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paytype = models.CharField(db_column='Staff_PayType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='Staff_Birthdate', blank=True, null=True)  # Field name made lowercase.
    last_trans = models.CharField(db_column='Staff_Last_Trans', max_length=50, blank=True, null=True)  # Field name made lowercase.
    attendance = models.CharField(db_column='Staff_Attendance', max_length=10, blank=True, null=True)  # Field name made lowercase.
    att_date = models.DateTimeField(db_column='Staff_Att_Date', blank=True, null=True)  # Field name made lowercase.
    pin_req = models.NullBooleanField(db_column='Staff_Pin_Req')  # Field name made lowercase.
    pin = models.CharField(db_column='Staff_PIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    att_time = models.DateTimeField(db_column='Staff_Att_Time', blank=True, null=True)  # Field name made lowercase.
    default_company = models.IntegerField(db_column = 'default_company')
    #default_ml_loc = models.CharField(db_column='default_ML_Loc', max_length=3, blank=True, null=True)
    default_ml_loc = models.ForeignKey('Company',db_column='default_ML_Loc') #, max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        ordering = ['last_name']
        db_table = 'tblStaff'
        
    def __str__(self):
       #return self.name
       if self.last_name:
           return '%s %s' %(self.last_name,self.first_name )
       else:
           return unicode(self.staffname).encode('utf-8')
    
    @property
    def propertyidea(self):
        return "This is from the property decorator"
    
    def get_emergency_contact(self):
        if self.emg_contact_name:
            emergency_contact =  '%s %s' %(self.emg_contact_name,self.emg_contact_phone)
        else:
            emergency_contact = 'No emergency Contact on File'
        return emergency_contact    
    emergency_contact = property(get_emergency_contact)
# the bit of code above will allow you to do x= Staff.emergency_contact x will be the  name and number

    def get_displayfields(self):
        ''' returns list of fieldnames and values for user edit form 
         ... this one is trickey .. allfields makes list of tuples of all fields and values in model (based on a call from one pk)
         then displayfields removes all the tuples that have names we dont want to display in the list ie removes values we can't edit
         and don't have much use on the user (staff) list form remember that the object can still b referneced like: object.staffname''' 
        allfields = [(field.verbose_name.capitalize(), field._get_val_from_obj(self)) for field in self.__class__._meta.fields]
        displayfields = [field for field in allfields if field[0] not in
                         ['Staffname','User','Attendance','Att date','Att time','Last trans']]    
        return displayfields


