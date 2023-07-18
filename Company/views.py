from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from Company.models import Company
from Company.forms import CompanyForm

def company_registration(request):
    if request.method =='POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save()
            Group.objects.create(name = company.name)
            return redirect("company:companies")
    else:
        form = CompanyForm()
    return render(request,'company/add-company.html',{'form':form})


@login_required
def get_companies(request):
    companies = Company.objects.all()
    return render(request,'company/companies.html',{'companies':companies})

@login_required
def company_dashboard(request):
    return render(request,'dashboard/dashboard.html')

