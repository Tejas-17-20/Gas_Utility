from django.urls import path
from .views import (
    customer_login,
    submit_request,
    track_request,
    edit_customer_account,
    customer_account,
)

urlpatterns = [
    path('', customer_login, name='login'),  
    path('login/', customer_login, name='customer_login'),  
    path('account/', customer_account, name='customer_account'),
    path('account/edit/', edit_customer_account, name='edit_account'), 
    
    path('submit/', submit_request, name='submit_request'), 
    path('track/', track_request, name='track_request'),  
]
    