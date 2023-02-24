from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name','description','image']
    
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','main_category_id','category_name','description','image']
    
@admin.register(ChildCategory)
class ChildCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','main_category_id','sub_category_id','category_name','description','image']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','main_category_id','sub_category_id','product_name','price','qty','description','image']
