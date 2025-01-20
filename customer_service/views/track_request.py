from django.shortcuts import render, redirect
from django.http import Http404
from ..models import ServiceRequest

def track_request(request):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('login') 

    requests = ServiceRequest.objects.filter(customer__customer_id=customer_id)
    return render(request, 'customer_service/track_request.html', {'requests': requests, 'customer_id': customer_id})
