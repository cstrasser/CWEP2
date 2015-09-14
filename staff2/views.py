from django.shortcuts import render
from django.views.generic import TemplateView ,ListView , UpdateView, DetailView
from staff.models import Staff


class StaffListView(ListView):
    queryset = Staff.objects.filter(status = 'Full Time').order_by('last_name')
    context_object_name = 'Staff_List'  #defaults to object_list so you could omit this line 
   
class StaffUpdateView(UpdateView):
    model = Staff
    context_object_name = 'staffmember'
    fields  = ('staffname','first_name' ,'last_name', 'home_phone')
    
    
class StaffDetailView(DetailView):
    model = Staff
    context_object_name = 'staffmember'
    
    
    
    
    

