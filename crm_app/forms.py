from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _
from .models import *


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))




class ProductForm(forms.ModelForm):
    class Meta:
        model = Prodcut
        fields = ['name', 'price', 'description', 'duration', 'commission','product_img']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),'price':forms.NumberInput(attrs={'class':'form-control'}),'description':forms.Textarea(attrs={'class':'form-control'}),'duration':forms.TextInput(attrs={'class':'form-control'}),'commission':forms.NumberInput(attrs={'class':'form-control'})}
        

class UpiForm(forms.ModelForm):
    class Meta:
        model = upi
        fields = ['select_upi', 'upi_number']
        labels = {'select_upi':'Select Upi','upi_number':'Upi Number'}
        widgets = {'select_upi':forms.Select(attrs={'class':'form-control'}),'upi_number':forms.TextInput(attrs={'class':'form-control'})}
        

class KycForm(forms.ModelForm):
    class Meta:
        model = kyc
        fields = ['holder_name', 'account_number','bank_name','branch','ifsc_code']
        labels = {'holder_name':'Holder Name','account_number':'Account Number', 'bank_name':'Bank'}
        widgets = {'holder_name':forms.TextInput(attrs={'class':'form-control'}),'account_number':forms.NumberInput(attrs={'class':'form-control'}),'bank_name':forms.TextInput(attrs={'class':'form-control'}),'branch':forms.TextInput(attrs={'class':'form-control'}),'ifsc_code':forms.TextInput(attrs={'class':'form-control'})}
        