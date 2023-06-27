from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from Company.models import Company
from Company.forms import CompanyForm

def company_registration(request):
    if request.method =='POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("company:companies")
    else:
        form = CompanyForm()
    return render(request,'company/add-company.html',{'form':form})


# @login_required
def get_companies(request):
    companies = Company.objects.all()
    return render(request,'company/companies.html',{'companies':companies})
