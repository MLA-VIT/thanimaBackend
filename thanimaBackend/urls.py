from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls'), name='socialaccount_signup'),
    path('api/auth/',include('userauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
