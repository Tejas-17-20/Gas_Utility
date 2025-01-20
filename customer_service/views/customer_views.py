from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import ServiceRequest, Customer
from ..forms import ServiceRequestForm,CustomerEditForm
from ..forms.request_form import ServiceRequestForm
from ..forms.customer_edit_form import CustomerEditForm,LoginForm
from customer_service.models.customer import Customer

@login_required
def submit_request(request):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('login')

    try:
        customer = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        return redirect('login')

    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = customer
            if service_request.status.lower() == 'resolved':
                service_request.status = 'Resolved'
            service_request.save()
            return redirect('track_request')
    else:
        form = ServiceRequestForm()

    return render(request, 'customer_service/submit_request.html', {
        'form': form,
        'requests': ServiceRequest.objects.filter(customer=customer),
        'customer_id': customer_id,
    })

def customer_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            customer_id = form.cleaned_data['customer_id']
            password = form.cleaned_data['password']
            try:
                customer = Customer.objects.get(customer_id=customer_id)
                if customer.password == password:  
                    request.session['customer_id'] = customer.customer_id
                    return redirect('/submit')  
                else:
                    form.add_error(None, "Invalid customer ID or password.")
            except Customer.DoesNotExist:
                form.add_error(None, "Invalid customer ID or password.")
    else:
        form = LoginForm()

    return render(request, 'customer_service/customer_login.html', {'form': form})

@login_required
def customer_account(request):
    customer_id = request.session.get('customer_id')  
    if not customer_id:  
        return redirect('login')
    
    customer = Customer.objects.filter(customer_id=customer_id).first()  
    
    if not customer: 
        return render(request, 'customer_not_found.html')
    
    return render(request, 'customer_service/customer_account.html', {'customer': customer})

@login_required
def edit_customer_account(request):
    customer_id = request.session.get('customer_id') 
    if not customer_id:
        return redirect('login')
    
    customer = Customer.objects.filter(customer_id=customer_id).first()
    if not customer:
        return redirect('customer_account')  

    if request.method == 'POST':
        form = CustomerEditForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_account')
    else:
        form = CustomerEditForm(instance=customer)
    
    return render(request, 'customer_service/edit_customer_account.html', {'form': form})