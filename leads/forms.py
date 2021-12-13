from django import forms
from leads.models import Lead, Agent, Category
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class LeadForm(forms.ModelForm):
    
    class Meta:
        model = Lead
        fields = ('first_name', 'last_name', 'age', 'agent', 'phone_number')

class CustomUserModelForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username","email")
        field_classes = {'username':UsernameField}

class AssingAgentToLeadForm(forms.Form):
    agents = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        super(AssingAgentToLeadForm, self).__init__(*args, **kwargs)
        self.fields["agents"].queryset = Agent.objects.filter(organisation=request.user.userprofile)

class LeadUpdateCategoryForm(forms.ModelForm):
    
    class Meta:
        model = Lead
        fields = ('category',)