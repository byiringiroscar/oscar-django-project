from django.shortcuts import render
from .models import Employee_s


# Create your views here.

def home(request):
    Employ = Employee_s.objects.all()
    context = {
        'employee': Employ
    }
    return render(request, 'html/old.html', context)


def detail_view(request, pksa):
    detail = Employee_s.objects.get(id=pksa)
    prove_d = Employee_s.objects.all()
    print(pksa)

    context = {
        'prove': prove_d,
        'detail': detail
    }
    return render(request, 'html/detail_employee.html', context)
