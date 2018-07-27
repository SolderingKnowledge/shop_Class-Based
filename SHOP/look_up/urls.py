from django.urls import path
from .views import (
    LookUpMerchandiseList
    )

app_name = 'look_up'
urlpatterns = [

    path('', LookUpMerchandiseList.as_view(), name='query'),
    
]