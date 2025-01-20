from django import forms
from ..models import Customer

class CustomerEditForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email',]
        labels = {
            'name': 'Name',
            'phone': 'Phone Number',
            'email': 'Email Address',
        }


class LoginForm(forms.Form):
    customer_id = forms.CharField(label="Customer ID", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)