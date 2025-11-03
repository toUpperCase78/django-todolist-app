from django import forms

# This forms.py file enables to create forms for your application.

class CreateNewForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200, widget=forms.TextInput(attrs={"style": "width: 500px;"}))
    check = forms.BooleanField(required=False)

# In BooleanField, set 'required=False' to disable the pop-up message when hovered:
# 'Please check this box if you want to proceed.'
# 'forms.Form' is amazing in the way that it automatically checks all of the fields to make sure they have valid input.