from django.db import models

class Customer(models.Model):
    customer = models.AutoField(db_column='CustNameID', primary_key = True)  # CJS added primary key =true for DJANGO.
    name = models.CharField(db_column='CustName', primary_key=True, max_length=100)  
    url = models.CharField(db_column='CustWebAddr', max_length=50, blank=True, null=True)  
    category = models.CharField(db_column='CustCategory', max_length=20, blank=True, null=True)  
    designfeatures = models.TextField(db_column='CustDesignFeatures', blank=True, null=True)  
    enteredby = models.CharField(db_column='CustEnteredBy', max_length=50, blank=True, null=True)  
    created = models.DateTimeField(db_column='CustEnteredDate', blank=True, null=True)  
    msa = models.CharField(db_column='CustMSA', max_length=50, blank=True, null=True)  
    msa_details = models.TextField(db_column='CustMSA_Details', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'tblS_Customers'
    
    def __str__(self):
       #return self.name
       return unicode(self.name).encode('utf-8')



class LocationMaster(models.Model):
    location_id = models.AutoField(db_column='CusLocID', primary_key=True)  
    addr1 = models.CharField(db_column='CLAddr1', max_length=50, blank=True, null=True)  
    addr2 = models.CharField(db_column='CLAddr2', max_length=50, blank=True, null=True)  
    city = models.CharField(db_column='CLCity', max_length=50)  
    provstate = models.CharField(db_column='CLProvState', max_length=50)  
    country = models.IntegerField(db_column='CLCountry')  
    pczip = models.CharField(db_column='CLPCZip', max_length=50, blank=True, null=True)  
    fax = models.CharField(db_column='CLFax', max_length=50, blank=True, null=True)  
    email = models.CharField(db_column='CLEmail', max_length=50, blank=True, null=True)  
    phone = models.CharField(db_column='CLPhone', max_length=50, blank=True, null=True)  
    irsnum = models.CharField(db_column='CLIRSNum', max_length=50, blank=True, null=True)  
    disc = models.IntegerField(db_column='CLDisc', blank=True, null=True)  
    notes = models.TextField(db_column='CLNotes', blank=True, null=True)  
    credit_status = models.CharField(db_column='CLCreditStatus', max_length=30, blank=True, null=True)  
    credit_status_date = models.DateTimeField(db_column='CLCreditStatDate', blank=True, null=True)  
    bill_office = models.NullBooleanField(db_column='CLBillOffice')  
    status = models.CharField(db_column='CLStatus', max_length=20)  
    simply_xref = models.IntegerField(db_column='CLSimplyXRef', blank=True, null=True)  
    contact_type = models.CharField(db_column='ClContactType', max_length=50)  
    contact_sub_type = models.CharField(db_column='CLContSubType', max_length=50, blank=True, null=True)  
    #conact_name_id = models.IntegerField(db_column='CLCoNameID', blank=True, null=True)  
    customer = models.ForeignKey(Customer,db_column='CLCoNameID') # blank=True, null=True) ##################ForeignKey
    pstexempt = models.CharField(db_column='CLPSTExempt', max_length=20, blank=True, null=True)  
    gstexempt = models.CharField(db_column='CLGSTExempt', max_length=20, blank=True, null=True)  
    default_tax_code = models.CharField(db_column='CLDefTaxCode', max_length=2, blank=True, null=True)  
    bill_to_default = models.IntegerField(db_column='CLBillToDefault', blank=True, null=True)  
    default_commission_rate = models.FloatField(db_column='CLDefCommRate', blank=True, null=True)  
    enteredy = models.CharField(db_column='CLEnteredBy', max_length=50, blank=True, null=True)  
    entered_date = models.DateTimeField(db_column='CLEnteredDate', blank=True, null=True)  
    modified_by = models.CharField(db_column='CLModifiedBy', max_length=50, blank=True, null=True)  
    modified_date = models.DateTimeField(db_column='CLModifiedDate', blank=True, null=True)  
    rank = models.FloatField(db_column='CL_Rank', blank=True, null=True)  
    peoplefocused = models.CharField(db_column='CL_PeopleFocused', max_length=50, blank=True, null=True)  
    annual_system = models.IntegerField(db_column='CL_AnnualSystem', blank=True, null=True)  
    type_of_sites = models.CharField(db_column='CL_TypeofSites', max_length=50, blank=True, null=True)  
    customer_focus = models.CharField(db_column='CL_CustomerFocus', max_length=50, blank=True, null=True)  
    big_customers = models.CharField(db_column='CL_BigCustomers', max_length=50, blank=True, null=True)  
    other_markets = models.CharField(db_column='CL_OtherMarkets', max_length=50, blank=True, null=True)  
    vendor1 = models.CharField(db_column='CL_Vendor1', max_length=50, blank=True, null=True)  
    vendor2 = models.CharField(db_column='CL_Vendor2', max_length=50, blank=True, null=True)  
    vendor3 = models.CharField(db_column='CL_Vendor3', max_length=50, blank=True, null=True)  
    prospect = models.NullBooleanField(db_column='CL_Prospect')  
    cust_class = models.CharField(db_column='CL_Cust_Class', max_length=50, blank=True, null=True)  
    market = models.CharField(db_column='CL_Market', max_length=50, blank=True, null=True)  
    def_tax = models.CharField(db_column='CL_Def_Tax', max_length=50, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'tblS_CusLocMaster'
    
    def __str__(self):
       #return '%s %s %s %s %s' %(self.addr1, self.addr2, self.city, self.country, Customer.customer)    
        #return '%s %s %s %s ' %(self.addr1, self.addr2, self.city, self.country) # original line that works
        q= '%s %s %s %s ' %(self.addr1, self.addr2, self.city, self.country)
        return unicode(q).encode('utf-8')

class Contact(models.Model):
    contact_id = models.AutoField(db_column='CC_ConID', primary_key=True)  
    #location_id = models.IntegerField(db_column='CC_CompLocID')  
    location = models.ForeignKey(LocationMaster, db_column='CC_CompLocID') #,db_column='CusLocID')
    customer_city = models.CharField(db_column='CC_CustCity', max_length=50, blank=True, null=True)  
    first_name = models.CharField(db_column='CC_Name_First', max_length=50)  
    middle_name = models.CharField(db_column='CC_Name_Middle', max_length=50, blank=True, null=True)  
    last_name = models.CharField(db_column='CC_Name_Last', max_length=50)  
    email = models.CharField(db_column='CC_Email', max_length=255, blank=True, null=True)  
    direct_phone = models.CharField(db_column='CC_PhoneDirect', max_length=50, blank=True, null=True)  
    cell = models.CharField(db_column='CC_Cell', max_length=50, blank=True, null=True)  
    pager = models.CharField(db_column='CC_Pager', max_length=50, blank=True, null=True)  
    home_phone = models.CharField(db_column='CC_Home_Phone', max_length=50, blank=True, null=True)  
    description = models.CharField(db_column='CC_Desc', max_length=50)  
    extension = models.CharField(db_column='CC_Ext', max_length=50, blank=True, null=True)  
    birthday = models.DateTimeField(db_column='CC_Birthday', blank=True, null=True)  
    spouse = models.CharField(db_column='CC_Spouse', max_length=50, blank=True, null=True)  
    notes = models.TextField(db_column='CC_Notes', blank=True, null=True)  
    rec_newsletter = models.BooleanField(db_column='CC_Rec_Newsletter')  
    full_name = models.CharField(db_column='CC_Full_Name', max_length=50)  
    title_courtesy = models.CharField(db_column='CC_Title_Courtesy', max_length=8)  
    title_suffix = models.CharField(db_column='CC_Title_Suffix', max_length=8, blank=True, null=True)  
    cctype = models.CharField(db_column='CC_Type', max_length=50)  
    status = models.CharField(db_column='CC_Status', max_length=10)  
    date_last_changed = models.DateTimeField(db_column='CC_DtLastChg', blank=True, null=True)  
    entered_by = models.CharField(db_column='CC_EnteredBy', max_length=50, blank=True, null=True)  
    entered_date = models.DateTimeField(db_column='CC_EnteredDate', blank=True, null=True)  
    modified_by = models.CharField(db_column='CC_ModifiedBy', max_length=50, blank=True, null=True)  
    modified_date = models.DateTimeField(db_column='CC_ModifiedDate', blank=True, null=True)  
    no_newsletter = models.NullBooleanField(db_column='CC_No_Newsletter')  
    prospect = models.NullBooleanField(db_column='CC_Prospect')  

    class Meta:
        managed = False
        db_table = 'tblS_CustContact'     
        
    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)




class STO(models.Model):
    stid = models.SmallIntegerField(db_column='STID', primary_key=True)  
    #customer = models.IntegerField(db_column='STCustomer', blank=True, null=True)  
    customer_location = models.ForeignKey(LocationMaster,db_column='STCustomer')                           #foreignKey
    project = models.CharField(db_column='STProjNum', max_length=50, blank=True, null=True)  
    entrydate = models.DateTimeField(db_column='STEntryDate')  
    status = models.CharField(db_column='STStatus', max_length=15, blank=True, null=True)  
    notes = models.TextField(db_column='STNotes', blank=True, null=True)  
    person_responsible = models.CharField(db_column='STRespPerson', max_length=20, blank=True, null=True)  
    billing = models.CharField(db_column='STBilling', max_length=10)  
    hotel = models.IntegerField(db_column='STHotel', blank=True, null=True)  
    perdiem = models.IntegerField(db_column='STPerDiem', blank=True, null=True)  
    mileage = models.IntegerField(db_column='STMileage', blank=True, null=True)  
    travel_hrs = models.IntegerField(db_column='STTravel(hrs)', blank=True, null=True)   
    sitework_hrs = models.IntegerField(db_column='STSiteWork(hrs)', blank=True, null=True)   
    on_site_date = models.DateTimeField(db_column='STOn_Site_Date', blank=True, null=True)  
    tech = models.CharField(db_column='STTech', max_length=50, blank=True, null=True)  
    billingnotes = models.TextField(db_column='STBillingNotes', blank=True, null=True)  
    invoicenumber = models.CharField(db_column='STInvoiceNumber', max_length=15, blank=True, null=True)  
    oldstcustomer = models.CharField(db_column='OLDSTCustomer', max_length=50, blank=True, null=True)  
    oldstcontact = models.CharField(db_column='OLDSTContact', max_length=50, blank=True, null=True)  
    billingdate = models.DateTimeField(db_column='STBillingDate', blank=True, null=True)  
    materials = models.DecimalField(db_column='STMaterials', max_digits=19, decimal_places=4, blank=True, null=True)  
    labour = models.DecimalField(db_column='STLabour', max_digits=19, decimal_places=4, blank=True, null=True)  
    total = models.DecimalField(db_column='STTotal', max_digits=19, decimal_places=4, blank=True, null=True)  
    reference = models.CharField(db_column='STReference', max_length=50, blank=True, null=True)  
    phone = models.CharField(db_column='STPhone', max_length=50, blank=True, null=True)  
    add1 = models.CharField(db_column='STAdd1', max_length=50, blank=True, null=True)  
    add2 = models.CharField(db_column='STAdd2', max_length=50, blank=True, null=True)  
    add3 = models.CharField(db_column='STAdd3', max_length=50, blank=True, null=True)  
    city = models.CharField(db_column='STCity', max_length=50, blank=True, null=True)  
    state = models.CharField(db_column='STState', max_length=50, blank=True, null=True)  
    stzip = models.CharField(db_column='STZip', max_length=50, blank=True, null=True)  
    tag = models.CharField(db_column='STTag', max_length=50, blank=True, null=True)  
    fedid = models.CharField(db_column='STFedID', max_length=50, blank=True, null=True)  
    cell = models.CharField(db_column='STCell', max_length=50, blank=True, null=True)  
    email = models.CharField(db_column='STEmail', max_length=50, blank=True, null=True)  
    ship_prior = models.CharField(db_column='STShipPrior', max_length=10, blank=True, null=True)  
    ship_cost = models.DecimalField(db_column='STShipCost', max_digits=19, decimal_places=4, blank=True, null=True)  
    ship_method = models.CharField(db_column='STShipMethod', max_length=50, blank=True, null=True)  
    technician_rate = models.DecimalField(db_column='STTechRate', max_digits=19, decimal_places=4, blank=True, null=True)  
    travle_rate = models.DecimalField(db_column='STTravRate', max_digits=19, decimal_places=4, blank=True, null=True)  
    mileage_rate = models.DecimalField(db_column='STMileRate', max_digits=19, decimal_places=4, blank=True, null=True)  
    perdeim_rate = models.DecimalField(db_column='STPerDeimRate', max_digits=19, decimal_places=4, blank=True, null=True)  
    hotel_rate = models.DecimalField(db_column='STHotelRate', max_digits=19, decimal_places=4, blank=True, null=True)  
    action_required = models.CharField(db_column='STActionReq', max_length=20, blank=True, null=True)  
    schedueld_date = models.DateTimeField(db_column='STSchDate', blank=True, null=True)  
    country = models.IntegerField(db_column='STCountry', blank=True, null=True)  
    description = models.TextField(db_column='STDescription', blank=True, null=True)  
    acknowledge = models.NullBooleanField(db_column='STAcknowledge')  
    custdesc = models.TextField(db_column='STCustDesc', blank=True, null=True)  
    customer_po = models.CharField(db_column='STCustPO', max_length=34, blank=True, null=True)  
    bill_coloc = models.IntegerField(db_column='STBillCoLoc', blank=True, null=True)  
    bill_contact = models.IntegerField(db_column='STBillContact', blank=True, null=True)  
    contact = models.IntegerField(db_column='STContact', blank=True, null=True)
    #contact = models.ForeignKey(Contact, db_column='STContact') #, blank=True, null=True) ##
    project_manager = models.CharField(db_column='STProj_Mgr', max_length=50, blank=True, null=True)  
    priority = models.CharField(db_column='STPriority', max_length=30, blank=True, null=True)  
    date_closed = models.DateTimeField(db_column='STCloseDate', blank=True, null=True)  
    tracking_flag = models.NullBooleanField(db_column='STTrackFlag')  
    contact2 = models.IntegerField(db_column='STContact2', blank=True, null=True)  
    customer2 = models.IntegerField(db_column='STCustomer2', blank=True, null=True)  
    repcontact = models.IntegerField(db_column='STRepContact', blank=True, null=True)  
    currency = models.CharField(db_column='STCurr', max_length=3, blank=True, null=True)  
    st_type = models.CharField(db_column='ST_Type', max_length=15)  
    st_dla = models.DateTimeField(db_column='ST_DLA', blank=True, null=True)  
    st_days_att = models.IntegerField(db_column='ST_Days_Att', blank=True, null=True)  
    terms = models.CharField(db_column='ST_Terms', max_length=50, blank=True, null=True)  
    taxcode = models.CharField(db_column='ST_TAXCode', max_length=2, blank=True, null=True)  
    st_commrate = models.FloatField(db_column='ST_CommRate', blank=True, null=True)  
    stsalescomp = models.IntegerField(db_column='STSalesComp', blank=True, null=True)  
    tax1 = models.FloatField(db_column='ST_Tax1', blank=True, null=True)  
    tax2 = models.FloatField(db_column='ST_Tax2', blank=True, null=True)  
    county = models.CharField(db_column='ST_County', max_length=50, blank=True, null=True)  
    commadder = models.FloatField(db_column='STCommAdder', blank=True, null=True)  
    account_type = models.CharField(db_column='ST_Account_Type', max_length=50, blank=True, null=True)  
    quote = models.CharField(db_column='ST_Quote', max_length=50, blank=True, null=True)  
    all_po_sent = models.NullBooleanField(db_column='ST_AllPOSent')  
    segment = models.CharField(db_column='ST_Segment', max_length=50, blank=True, null=True)  
    site_type = models.CharField(db_column='ST_Site_Type', max_length=50, blank=True, null=True)  
    invoice_comment = models.CharField(db_column='ST_Invoice_Comment', max_length=100, blank=True, null=True)  
    def_gl = models.IntegerField(db_column='ST_Def_GL', blank=True, null=True)  
    def_dept = models.IntegerField(db_column='ST_Def_Dept', blank=True, null=True)  
    def_cogs_gl = models.IntegerField(db_column='ST_Def_COGS_GL', blank=True, null=True)  
    def_cogs_dept = models.IntegerField(db_column='ST_Def_COGS_Dept', blank=True, null=True)  
    company_to_invoice_from = models.IntegerField(db_column='STCompany')  # INC or LTD

    class Meta:
        managed = False
        db_table = 'tblServiceTask'
     
    def __str__(self):
        return unicode(self.stid)

