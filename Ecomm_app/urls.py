from django.urls import path
from Ecomm_app import views
from .views import *
from .forms import *
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('api/v1/add-to-cart-item/',views.add_to_cart_data.as_view(), name='add-to-cart-item'),
    path('api/v1/add-to-wish-item/',views.AddToWishlistAPI.as_view(), name='add-to-wish-item'),
    path('api/v1/product/',views.ProductAPI.as_view(), name='product'),
    path('api/v1/product/<int:pk>',views.ProductAPI.as_view(), name='product'),
    path('api/v1/index/', views.index),
#     path('api/v1/profile/', views.profileupdate),
    path('api/v1/about/', views.about),
    path('api/v1/contact/', views.contact),
    path('api/v1/login/', views.CustomerLoginView.as_view(), name='login'),
    # path('api/v1/registrations/',views.registration),
    path('api/v1/category/<slug:val>', views.CategoryView.as_view(), name='category'),
    path('api/v1/categorytitle/<val>', views.CategoryTitle.as_view(), name='categorytitle'),
    path('api/v1/productDetail/<int:pk>',views.ProductDetail.as_view(), name='ProductDetail'),
    # path('api/v1/userregistration/',views.RegistrationAPI.as_view(),name='userregistration'),
    # path('api/v1/userlogin/',views.LoginAPI.as_view(),name='userlogin'),
    path('api/v1/logout/', views.logout_view, name='logout'),
    path('contactus/', views.ContactusAPI.as_view(), name='contactus'),
    path('api/v1/profileupdate/<int:pk>', views.UpdateProfile.as_view(), name='profileupdate'),
    path('api/v1/productlist/', views.ProductListAPI.as_view(), name='productlist'),
#     path('api/v1/profileview/<int:pk>', views.ProfileViewAPI.as_view(), name='profileview'),
    path('api/v1/changepassword/', views.changepassword, name='changepassword'),
    path('api/v1/ChangePasswordAPI/', views.ChangePasswordAPI.as_view(), name='ChangePasswordAPI'),
    path('api/v1/OrderAPI/', views.OrderAPI.as_view(), name='OrderAPI'),
    path('api/v1/orderlist/', views.orderlistapi.as_view(), name='orderlist'),
    path('api/v1/CartList/', views.CartList.as_view(), name='CartList'),
    path('api/v1/cartdata/', views.cartdata, name='cartdata'),
    path('api/v1/searchdata/', views.filter, name='searchdata'),
    path('api/v1/wishlist/', views.WishlistAPI.as_view(), name='wishlist'),
    path('api/v1/add-to-wishlist/', views.AddToWishlistAPI.as_view(), name='add-to-wishlist'),
    path('api/v1/registrations/', views.CustomerRegistrationView.as_view(),name='registration'),
    path('api/v1/accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',
                                                        authentication_form=LoginForm), name='login'),
    path('api/v1/password-reset/',auth_view.PasswordResetView.as_view
         (template_name="app/password_reset.html",form_class=MyPasswordResetForm), name="password-reset"),
    
    path('api/v1/profile/',views.ProfileView.as_view(),name='profile'),
    path('api/v1/address/',views.address,name='address'),
    
    path('api/v1/product-review/',views.ProductReviewAPI.as_view(),name='product-review'),
    path('api/v1/product-review/<int:pk>',views.ProductReviewAPI.as_view(),name='product-review'),
    
    path('api/v1/product-comment/',views.ProductCommentAPI.as_view(),name='product-comment'),
    path('api/v1/product-comment/<int:pk>',views.ProductCommentAPI.as_view(),name='product-comment'),
    
    
    
    
    
    ###########################################
    
  
]
