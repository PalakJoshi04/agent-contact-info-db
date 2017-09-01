from django import forms
from .models import Agent


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['first_name', 'last_name', 'education', 'company_name', 'specialization', 'agent_notes', 'mobileNumber', 'phoneNumber', 'emailID']
