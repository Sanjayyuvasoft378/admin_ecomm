from django.urls import path
from admin_app import views
from rest_framework.urlpatterns import format_suffix_patterns

from django.contrib.auth import views as auth_view

urlpatterns = [
    
    path('api/v1/login/',views.login,name='login'),
    
    path('api/v1/edit-profile/',views.editprofile,name='edit-profile'),
    path('api/v1/change-password/',views.changepassword,name='change-password'),
    path('api/v1/change-admin-password/',views.ChangePasswordAPI.as_view(),name='change-admin-password'),
    
    path('api/v1/home/',views.home,name='home'),
    path('api/v1/allproductlist/',views.allproductlist,name='allproductlist'),
    path('api/v1/dashboard/',views.dashboard,name='dashboard'),
    
    
    path('api/v1/allorder/',views.allorder,name='allorder'),
    path('api/v1/pending-order/',views.pendingorder,name='pending-order'),
    path('api/v1/processing-order/',views.processingorder,name='processing-order'),
    path('api/v1/completed-order/',views.completedorder,name='completed-order'),
    path('api/v1/decliend-order/',views.deciendorder,name='decliend-order'),
    
    path('image-request/', views.FileUploadView.as_view(), name = "image-request"),
    
    path('api/v1/deactivate-product/',views.deactivateproduct,name='deactivate-product'),
    path('api/v1/add-product/',views.addproduct,name='add-product'),
    
    path('api/v1/product-reviews/',views.productreviews,name='product-reviews'),
    path('api/v1/product-comments/',views.productcomments,name='product-comments'),
    path('api/v1/product-reports/',views.productreports,name='product-reports'),
    path('api/v1/coupons1/',views.coupons,name='coupons1'),
    
    path('api/v1/main-category/',views.MainCategoryAPI.as_view(),name='main-category'),
    path('api/v1/main-category/<int:pk>',views.MainCategoryAPI.as_view(),name='main-category-detail'),
    
    path('api/v1/sub-category/',views.SubCategoryAPI.as_view(),name='sub-category'),
    path('api/v1/sub-category/<int:pk>',views.SubCategoryAPI.as_view(),name='sub-category'),
    
    path('api/v1/child-category/',views.ChildCategoryAPI.as_view(),name='child-category'),
    path('api/v1/child-category/<int:pk>',views.ChildCategoryAPI.as_view(),name='child-category'),
    
    path('api/v1/product/',views.ProductAPI.as_view(),name='product'),
    path('api/v1/product/<int:pk>',views.ProductAPI.as_view(),name='product'),
    
    path('api/v1/coupons/',views.CouponsAPI.as_view(),name='coupons'),
    path('api/v1/coupons/<int:pk>',views.CouponsAPI.as_view(),name='coupons'),
    
    path('api/v1/product-list/',views.ProductlistAPI.as_view(),name='product-list'),
    
    path('api/v1/customer-list/',views.CustomerListAPI.as_view(),name='customer-list'),
    path('api/v1/staff/',views.StaffAPI.as_view(),name='staff'),
    path('api/v1/staff/<int:id>',views.StaffAPI.as_view(),name='staff'),
    
    path('api/v1/posts/',views.PostsAPI.as_view(),name='posts'),
    path('api/v1/posts/<int:pk>',views.PostsAPI.as_view(),name='posts'),
    
    path('api/v1/product-review-list/',views.ProductReviewListAPI.as_view(),name='product-review-list'),
    path('api/v1/product-comment-list/',views.ProductCommentListAPI.as_view(),name='product-comment-list'),

    path('api/v1/deactivate-product/',views.DeactivateProductAPI.as_view(),name='deactivate-product'),
    path('api/v1/popular-product/',views.PopularProductAPI.as_view(),name='popular-product'),
    
    path('api/v1/slider/',views.SliderAPI.as_view(),name='slider'),
    path('api/v1/slider/<int:pk>',views.SliderAPI.as_view(),name='slider'),
    
    path('contact-us-list/',views.ContactUsListAPI.as_view(),name='contact-us-list'),
]
urlpatterns = format_suffix_patterns(urlpatterns)