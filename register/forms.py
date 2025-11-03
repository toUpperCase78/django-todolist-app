from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

# 'Meta' class is created inside this form, because we want to define the fact that the form is going to save 
# into the Users database.
# We need to change the User model whenever we save something in this form.
# This email field does not show up initially. Inside of the parent class, we have to define that.
# Many related fields are already built-in; we just need to type the order of these fields.

# It is recommended to install the package 'django-crispy-forms' with pip.
# The good thing is that it has some automatic styling for our forms.
# Before using that, we have to add this as an installed app, in the project's setting.py file. ('crispy_forms')
# Also, define what kind of CSS layout, framework it's actually going to use. ('CRISPY_TEMPLATE_PACK')
# IMPORTANT: django-crispy-forms 2.x have its template packages separated!.
# Thus, we need to install 'crispy-bootstrap4' or 'crispy-bootstrap5' as well.
# Then, add 'crispy_bootstrap5' as an installed app and appropriately define the template pack.