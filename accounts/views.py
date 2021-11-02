from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("home")
        else:

            messages.info(request,'User Name & Password Error')
            return render(request, 'login.html')

    else:
        return render(request,'login.html')




def registrations(reguest):
    if reguest.method=='POST':
        first_name =reguest.POST['first_name']
        last_name = reguest.POST['last_name']
        username = reguest.POST['username']
        password1 = reguest.POST['password1']
        password2 = reguest.POST['password2']
        email = reguest.POST['email']

        if password2==password1:
            if User.objects.filter(username=username).exists():
                messages.info(reguest,'Username Taken')
                return redirect('/accounts/registrations/')
            elif User.objects.filter(email=email).exists():
                  messages.info(reguest,'Email Taken')
                  return redirect('/accounts/registrations/')



            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.info(reguest,'Regestations Done ')
        else:
             messages.info (reguest,'password not matching')
             return redirect('/accounts/registrations/')
        return redirect('/accounts/login/')
    else:

        return render(reguest,'registration.html')

def logout(request):
    auth.logout(request)
    return redirect('login')