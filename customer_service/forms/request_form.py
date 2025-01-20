from django import forms
from ..models import ServiceRequest, Customer

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'request_details', 'attachment']
        exclude = ['customer_id']
        widgets = {
            'request_details': forms.Textarea(attrs={'rows': 4}),
        }
    
    

        