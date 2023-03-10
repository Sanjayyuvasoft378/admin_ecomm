from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','discount_price',
                'description','category','product_image']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality',
                'city','state','zipcode']
     
@admin.register(UserRegistration)
class UserRegistration(admin.ModelAdmin):
    list_display = ['id','username','email','password1','password2']

@admin.register(ContactUs)
class ConatctAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','subject','your_message']

@admin.register(AddToCartModel)
class AddToCart(admin.ModelAdmin):
    list_display = ['product_id','qty']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','product_title','qty','price']

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['product_id','qty']

@admin.register(ProductReviewModel)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['id','review','reviewer']
    
@admin.register(ProductCommentModel)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ['id','comment','commentator']