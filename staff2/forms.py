from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from crispy_forms.bootstrap import TabHolder, Tab

from staff.models import Staff

FIELDLIST = ['number', 'staffname',  'login_id','first_name', 'last_name', 'address','cell','home_phone','email','birthdate',
                'emg_contact_name',  'emg_contact_phone',
                'start_date','end_date','status',
                'pin_req','pin',
                'note',
                'default_type','designation','paytype',
                'default_company', 'default_ml_loc']



class StaffForm(forms.ModelForm):
    
    class Meta:
        model = Staff
        fields = FIELDLIST
        
    def __init__(self, *args, **kwargs):
        #self.key = kwargs.pop('key') 
        super(StaffForm, self).__init__(*args, **kwargs)
             
        #print 'PRIMARY KEY IS: %s'  %(self.key)
        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"    
        
        self.helper.layout = layout.Layout(
            layout.Fieldset('Employee Number {{form.number}}',
                            css_class='input class="form-control" type="text" readonly'),
            layout.Fieldset(
               ("Employee Data"),
               #layout.Div(bootstrap.PrependedText("staffname", """<span class="glyphicon glyphicon-user"></span>""",
                #                                  css_class="input"),),
               layout.Div(bootstrap.PrependedText("first_name", """<span class="glyphicon glyphicon-user"></span>""",
                                                  css_class="input-block-level"),),
               layout.Div(bootstrap.PrependedText("last_name", """<span class="glyphicon glyphicon-user"></span>""",
                                                  css_class="input-block-level"),),
               layout.Div(bootstrap.PrependedText("home_phone", """<span class="glyphicon glyphicon-earphone"></span>""",
                                                  css_class="input-block-level"),),
               layout.Div(bootstrap.PrependedText("cell", """<span class="glyphicon glyphicon-earphone"></span>""",
                                                  css_class="input-block-level"),),
               layout.Div(bootstrap.PrependedText("address", """<span class="glyphicon glyphicon-home"></span>""",
                                                  css_class="input-block-level"),),
               layout.Div(bootstrap.PrependedText("birthdate", """<span class="glyphicon glyphicon-calendar"></span>""",
                                                  css_class="input-block-level"),),  
            ),
            layout.Fieldset(
               ("Emerg Contact Info"),
               layout.Div(bootstrap.PrependedText("emg_contact_name", """<span class="glyphicon glyphicon-user"></span>""",
                                                  css_class="input-block-level"),),
               layout.Div(bootstrap.PrependedText("emg_contact_phone", """<span class="glyphicon glyphicon-earphone"></span>""",
                                                  css_class="input-block-level"),), 
            ),
            layout.Fieldset(
               ("newterra Info"),
               layout.Div(bootstrap.PrependedText("default_company", """<span class="glyphicon glyphicon-home"></span>""",
                                                  css_class="input-block-level"),),
               layout.Div(bootstrap.PrependedText("default_ml_loc", """<span ></span>""",
                                                  css_class="input-block-level"),),     
            ),
            TabHolder(
                   Tab('First Tab',  'emg_contact_name' ),    Tab('Second Tab',    'birthdate', css_class="extra")
    ),
)
    
     
        
        
        
        
        
        
        
            