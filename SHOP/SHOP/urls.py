"""SHOP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import include, path #includes merchandise app
from .views import * #index, contact, cart, user_sign_up, user_log_in, user_log_out


urlpatterns = [
    path('', index, name='index'),
    path('locations', location, name="location"),
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact'),
    path('user_sign_up/', user_sign_up, name='user_sign_up'),
    path('user_log_in/', user_log_in, name='user_log_in'),
    path('user_log_out/', user_log_out, name='user_log_out'),
    path('merchandise/', include('merchandise.urls', namespace='merchandise')),
    path('look_up/', include('look_up.urls', namespace='look_up')),
    path('cart/', include('cart.urls', namespace='cart')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
