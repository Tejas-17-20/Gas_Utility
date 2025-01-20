# Consumer Services Portal

A Django application to provide consumer services for gas utilities.

## Overview

This portal allows customers to create and track service requests while enabling support representatives to manage customer information and requests.

Refer to the **"Case_study_solution.pdf"** for a detailed solution.

---

## Features

### For Customers
- **/login**: Customer login
- **/submit**: Submit a service request
- **/track**: Track submitted requests
- **/account**: View customer information
- **/account/edit**: Edit customer details (e.g., Name, Email, Phone number)

### For Support Representatives
- **/admin**: Add/Manage customers and service requests (e.g., modify status)

---

## Directory Structure

Directory structure:
```
└── Gas_Utility/
    ├── README.md
    ├── LICENSE
    ├── db.sqlite3
    ├── manage.py
    ├── customer_service/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    │   ├── __pycache__/
    │   ├── forms/
    │   │   ├── __init__.py
    │   │   ├── customer_edit_form.py
    │   │   ├── request_form.py
    │   │   └── __pycache__/
    │   ├── migrations/
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_remove_servicerequest_customer_name_customer_address_and_more.py
    │   │   ├── 0003_rename_phone_number_customer_phone_and_more.py
    │   │   ├── __init__.py
    │   │   └── __pycache__/
    │   ├── models/
    │   │   ├── __init__.py
    │   │   ├── customer.py
    │   │   ├── service_request.py
    │   │   └── __pycache__/
    │   ├── templates/
    │   │   └── customer_service/
    │   │       ├── customer_account.html
    │   │       ├── customer_login.html
    │   │       ├── edit_customer_account.html
    │   │       ├── submit_request.html
    │   │       └── track_request.html
    │   └── views/
    │       ├── __init__.py
    │       ├── customer_views.py
    │       ├── track_request.py
    │       └── __pycache__/
    └── gas_utility_service/
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        ├── wsgi.py
        └── __pycache__/
```

---

## Temporary Credentials for Testing
Use the following credentials to log in as a customer:
- **Customer ID**: `test`
- **Password**: `test`

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Setup Instructions
1. Clone the repository:
   ```git clone https://github.com/kushalzinzuvadia/consumer-services-portal.git```

2. Navigate to the project directory:
    ```cd kushal-zinzuvadia-consumer-services-portal```

3. Install the required dependencies:
    ```pip install -r requirements.txt```

4. Run migrations:
    ```python manage.py migrate```

5. Start the development server:
    ```python manage.py runserver```
 
6. Access the portal at http://127.0.0.1:8000

---

Author: Tejas Dehade
