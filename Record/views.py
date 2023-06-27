from django.shortcuts import render,redirect

from Record.models import Record
from Record.forms import RecordForm


def record_registration(request):
    if request.method =='POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect("batch:codes")
    else:
        form = RecordForm()
    return render(request,'dashboard/add-record.html',{'form':form})


# @login_required
def get_records(request):
    records = Record.objects.all()
    return render(request,'dashboard/records.html',{'records':records})
