from django.shortcuts import render,redirect

# Create your views here.

from Batch.models import Batch, DeductionCode
from Batch.forms import DeductionCodeForm

def deduction_code_registration(request):
    if request.method =='POST':
        form = DeductionCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("batch:codes")
    else:
        form = DeductionCodeForm()
    return render(request,'deductioncode/add-deduction-code.html',{'form':form})


# @login_required
def get_deduction_codes(request):
    codes = DeductionCode.objects.all()
    return render(request,'deductioncode/deduction-codes.html',{'codes':codes})