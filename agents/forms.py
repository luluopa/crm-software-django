from django import forms
from leads.models import Agent
from leads.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class AgentModelForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name' 
        )