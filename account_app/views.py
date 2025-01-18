from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def user_login(request):
    if request.user.is_authenticated: # if user login
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            return redirect('/account/signup')
        
        login(request, user)
        return redirect('/')
    
    return render(request, 'account_app/signup.html', {})


def user_logout(request):
    logout(request)
    return redirect('/')
    

def register_page(request):
    return render(request, 'account_app/register.html', {})