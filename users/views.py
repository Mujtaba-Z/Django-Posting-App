from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def register_view(request):
    if request.method == "POST": ### Submit button redirects to the same users/register page. So here we are taking the new request and redirecting to posts page
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("posts:list") ### Referencing posts app by appname and then list name for the specific page
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get('next')) ### Getting field 'next' value from our input that we kept hidden in html
            else:
                return redirect("posts:list") ### Redirect back to the same page
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("posts:list")