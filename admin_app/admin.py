from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['file']

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['id','title','image','description']

@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name','description','cate_image']
    
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','main_category_id','category_name','description','image']
    
@admin.register(ChildCategory)
class ChildCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','main_category_id','sub_category_id','category_name','description','image']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','main_category_id','sub_category_id','product_name','price','qty','description','image']

@admin.register(Coupons)
class CouponsAdmin(admin.ModelAdmin):
    list_display = ['id','coupon_type','amount','used']
    
    
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','mobile_no','gender']

