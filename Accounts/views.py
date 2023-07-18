from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import check_password
from django.contrib import messages

from Record.models import Record
from .forms import *

from Company.models import Company
from Batch.models import Batch

def is_client(user):
    return user.groups.filter(name='clients').exists()
def is_agent(user):
    return user.groups.filter(name='agents').exists()
def is_admin(user):
    return user.groups.filter(name='admins').exists()

def is_under_group(user):
    for group in Group.objects.all():
        if user.groups.filter(name=group.name).exists():
            return True
    return False
    
        

def home_page(request):
    return render(request,"index.html")

@login_required
def check_company(request):
    user = request.user
    if is_under_group(user):
        group_name = user.groups.values_list('name', flat=True)[0]
        company = Company.objects.get(name= group_name)
        request.session['company_id'] = str(company.id)
        request.session['company'] = company.name
        return redirect('record:records')
    else:
        messages.error(request,"User is not allowed to access this portal.")
        return redirect('accounts:login')

def verify_password(request,batch_id):
    if request.method == 'POST':
        password = request.POST.get('current_password')
        security_key = request.POST.get('security_key')
        confirm_security_key = request.POST.get('security_key_confirm')
        user = request.user
        if check_password(password, user.password):
            if security_key == confirm_security_key:
                account =user.user_account_info
                account.security_code = security_key
                account.save()
                batch = Batch.objects.get(id=batch_id)
                records = batch.batch_records.all()
                for record in records:
                    record.status = Record.Status.SENT
                    record.save()
                batch.status = Batch.Status.SENT
                batch.save()
                return redirect('record:records')
            else:
                #Security key does not match
                messages.error(request,"Security key does not match")
                return redirect('accounts:add_security_code')
        else:
            #Password does not match
            messages.error(request,"Password does not match.")
            return redirect('accounts:add_security_code')
    else:
        return render(request,'auth/security-key.html')

    # Check if the entered password matches the stored password hash
    if check_password(password, user.password):
        pass
        # Passwords match
    # else:
        
    #     pass
        # Passwords don't match

#staff account creation
def staff_account_creation(request):
    if request.method =='POST':
        form = StaffSignUp(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            group  = Group.objects.get(name=request.session.get('company'))
            user.save()
            group.user_set.add(user)
            return redirect('accounts:view_accounts')
    else:
        form = StaffSignUp()
    return render(request,'auth/add-user.html',{'form':form})

@login_required
def get_company_users(request):
    users = User.objects.filter(groups__name = request.session.get('company'))
    return render(request,'auth/users.html',{'users':users})

@login_required
def profile_check(request):
    if is_client(request.user):
        return redirect("applicant:client_profile")
    elif is_agent(request.user):
        return redirect("agent:agent_profile")
    else:
        return redirect('admin:index')