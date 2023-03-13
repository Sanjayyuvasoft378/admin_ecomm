from django.db import models

class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file

class MainCategory(models.Model):
    category_name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    cate_image = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.category_name
    
class Posts(models.Model):
    image = models.FileField(blank=False, null=False)
    title = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    def __str__(self):
        return self.title

class SubCategory(models.Model):
    main_category_id = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.category_name

class ChildCategory(models.Model):
    main_category_id = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    sub_category_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    main_category_id = models.ForeignKey(MainCategory,on_delete=models.CASCADE)
    sub_category_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to='product/')
    description = models.TextField()

class Coupons(models.Model):
    coupon_type = models.CharField(max_length=20)
    amount = models.IntegerField()
    used = models.CharField(max_length=20)

class Staff(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    mobile_no = models.CharField(max_length=10)
    gender = models.CharField(max_length=20)

    # def __str__(self):
    #     return self.first_name

    
class Slider(models.Model):
    image = models.ImageField(upload_to='slider_image/')
    heading = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.heading
    

    