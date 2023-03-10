from django import forms
from .models import *
class Addproductform(forms.Form):
    error_css_class = "error"
    
    file = forms.ImageField()


class MainCatForm(forms.Form):
    error_css_class = "error"
    category_name=forms.CharField(max_length=250, required=True, widget=forms.TextInput(attrs={'class': "form-control input-lg", "placeholder":'category_name'}))
    description = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class': "form-control input-lg","placeholder":'description'}))
    cate_image = forms.ImageField()


class SubCatForm(forms.Form):
    error_css_class = "error"
    main_category_id = forms.ModelChoiceField(queryset=MainCategory.objects.all())
    category_name = forms.CharField(max_length=254, required=True, widget = forms.TextInput(attrs={"class":"form-control input-lg","placeholder":"category name"}))
    description = forms.CharField(max_length=254, widget=forms.TextInput(attrs={"class":"form-control input-lg","placeholder":"description"}))
    image = forms.ImageField()


class ChildCategoryForm(forms.Form):
    error_css_class = "error"
    main_category_id = forms.ModelChoiceField(queryset=MainCategory.objects.all())
    sub_category_id = forms.ModelChoiceField(queryset =SubCategory.objects.all())
    category_name = forms.CharField(max_length=100,required=True, widget = forms.TextInput(attrs={"class":"form-control","placeholder":"category_name"}))
    description = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"description"}))
    image= forms.ImageField()

    

class PostsForm(forms.Form):
    error_css_class = "error"
    title=forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': "form-control input-lg", "placeholder":'title'}))
    description = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class': "form-control input-lg","placeholder":'description'}))
    image = forms.ImageField()



