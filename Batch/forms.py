from django import forms
import re

from Batch.models import DeductionCode


class DeductionCodeForm(forms.ModelForm):
    company = forms.Select()
    currency = forms.Select()
    class Meta:
        model = DeductionCode
        fields = ['company', 'currency']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['currency'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})