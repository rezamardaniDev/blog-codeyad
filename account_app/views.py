from django.shortcuts import render

# Create your views here.
def signup_page(request):
    return render(request, 'account_app/signup.html', {})

def register_page(request):
    return render(request, 'account_app/register.html', {})