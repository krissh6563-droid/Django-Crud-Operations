from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Employees

# Create your views here.
def member(request):
    emp = Employees.objects.all()
    context = {
        'emp':emp,
    }
    return render(request, 'index.html',context)
