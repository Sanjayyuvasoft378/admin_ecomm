from django.contrib import admin  
from django.urls import path  
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  
# from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('api/token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    # path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
    path('admin/', admin.site.urls),
    path('',include('admin_app.urls')),
    path('',include('Ecomm_app.urls')),
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
