from django.shortcuts import render
from staff.forms import StaffForm

@login_required
def staffpage(request):
    print "staffpage"
    if request.method=='POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save(commit =true)
            return index(request)
        
    else:
      form = StaffForm()   
     
    return render(request, 'staffform.html',{'form':form})
    
