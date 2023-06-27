from django import forms
import re

from Record.models import Record


class RecordForm(forms.ModelForm):
    deduction_code = forms.Select()
    request_type = forms.Select()
    ec_number = forms.CharField(max_length=8)
    id_number = forms.CharField(max_length=11)
    transaction_refence = forms.CharField(max_length=20)
    deductions_start_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    deductions_end_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    installment_amount = forms.IntegerField(default=0)
    class Meta:
        model = Record
        fields = ['deduction_code', 'request_type','ec_number','id_number',
                  'transaction_refence','deductions_start_date',
                  'deductions_end_date','installment_amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['deduction_code'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['request_type'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['ec_number'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['id_number'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['transaction_refence'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['deductions_start_date'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['deductions_end_date'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        self.fields['installment_amount'].widget.attrs.update(
            {'class': 'form-control form-control-lg'})
        