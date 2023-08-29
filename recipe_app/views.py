from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render


def login_view(request):

    form = AuthenticationForm()
    error_message = None

    if request.method == "POST":

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipes:recipe-list')
        else:
            error_message = 'unable to login. please try again and confirm your credentials'

    context = {
        'form' : form,
        'error_message' : error_message
    }
    return render(request, 'auth/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('success')

def success(request):
    return render(request, "auth/success.html")