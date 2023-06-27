from django import forms
import re

from Company.models import Company

#Applicant Form 1
class CompanyForm(forms.ModelForm):
    name = forms.CharField(max_length=250)
    class Meta:
        model = Company
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})