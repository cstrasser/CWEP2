from django.shortcuts import render
from django.contrib.auth import authenticate 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf

def login(request):
    context = {}
    
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print user 
        if user is not None:
            if user.is_active:
             print("User is valid, active and authenticated")
             return render(request,'logauth/success.html',{'username':user})
            else:
                print("The password is valid, but the account has been disabled!")
        else:
         print("The username and password were incorrect.")
         return render(request,'logauth/loginform.html',context)
        
    else:
     print "got Here ======================================"
     return render(request,'logauth/loginform.html', context)
     
    


# from django.contrib.auth import authenticate
# user = authenticate(username='john', password='secret')
# if user is not None:
#     # the password verified for the user
#     if user.is_active:
#         print("User is valid, active and authenticated")
#     else:
#         print("The password is valid, but the account has been disabled!")
# else:
#     # the authentication system was unable to verify the username and password
#     print("The username and password were incorrect.")
#https://docs.djangoproject.com/en/1.8/topics/auth/default/