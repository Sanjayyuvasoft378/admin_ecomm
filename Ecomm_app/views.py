from django.shortcuts import render, redirect
from .serializers import *
# from admin_app.serializers import ProductSerializer
from django.views import View
from rest_framework import status
from .models import *
from rest_framework.views import APIView
from django.http import JsonResponse
from .forms import *
# from admin_app.models import Product
from django.contrib.auth import logout
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
    
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def index(request):
    return render(request, "app/home.html")

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")

# def profileupdate(request):
#     return render(request, 'app/profile.html')

def cartdata(request):
    return render(request, 'app/cartlist.html')
# def registration(request):
#     return render(request,'app/registration.html')

def changepassword(request):
    return render(request,'app/changepasword.html')

class CustomerRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, "app/registration.html", locals())
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congrats ! User Registration successfully")
            return redirect('/api/v1/login1/')
        else:
            messages.warning(request,"Invalid Form Data !! please enter correct data....")
        return render(request,'app/registration.html',locals())

class ChangUserPasswordAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            form = UserRegistrationForm(data)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CustomerLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "app/login.html", locals())

# class RegistrationAPI(APIView):
#     def post(self, request, *args, **kwargs):
#         try:
#             form = UserRegistrationSerializer(data=request.data)
#             if form.is_valid():
#                 form.save()
#                 return redirect('/ecomm_app/login/')
#             else:
#                 return redirect('/ecomm_app/registrations/')
#         except Exception as e:
#             return redirect('/ecomm_app/registrations/')


# class LoginAPI(APIView):
#     def post(self,request, *args, **kwargs):
#         email = request.data.get('email',None)
#         password1 = request.data.get('password1',None)
#         try:
#             login_data = UserRegistration.objects.get(email=email, password1=password1)
#             if login_data is not None:
#                 return redirect('/ecomm_app/index/')
#             else:
#                 return redirect('/ecomm_app/registrations/')
#         except Exception as e:
#             return redirect('/ecomm_app/registrations/')


def logout_view(request):
    logout(request)
    return redirect('/api/v1/login/')
  
class ContactusAPI(APIView):
    def post(self, request):
        try:
            Serializer = ContactUsSerializer(data=request.data)
            if Serializer.is_valid():
                Serializer.save()
                # messages.success(request,"message sent")
                return redirect('/api/v1/index/')
            else:
                return redirect('/contactus/')
        except Exception as e:
            return redirect('/contactus/')
        
    def get(self, request):
        try:
            events = ContactUs.objects.all()
            Serializer = ContactUsSerializer(events, many = True)
            return JsonResponse(Serializer.data,safe=False, status= status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False,
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self, request,pk):
        try:
            pk = ContactUs.objects.get(pk)
            serializer = ContactUsSerializer(pk = pk)
            serializer.delete()
            return JsonResponse({"msg":"data deleted successfully"},
                                safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False,
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html", locals())


class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(
            category=product[0].category).values('title')
        return render(request, 'app/category.html', locals())


class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', locals())

class UpdateProfile(APIView):
    def post(self, request,pk):
        try:
            get_data = UserRegistration.objects.get(pk=pk)
            Serializer = UserRegistrationSerializer(instance=get_data, data=request.data)
            if Serializer.is_valid():
                Serializer.save()
                # return redirect('/ecomm_app/index/')
                return JsonResponse({"msg":"Profile update successfully"},safe=False)
            else:
                return JsonResponse({"msg":"Profile update failed"},safe=False)
                # return redirect('/ecomm_app/index/')
        except Exception as e:
            return redirect('/ecomm_app/index/')
        
class ProductListAPI(APIView):
    def get(self, request):
        try:
            get_data = Product.objects.all()
            Serializer = ProductSerializer(get_data, many=True)
            data = Serializer.data
            # return render(request, 'app/home.html',{"data":data})
             
            return JsonResponse(Serializer.data, safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"mesg":"Internal server error {}".format(e)},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProfileViewAPI(APIView):
    def get(self, request,pk):
        try:
            profile_data = UserRegistration.objects.get(pk=pk)
            return render(request, 'app/profileview.html',locals())
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},
                                safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ChangePasswordAPI(APIView):
    def post(self, request):
        Serializer = ChangePasswordSerializer(data=request.data, context={"user":request.user})
        if Serializer.is_valid(raise_exception=True):
            Serializer.save()
            return redirect('/ecomm_app/accounts/login/')
        else:
            return render(request,'app/changepasword.html')

class OrderAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            Serializer = OrderSerializer(data=request.data)
            if Serializer.is_valid(raise_exception=True):
                Serializer.save()
                return JsonResponse({"msg":"Order created successfully"},safe=False)
            else:
                return JsonResponse({"msg":"Invalid data"},safe=False)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False)

class orderlistapi(APIView):
    def get(self, request):
        try:
            get_data = Order.objects.all()
            serializer = OrderSerializer(get_data, many = True)
            return render(request, 'app/order_list.html',locals())
            # return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False)
      
class CartList(APIView):
    def get(self, request):
        cart_data = AddToCartModel.objects.all()
        Serializer = AddToCartSerializer(cart_data, many=True)
        return render(request,'app/cartlist.html',locals())
        # return JsonResponse(Serializer.data,safe=False)

def filter(request):
    if request.method=="POST":
        title = request.POST.get('title')
        emps = Product.objects.all()
        if title:
            products = emps.filter(title__icontains = title)
            context = {
                "emps":products
            }
            return render(request, "home.html",context)
        else:
            return JsonResponse({"msg":"Invalid input"})
    else:
        return JsonResponse({"msg":"invalid method"})

class AddToWishlistAPI(APIView):
    def post(self, request):
        try:
            Serializer = WishlistSerializer(data=request.data)
            if Serializer.is_valid():
                product_id = request.POST.get('product_id')
                qty = request.POST.get('qty')
                item = Wishlist(product_id=product_id, qty=qty)
                item.save()
                return JsonResponse({"msg":"data added into wishlist successfully"})
            else:
                return JsonResponse({"msg":"invalid data"})
        except Exception as e:
            return JsonResponse({"msg":"internal server error {}".format(e)})

class WishlistAPI(APIView):
    def get(self, request):
        try:
            get_data = Wishlist.objects.all()
            Serializer = WishlistSerializer(get_data, many=True)
            # return JsonResponse(Serializer.data, safe=False,status=status.HTTP_200_OK)
            return render(request,'app/wishlist.html', locals())
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)}
                                ,safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
class Add_to_cartAPI(APIView):
    def post(self, request):
        try:
            # Data= request.data
            Serializer = AddToCartSerializer(data = request.data)
            if Serializer.is_valid():
                product_id = request.POST.get('product_id')
                qty = request.POST.get('qty')
                item = AddToCartModel(product_id = product_id, qty = qty)
                item.save()
                return JsonResponse({"msg":"data added into cart successfully"})
                # messages.success(request,"data added into cart successfully")
            else:
                return JsonResponse({"msg":"invalid data"})
                # messages.warning(request,"Invalid Data")
            # return render(request,'app/cartlist.html',locals())
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False)


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        # return JsonResponse(form.data)
        return render(request,'app/profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobileNo = form.cleaned_data['mobileNo']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user,name=name,locality=locality, mobileNo=mobileNo,city=city,
                           state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"congratulations! profile data save successfully")
        else:
            messages.warning(request,"Invalid Data")
        return render(request,'app/profile.html',locals())

def address(request):
    add = Customer.objects.filter(user = request.user)
    return render(request, 'app/address.html',locals())


class UpdateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'app/update_address.html',locals())
    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobileNo = form.cleaned_data['mobileNo']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"congratulations! profile Update successfully")
        else:
            messages.warning(request,"Invalid Data")
        return redirect("/api/v1/address/")





###########################################################
   
class ProductAPI(APIView):
    def post(self, request):
        Serializer = ProductSerializer(data = request.data)
        if Product.objects.filter(**request.data).exists():
            raise serializers.ValidationError("product already exists")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"Data added successfully"},safe=False)
        else:
            return JsonResponse({"msg":"invalid data"},safe=False)
    def get(self, request):
        item = Product.objects.all()
        Serializer = ProductSerializer(item, many= True)
        return JsonResponse(Serializer.data, safe=False)
    def delete(self, request, id):
        item = Product.objects.filter(id=id)
        item.delete()
        return JsonResponse({"msg":"data delete succesfully"},safe=False)
    def put(self, request,pk):
        item = Product.objects.get(id=pk)
        Serializer = ProductSerializer(instance=item,data=request.data)
        if Product.objects.filter(**request.data).exists():
            raise serializers.ValidationError("Product already exists")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"data added successfully"},safe=False)
        else:
            return JsonResponse({"msg":"Invalid data"},safe=False)
        
class add_to_cart_data(APIView):
    def get(self, request):
        item = AddToCartModel.objects.all()
        Serializer = AddToCartSerializer(item,many=True)
        import pdb ; pdb.set_trace()
        return JsonResponse(Serializer.data,safe=False)
    
    def post(self, request):
        try:
            form = AddToCartForm(request.POST)
            if form.is_valid():
                product_id = form.cleaned_data['product_id']
                qty = form.cleaned_data['qty']
                item = AddToCartModel(product_id=product_id, qty=qty)
                item.save()
                return JsonResponse({"msg":"data added successfully"})
            else:
                return JsonResponse({"msg":"form data invalid"})
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False)

class AddToWishlistAPI(APIView):
    def post(self, request):
        try:
            form = AddToWishlistForm(request.POST)
            if form.is_valid():
                product_id = form.cleaned_data['product_id']
                qty = form.cleaned_data['qty']
                item = Wishlist(product_id=product_id, qty=qty)
                item.save()
                return JsonResponse({"msg":"data added successfully"})
            else:
                return JsonResponse({"msg":"form data invalid"})
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False)
        
class AddToCartAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            Serializer = AddToCartSerializer(data=data)
            if Serializer.is_valid():
                Serializer.save()
                return JsonResponse({"msg":"data added into cart"},safe=False,status=200)
            else:
                return JsonResponse({"msg":"Invalid data"},safe=False,status=400)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False,status=400)

            
class ProductReviewAPI(APIView):
    def post(self, request):
        Serializer =  ProductReviewSerializer(data = request.data)       
        if ProductReviewModel.objects.filter(**request.data).exists():
            raise serializers.ValidationError("review already exists")
        if Serializer.is_valid():
            Serializer.save()
            
            return JsonResponse({"msg":"review added"},safe=False, status=200)
        else:
            return JsonResponse({"msg":"invalid data"},safe=False,status=400)
        
    def get(self, request):
        item = ProductReviewModel.objects.all()
        Serializer = ProductReviewSerializer(item, many=True)
        return JsonResponse(Serializer.data,safe=False,status=200)

    def delete(self, request, pk):
        item = ProductReviewModel.objects.filter(id=pk)
        item.delete()
        return JsonResponse({"msg":"data deleted "},safe=False,status=200)

    def put(self, request,pk):
        item = ProductReviewModel.objects.get(id=pk)
        Serializer = ProductReviewSerializer(data=request.data, instance=item)
        if ProductReviewModel.objects.filter(**request.data).exists():
            raise serializers.ValidationError("review already exits")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"data updated"},safe=False,status=200)
        else:
            return JsonResponse({"msg":"invalid data"},safe=False,status=400)
        
        
class ProductCommentAPI(APIView):
    def post(self, request):
        Serializer = ProductCommentSerializer(data= request.data)
        if ProductCommentModel.objects.filter(**request.data).exists():
            raise serializers.ValidationError("Comment already exists")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"data added "},safe=False,status=200)
        else:
            return JsonResponse({"msg":"Invalid data"},safe=False,status=400)
    def get(self, request):
        item = ProductCommentModel.objects.all()
        Serializer = ProductCommentSerializer(item, many=True)
        return JsonResponse(Serializer.data,safe=False,status=200)

    def delete(self, request, pk):
        item = ProductCommentModel.objects.filter(id=pk)
        item.delete()
        return JsonResponse({"msg":"data deleted "},safe=False,status=200)

    def put(self, request,pk):
        item = ProductCommentModel.objects.get(id=pk)
        Serializer = ProductCommentSerializer(data=request.data, instance=item)
        if ProductCommentModel.objects.filter(**request.data).exists():
            raise serializers.ValidationError("review already exits")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"data updated"},safe=False,status=200)
        else:
            return JsonResponse({"msg":"invalid data"},safe=False,status=400)
     
