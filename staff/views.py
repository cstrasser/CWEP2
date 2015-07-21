import datetime
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from staff.models import Staff
from staff.forms import StaffForm


@login_required
def stafflist(request):
    x=Staff.objects.filter(end_date__isnull = True)     
    context = {'stafflist': x}
    return render(request,'staff/stafflist.html', context)
    
@login_required
def staffform(request,staff_id):
    member = get_object_or_404(Staff, pk=staff_id)
    if request.method=='POST':
        form = StaffForm(request.POST, instance = member)
        if form.is_valid():
            form.save(commit =true)
            return index(request)
        
    else:
      form = StaffForm(instance = member)   
     
    return render(request, 'staff/staffform.html',{'form':form})
    
