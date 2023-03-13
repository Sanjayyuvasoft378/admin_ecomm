from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from .models import *
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus":"True","class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"autocomplete":"current-password","class":"form-control"}))

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"autofocus": "True", "class": "form-control"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(
        attrs={"class": "form-control"}))
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput(
        attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['id','username','email','password1','password2']
    
    
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="old password",widget=forms.PasswordInput(attrs={"autofocus":"True", "autocomplete":"current-password","class":"form-control"}))
    new_password1 = forms.CharField(label="new_password", widget=forms.PasswordInput(attrs={"autocomplete":"current-password","class":"form-control"}))
    new_password2 = forms.CharField(label="confirm_password", widget=forms.PasswordInput(attrs={"autocomplete":"current-password","class":"form-control"}))
    


class MyPasswordResetForm(PasswordChangeForm):
    pass

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','locality','city','mobileNo','state','zipcode']
        widget = {
            'name':forms.TextInput(attrs={'class':"form-control"}),
            'locality':forms.TextInput(attrs={'class':"form-control"}),
            'city':forms.TextInput(attrs={'class':"form-control"}),
            'mobileNo':forms.NumberInput(attrs={'class':"form-control"}),
            'state':forms.Select(attrs={'class':"form-control"}),
            'zipcode':forms.NumberInput(attrs={'class':"form-control"}),
        }
        
        
        
class AddToCartForm(forms.ModelForm):
    class Meta:
        model = AddToCartModel
        fields = ['product_id','qty']
        widget = {
            'product_id':forms.TextInput(attrs={'class':'form-control'}),
            'qty':forms.NumberInput(attrs={'class':'form-control'})
        }
        
class AddToWishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['product_id','qty']
        widget = {
            'product_id':forms.TextInput(attrs={'class':'form-control'}),
            'qty':forms.NumberInput(attrs={'class':'form-control'})
        }
