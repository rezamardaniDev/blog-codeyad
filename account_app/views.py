from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def signup_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            return redirect('/account/signup')
        
        return redirect('/account/register')
    
    return render(request, 'account_app/signup.html', {})

def register_page(request):
    return render(request, 'account_app/register.html', {})