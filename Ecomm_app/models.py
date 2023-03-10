from django.db import models
from django.contrib.auth.models import User,BaseUserManager,AbstractBaseUser


CATEGORY_CHOICE = (
    ("CR","Curd"),
    ("ML","Milk"),
    ("LS","Lassi"),
    ("MS","Milkshake"),
    ("PN","Paneer"),
    ("GH","Ghee"),
    ("CZ","Cheese"),
    ("IC","Ice Creames"),
    ("BM","Buttermilk")
)

 


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.CharField(max_length=20)
    discount_price = models.CharField(max_length=20)
    qty = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=2)
    product_image = models.ImageField(upload_to="product",blank = True, null=True)
    def __str__(self):
        return self.title


STATE_CHOICES = (
    ("Andhra Pradesh","Andhra Pradesh",),
    ("Arunachal Pradesh ","Arunachal Pradesh "),
    ("Assam","Assam"),
    ("Bihar","Bihar"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Goa","Goa"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("Himachal Pradesh","Himachal Pradesh"),
    ("Jammu and Kashmir","Jammu and Kashmir"),
    ("Jharkhand","Jharkhand"),
    ("Karnataka","Karnataka"),
    ("Kerala","Kerala"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra"),
    ("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),
    ("Odisha","Odisha"),
    ("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),
    ("Sikkim","Sikkim"),
    ("Tamil Nadu","Tamil Nadu"),
    ("Telangana","Telangana"),
    ("Tripura","Tripura"),
    ("Uttar Pradesh","Uttar Pradesh"),
    ("Uttarakhand","Uttarakhand"),
    ("West Bengal","West Bengal"),
    ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
    ("Chandigarh","Chandigarh"),
    ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
    ("Daman and Diu","Daman and Diu"),
    ("Lakshadweep","Lakshadweep"),
    ("National Capital Territory of Delhi","National Capital Territory of Delhi"),
    ("Puducherry","Puducherry")

)

    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    locality = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    mobileNo = models.IntegerField(default=0)
    zipcode  = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=200)

    def __str__(self):
        return self.name

class UserRegistration(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    password1 = models.CharField(max_length=15)
    password2 = models.CharField(max_length=15)
    def __str__(self):
        return self.username

class ContactUs(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    subject = models.CharField(max_length=200)
    your_message = models.TextField(max_length=200)
    def __str__(self):
        return self.username + self.email
    
class AddToCartModel(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)
    qty = models.IntegerField()
    
class Order(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, default=True)
    product_title = models.CharField(max_length=20)
    qty = models.IntegerField(default=1)
    price = models.FloatField()
    def __str__(self):
        return self.product_title

class UserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2=None):
        # Creates and saves a User with the given email, name, tc and password.
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email), name=name, tc=tc,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  name, tc, password=None):
        # Creates and saves a superuser with the given email, name, tc and password.
        user = self.create_user(email, password=password, name=name, tc=tc,)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    name = models.CharField(max_length=250)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'tc']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Wishlist(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()

class ProductReviewModel(models.Model):
    review = models.CharField(max_length=100)
    # reviewer = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=200)

class ProductCommentModel(models.Model):
    comment = models.CharField(max_length=100)
    commentator = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)

    
    
