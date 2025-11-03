from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/login")
        # return render(response, "registeration/login.html", 
        #               {"register_success": "User registration successful. Now login with the same credentials..."})
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})

def logout_view(response):
    logout(response)
    return redirect("/")

# Thankfully, Django creates the common form for user register and login automatically for us.
# It typically generates several texts, some input forms:
#   Username: Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
#   Password:
#     - Your password can't be too similar to your other personal information.
#     - Your password must contain at least 8 characters.
#     - Your password can't be a commonly used password.
#     - Your password can't be entirely numeric.
#   Password Confirmation: Enter the same password as before, for verification.
# After successful registry, you can check the Users table from the admin page, and see the newly added user.