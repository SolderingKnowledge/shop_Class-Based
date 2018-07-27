from django.urls import path
from .views import (
    MerchandiseList,
    MerchandiseDetailSlug, 
    MerchandiseDetail,
    )

app_name = 'merchandise'
urlpatterns = [

    path('', MerchandiseList.as_view(), name='list'),
    path('<str:slug>/', MerchandiseDetailSlug.as_view(), name='detail'),
    
]


