from django.shortcuts import render,redirect
from rest_framework.generics import ListAPIView
from rest_framework import status
from PIL import Image
from io import BytesIO
import base64
from .models import *
from rest_framework.response import Response
import random
from .serializers import *
from Ecomm_app.serializers import * #UserRegistrationSerializer, ProductReviewSerializer, ProductCommentSerializer,ChangePasswordSerializer,ContactUsSerializer
from Ecomm_app.models import *    #UserRegistration,ProductReviewModel,ProductCommentModel,ContactUs
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import FileUploadParser,FormParser, MultiPartParser
from . forms import Addproductform,MainCatForm, SubCatForm, PostsForm

def editprofile(request):
    return render(request, 'Account/edit_profile.html')

def changepassword(request):
    return render(request, 'Account/change_password.html')

def allproductlist(request):
    return render(request, 'Product/all_product.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html')

def login(request):
    return render(request,'Account/login.html')

def allorder(request):
    return render(request,'Order/allorder.html')

def pendingorder(request):
    return render(request,'Order/order_pending.html')

def processingorder(request):
    return render(request,'Order/processing_order.html')

def completedorder(request):
    return render(request,'Order/completed_order.html')

def deciendorder(request):
    return render(request,'Order/deciend_order.html')

def home(request):
    return render(request,'Product/add_product.html')

def deactivateproduct(request):
    return render(request,'Product/deactivate_product_list.html')

def addproduct(request):
    return render(request,'Product/add_product.html')

############

def productreviews(request):
    return render(request,'Product/product_reviews.html')

def productcomments(request):
    return render(request,'Product/product_comments.html')

def productreports(request):
    return render(request,'Product/product_reports.html')

def coupons(request):
    return render(request,'coupons/coupons.html')

# Convert Image to Base64
def image_to_base64(image):
    buff = BytesIO()
    image.save(buff, format="PNG")
    img_str = base64.b64encode(buff.getvalue())
    img_str = img_str.decode("utf-8")  # convert to str and cut b'' chars
    return img_str

class FileUploadView(ListAPIView):
    parser_class = (FileUploadParser,FormParser, MultiPartParser)
    serializer_class = FileSerializer
    
    def get(self, request):
        data = File.objects.all()
        file_serializer = FileSerializer(data, many=True)
        obj = file_serializer.data
        # return render(request, 'image_form.html',{"obj":obj})
        return JsonResponse(file_serializer.data, safe=False,status=200)

    def post(self, request, *args, **kwargs):
        form = Addproductform(request.POST, request.FILES)
        if form.is_valid():
            file=form.cleaned_data['file']
            item = File(file=file)      
            serializer = FileSerializer(data=form.cleaned_data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )   
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return JsonResponse({"msg":"Invalid data"},safe=False)

    def put(self, request):
        imageid = self.request.POST.get('id')
        f_obj = File.objects.filter(id=imageid) #File is my model name
        file_serializer = FileSerializer(f_obj, data=request.data)
        print(file_serializer)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(
                file_serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                file_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request):
        imageid = request.POST.get('id')
        f_obj = File.objects.filter(id=imageid) #File is my model name
        import pdb; pdb.set_trace()
        if f_obj.exists():
            f_obj.delete()
            return Response(
                {
                    "Status": True,
                    "Message": "image deleted"
                }
            )
        else:
            return JsonResponse({"msg":"not delete"},safe=False)

class CustomerListAPI(APIView):
    def get(self, request):
        customer = UserRegistration.objects.all()
        a = customer.count()
        Serializer = UserRegistrationSerializer(customer,many=True)
        data = Serializer.data
        return render(request, 'customer_list.html',{"data":data})
        # return JsonResponse(Serializer.data, safe=False)

# Create your views here.
class MainCategoryAPI(APIView):
    def get(self, request):
        item = MainCategory.objects.all()
        Serializer = MaincategorySerializer(item, many=True)
        data=Serializer.data
        # return JsonResponse(Serializer.data,safe=False)
        return render(request, 'Categories/Main-Category/main_category_list.html',{"data":data})
        # return redirect('/api/v1/main-category',{"data":data})

    def post(self, request):
        try:
            form = MainCatForm(request.POST, request.FILES)
            if form.is_valid():
                category_name = request.POST.get("category_name")
                description = request.POST.get("description")
                cate_image=form.cleaned_data['cate_image']
                item = MainCategory(cate_image=cate_image, description=description,category_name=category_name)      
                Serializer = MaincategorySerializer(data=form.cleaned_data)

                if MainCategory.objects.filter(**request.data).exists():
                    raise serializers.ValidationError("category already exist")

                if Serializer.is_valid():
                    Serializer.save()
                    return render(request, 'Categories/Main-Category/main_category_list.html')
                    # return JsonResponse({"msg":"data added successfully"},safe=False,status=200)
                else:
                    return JsonResponse({"msg":"invalid data "},safe=False,status=400)
            else:
                return JsonResponse({"msg":"invalid data "},safe=False,status=400)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False, status=500)
    
    def delete(self, request,id):
        try:
            id= int(id)
            item = MainCategory.objects.filter(id=id)
            item.delete()
            import pdb; pdb.set_trace()
            return JsonResponse({"msg":"deleted"},safe=False,status=200)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False,status=500)

    def put(self, request,id):
        item = MainCategory.objects.get(id=id)
        Serializer = MaincategorySerializer(instance=item, data=request.data)
        if MainCategory.objects.filter(**request.data).exists():
            raise serializers.ValidationError("category of this name already exists")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"category updated"},safe=False)
        else:
            return JsonResponse({"msg":"invalid form data"}, safe=False)
       
class SubCategoryAPI(APIView):
    def post(self, request):
        form = SubCatForm(request.POST, request.FILES)
        import pdb; pdb.set_trace()
        if form.is_valid():
            main_category_id = request.POST.get("main_category_id")
            category_name = request.POST.get("category_name")
            description = request.POST.get("description")
            image=form.cleaned_data['image']
            item = SubCategory(main_category_id=main_category_id, image=image, description=description,category_name=category_name)      
            Serializer = SubcategorySerializer(data=item)

            if SubCategory.objects.filter(**request.data).exists():
                raise serializers.ValidationError("category already exist")
            
            if Serializer.is_valid():
                Serializer.save()
                return JsonResponse({"msg":"data added successfully"},safe=False)
            else:
                return JsonResponse({"msg":"invalid data "},safe=False)
        else:
            return JsonResponse({"msg":"invalid data "},safe=False,status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        item = SubCategory.objects.all()
        Serializer = SubcategorySerializer(item, many=True)
        data = Serializer.data
        return render(request,'Categories/Sub-Category/sub_category_list.html',{"data":data})
        # return JsonResponse(Serializer.data,safe=False)
    
    def delete(self, request):
        id = int(request.GET.get('id'))
        item = SubCategory.objects.filter(id=id)
        item.delete()
        return JsonResponse({"msg":"delete"},safe=False)

    def put(self, request,pk):
        item = SubCategory.objects.get(pk=pk)
        Serializer = SubcategorySerializer(instance=item, data=request.data)
        if SubCategory.objects.filter(**request.data).exists():
            raise serializers.ValidationError("category of this name already exists")

        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"category updated"},safe=False)
        else:
            return JsonResponse({"msg":"invalid form data"}, safe=False)
        
class ChildCategoryAPI(APIView):
    def post(self, request):
         form = ChildCategoryForm(request.POST, request.FILES)
         if form.is_valid():
            main_category_id = request.POST.get('main_category_id')
            sub_category_id = request.POST.get('sub_category_id')
            category_name = request.POST.get('category_name')
            description = request.POST.get('description')
            image = form.cleaned_data['image']
            serializer = ChildCategory(main_category_id=main_category_id,sub_category_id=sub_category_id,category_name=category_name,description=description,image=image)
            Serializer = ChildcategorySerializer(data=serializer)
            if ChildCategory.objects.filter(**request.data).exists():
                raise serializers.ValidationError("category already exist")
            if Serializer.is_valid():
                Serializer.save()
                return JsonResponse({"msg":"data added successfully"},safe=False)
            else:
                return JsonResponse({"msg":"invalid data "},safe=False)
    def get(self, request):
        item = ChildCategory.objects.all()
        Serializer = ChildcategorySerializer(item, many=True)
        data = Serializer.data
        return render(request,'Categories/Child-Category/child_category_list.html',{"data":data})
        # return JsonResponse(Serializer.data,safe=False)
    
    def delete(self, request, pk):
        item = ChildCategory.objects.filter(id=pk)
        item.delete()
        return JsonResponse({"msg":"delete"},safe=False)

    def put(self, request,pk):
        item = ChildCategory.objects.get(pk=pk)
        Serializer = ChildcategorySerializer(instance=item, data=request.data)
        if ChildCategory.objects.filter(**request.data).exists():
            raise serializers.ValidationError("category of this name already exists")

        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"category updated"},safe=False)
        else:
            return JsonResponse({"msg":"invalid form data"}, safe=False)
                
class ProductAPI(APIView):
    def post(self, request):
        Serializer = ProductSerializer(data=request.data)
        if Product.objects.filter(**request.data).exists():
            raise serializers.ValidationError("category already exist")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"data added successfully"},safe=False)
        else:
            return JsonResponse({"msg":"invalid data "},safe=False,status=400)
        
    def get(self, request):
        item = Product.objects.all()
        Serializer = ProductSerializer(item, many=True)
        data = Serializer.data
        # return render(request,'Product/all_product.html',{"data":data})
        return JsonResponse(Serializer.data, safe=False)
    
    def delete(self, request, pk):
        item = Product.objects.filter(id=pk)
        item.delete()
        return JsonResponse({"msg":"delete"},safe=False)

    def put(self, request,pk):
        item = Product.objects.get(pk=pk)
        Serializer = ProductSerializer(instance=item, data=request.data)
        if Product.objects.filter(**request.data).exists():
            raise serializers.ValidationError("category of this name already exists")

        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"category updated"},safe=False)
        else:
            return JsonResponse({"msg":"invalid form data"}, safe=False)

class ProductlistAPI(APIView):
    def get(self, request):
        item = Product.objects.all()
        Serializer = ProductSerializer(item, many=True)
        data = Serializer.data
        return render(request, 'Product/all_product.html',{"get_data":data})
        # return JsonResponse(Serializer.data,safe=False)
    
class ProductDeactivateAPI(APIView):
    def get(self, request):
        try:     
            if status==0:
                item = Product.objects.all()
                Serializer = ProductSerializer(item,many=True)
                return JsonResponse(Serializer.data,safe=False,status=200)
            elif status==1:
                item = Product.objects.filter(status="deactivated")
                Serializer = ProductSerializer(item)
                return JsonResponse(Serializer.data,safe=False,status=200)
            elif status==2:
                item = Product.objects.filter(status="activated")
                Serializer = ProductSerializer(item)
                return JsonResponse(Serializer.data,safe=False,status=200)
            else:
                return JsonResponse(Serializer.error,safe=False,status=400)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False,status=500)
        
class CouponsAPI(APIView):
    def post(self, request):
        Serializer = CouponsSerializer(data=request.data)
        if Coupons.objects.filter(**request.data).exists():
            raise serializers.ValidationError("category already exist")
        if Serializer.is_valid():
            Serializer.save()
            # return redirect('/api/v1/coupons/')
            return JsonResponse({"msg":"data added successfully"},safe=False)
        else:
            return JsonResponse({"msg":"invalid data "},safe=False)
        
    def get(self, request):
        item = Coupons.objects.all()
        Serializer = CouponsSerializer(item, many=True)
        data= Serializer.data
        return render(request,'coupons/coupons.html',{"data":data})
        return JsonResponse(Serializer.data, safe=False)
    
    def delete(self, request, pk):
        item = Coupons.objects.filter(id=pk)
        item.delete()
        return render(request, "coupons/coupons.html")
        # return JsonResponse({"msg":"delete"},safe=False)

    def put(self, request,pk):
        item = Coupons.objects.get(pk=pk)
        Serializer = CouponsSerializer(instance=item, data=request.data)
        if Coupons.objects.filter(**request.data).exists():
            raise serializers.ValidationError("category of this name already exists")
        if Serializer.is_valid():
            Serializer.save()
            return render(request, "coupons/coupons.html")
            # return JsonResponse({"msg":"category updated"},safe=False)
        else:
            return JsonResponse({"msg":"invalid form data"}, safe=False)

class StaffAPI(APIView):
    def post(self, request):
        try:
            Serializer = StaffSerializer(data=request.data)
            if Staff.objects.filter(**request.data).exists():
                raise serializers.ValidationError("already exists")
            if Serializer.is_valid(raise_exception=True):
                Serializer.save() 
                return redirect('/api/v1/staff/')
                # return JsonResponse({"msg":"data added successfully"},safe=False,status=200)
            else:
                return render(request, "staff_list.html")
                # return JsonResponse({"msg":"Invalid input"},safe=False)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False,status=500)
        
    def get(self, request):
        try:
            item = Staff.objects.all()
            Serializer = StaffSerializer(item, many=True)        
            data = Serializer.data
            return render(request, 'staff_list.html',{"data":data})
            # return JsonResponse(Serializer.data,safe=False)
        except Exception as e:
            return JsonResponse({"msg":"Internal server eror {}".format(e)},safe=False, status=500)

    def delete(self, request, id):
        item = Staff.objects.filter(id=id)
        item.delete()
        return JsonResponse({"msg":"data deleted successfully"},safe=False, status=200)

    def put(self, request, pk):
        item = Staff.objects.get(pk=pk)
        Serializer = StaffSerializer(instance=item, data=request.data)
        if Staff.objects.filter(**request.data).exists():
            raise serializers.ValidationError("already exist")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"data updated successfully"},safe=False,status=200)
        else:
            return JsonResponse({"msg":"Invalid data"},safe=False,status=500)

class PostsAPI(APIView):
    def post(self, request):
        try:
            form = PostsForm(request.POST, request.FILES)
            if form.is_valid():
                title = request.POST.get("title")
                description = request.POST.get("description")
                image=form.cleaned_data['image']
                item = Posts(image=image, description=description,title=title)      
                Serializer = PostsSerializer(data=form.cleaned_data)
                if Posts.objects.filter(**request.data).exists():
                    raise serializers.ValidationError("already exists")
                if Serializer.is_valid(raise_exception=True):
                    Serializer.save() 
                    # return JsonResponse({"msg":"data added successfully"},safe=False,status=200)
                    return render(request,'Blog/posts_list.html')
                else:
                    return JsonResponse({"msg":"Invalid input"},safe=False)
            else:
                return JsonResponse({"msg":"Invalid form data"},safe=False,status=400)
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False,status=500)
        
    def get(self, request):
        try:
            item = Posts.objects.all()
            Serializer = PostsSerializer(item, many=True)        
            data = Serializer.data
            a = data.count
            return render(request,'Blog/posts_list.html',{"data":data,"a":a})
            # return JsonResponse(Serializer.data,safe=False)
        except Exception as e:
            return JsonResponse({"msg":"Internal server eror {}".format(e)},safe=False, status=500)

    def delete(self, request, pk):
        item = Posts.objects.filter(id=pk)
        item.delete()
        return JsonResponse({"msg":"data deleted successfully"},safe=False, status=200)

    def put(self, request, pk):
        item = Posts.objects.get(pk=pk)
        Serializer = PostsSerializer(instance=item, data=request.data)
        if Posts.objects.filter(**request.data).exists():
            raise serializers.ValidationError("already exist")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"data updated successfully"},safe=False,status=200)
        else:
            return JsonResponse({"msg":"Invalid data"},safe=False,status=500)
         
         
class ProductReportsListAPI(APIView):
    def get(self, request):
        item = ProductCommentModel.objects.all()
        Serializer = ProductCommentSerializer(item, many=True)
        data = Serializer.data
        return render(request, 'Product/product_report.html',{"data":data})


class ProductReviewListAPI(APIView):
    def get(self, request):
        item = ProductReviewModel.objects.all()
        Serializer = ProductReviewSerializer(item, many=True)
        data = Serializer.data
        # return JsonResponse(Serializer.data,safe=False,status=200)
        return render(request, 'Product/product_reviews.html',{"data":data})
    
class ProductCommentListAPI(APIView):
    def get(self, request):
        item = ProductCommentModel.objects.all()
        Serializer = ProductCommentSerializer(item, many=True)
        data = Serializer.data
        # return JsonResponse(Serializer.data,safe=False,status=200)
        return render(request, 'Product/product_comments.html',{"data":data})

class ChangePasswordAPI(APIView):
    def post(self, request):
        Serializer = ChangePasswordSerializer(data=request.data, context={"user":request.user})
        if Serializer.is_valid(raise_exception=True):
            Serializer.save()
            return redirect('home/')
        else:
            return render(request,'app/changepasword.html')
        
class DeactivateProductAPI(APIView):
    def get(self, request):
        try:
            item = Product.objects.find(status=False)
            Serializer = ProductSerializer(item)
            data = Serializer.data
            return render(request,'Product/deactivate_product.html',{"data":data})
        except Exception as e:
            return JsonResponse({"msg":"Internal server error {}".format(e)},safe=False,status=500)
        
class PopularProductAPI(APIView):
    def get(self, request):
        item = Product.objects.all()
        Serializer = ProductSerializer(item, many=True)
        data = Serializer.data
        return render(request, 'Product/popular_product.html',{"data":data})
        # return JsonResponse(data,safe=False,status=200)
    
    
class SliderAPI(APIView):
    def post(self, request):
        Serializer = SliderSerializer(data = request.data)
        if Slider.objects.filter(**request.data).exists():
            raise serializers.ValidationError("heading already exists")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"data added successfully"},safe=False,status=200)
        else:
            return JsonResponse({"msg":"Invlid form data"},safe=False,status=400)

    def get(self, request):
        item = Slider.objects.all()
        Serializer = SliderSerializer(item, many=True)
        data = Serializer.data
        return render(request,'slider.html',{"data":data})

    def delete(self, request,pk):
        item = Slider.objects.filter(id=pk)
        item.delete()
        return JsonResponse({"msg":"data deleted "},safe=False,status=200)

    def put(self, request, pk):
        item = Slider.objects.get(id=pk)
        Serializer = SliderSerializer(data = request.data, instance=item)
        if Slider.objects.filter(**request.data).exists():
            raise serializers.ValidationError("heading already exists")
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"msg":"data added successfully"},safe=False,status=200)
        else:
            return JsonResponse({"msg":"Invlid form data"},safe=False,status=400)


class ContactUsListAPI(APIView):
    def get(self, request):
        item = ContactUs.objects.all()
        Serializer = ContactUsSerializer(item,many=True)
        data = Serializer.data
        return render(request, 'contactlist.html',{"data":data})
        


        