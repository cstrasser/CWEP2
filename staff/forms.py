from django import forms
from logauth.models import Staff

class StaffForm(forms.ModelForm):
    number  = forms.CharField(max_length=10, help_text="Employee ID number")
    login_id = forms.CharField(max_length=12, help_text="Like rkennedy")
    home_phone = forms.CharField(max_length=50, )
    emg_contact_name = forms.CharField(max_length=50, )
    emg_contact_phone = forms.CharField(max_length=50, )
    #userid = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Staff
        #fields = ('staffname','login_id')
        exclude = ('designation',)
        
        
    
