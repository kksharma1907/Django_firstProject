from django.shortcuts import render
from django.http import HttpResponse  # Import HttpResponse
from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, this is the index page!")

# def home(request):
#     return HttpResponse("Welcome to the Home Page!")

# def contact(request):
#     return HttpResponse("This is the Contact Page.")

# def about(request): 
#     return HttpResponse("This is the About Page.")


def index(request):
    return render(request, 'web/index.html')

def home(request):
    return render(request, 'web/home.html')

def about(request):
    return render(request, 'web/about.html')

def contact(request):
    return render(request, 'web/contact.html')

def login(request):
    return render(request, 'web/login.html')

def create_employee(request):
    employee_details=EmployeeForm()
    return render(request,'web/create_employee.html',{'emp':employee_details})


# def create_employee(request):
#     if request.method == 'POST':
#         employee_details = EmployeeForm(request.POST)

#     else:
#         employee_details = EmployeeForm()

#     return render(request, 'web/create_employee.html', {'emp': employee_details})