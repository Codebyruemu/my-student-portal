"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

# setting the admin properties below modify the look of the admin page
admin.site.site_header = 'STORE ADMIN'
admin.site.site_title = 'Online Store'
admin.site.index_title = 'STORE ADMIN'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myportfolioapp.urls')),
    path('items',include('Items.urls')),
    path('registration', include('registration.urls'))   
] 

# ✅ Add BOTH static and media when DEBUG=True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
