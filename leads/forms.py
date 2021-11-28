from django import forms
from leads.models import Lead
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class LeadForm(forms.ModelForm):
    
    class Meta:
        model = Lead
        fields = ('first_name', 'last_name', 'age', 'agent')

class CustomUserModelForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username","email")
        field_classes = {'username':UsernameField}
