from django.shortcuts import render, HttpResponse 
from django.contrib.auth.decorators import login_required

@login_required
def navpage(request):
    #return redirect('/navpage/')  
    return render(request, 'navpage.html', {})
    
   