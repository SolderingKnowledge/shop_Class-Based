from django.urls import path

from .views import (
        cart_home, 
        cart_update, 
        )
app_name = 'cart'

urlpatterns = [
    path('', cart_home, name='index'),
    path('update/', cart_update, name='update'),
]







