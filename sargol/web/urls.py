from django.urls import path
from .views import home_page,ProductDetail,kham

app_name = 'web'

urlpatterns = [
    path('',home_page,name="home_page"),
    path('kham',kham, name='kham'),
    path('product/<slug:slug>',ProductDetail, name='ProductDetail')
]
