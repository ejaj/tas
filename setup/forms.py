from django import forms
from .models import Agent, Customer


class AgentForm(forms.ModelForm):
    '''
    Agent Form for create and update single agent.
    '''

    class Meta:
        model = Agent
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    '''
    Customer Form for create and update single customer.
    '''

    class Meta:
        model = Customer
        fields = '__all__'
