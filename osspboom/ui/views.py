from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def view_details(request):
    return render(request, 'view_details.html')