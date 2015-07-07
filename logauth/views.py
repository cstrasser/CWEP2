from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def ntlogin(request):
       
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
             print("User is valid, active and authenticated")
             login(request,user)
             return render(request,'logauth/success.html',{'username':user})
            else:
                print("The password is valid, but the account has been disabled!")
                #use django messages here to show error on user screen
        else:
         print("The username and password were incorrect.")
          #use django messages here to show error on user screen
         
    else:
        return render(request,'logauth/loginform.html')
     
def about(request):
    return render(request,'about.html')


@login_required
def user_logout(request):
    logout(request)
    
    return redirect('http://newterra.com')

