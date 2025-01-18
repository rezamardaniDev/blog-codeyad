from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def user_login(request):
    if request.user.is_authenticated: # if user login
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password)
        
        print(user)
        
        if user is None:
            return redirect('/account/login')
        
        login(request, user)
        return redirect('/')
    
    return render(request, 'account_app/signup.html', {})


def user_logout(request):
    logout(request) 
    return redirect('/')
    

def register_page(request):
    context = {'errors' : []}
    if request.user.is_authenticated: # if user login
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            context['errors'].append('پسورد ها یکسان نیستند')
            return render(request, 'account_app/register.html', context)
        
        if User.objects.filter(username=username).exists():
             context['errors'].append('این نام کاربری قبلا ثبت شده')
             return render(request, 'account_app/register.html', context)
                
        user = User.objects.create_user(username=username, password=password)
        user.save()
        
        login(request, user)
        return redirect('/')
        
    return render(request, 'account_app/register.html', {})