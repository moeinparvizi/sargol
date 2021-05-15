from django.shortcuts import render, get_list_or_404
from .models import products,Articles,Category,Banners
from productgallery.models import gallery

# Create your views here.
def home_page(request):
    context = {
        "products":products.objects.filter(status='p'),
        "articles":Articles.objects.filter(status='p'),
        "categoryes":Category.objects.filter(status=True),
        "banners":Banners.objects.get()

    }
    return render(request,"index.html",context)

def ProductDetail(request,slug):
    context = {
        "product":products.objects.get(slug=slug),
        "products":products.objects.filter(status='p')[:4],
        "categoryes":Category.objects.filter(status=True),
        "banners":Banners.objects.get(),
        "images":gallery.objects.all()
    }
    return render(request,"ProductDetail.html",context)

def kham(request):
    context={
        "banners":Banners.objects.get()
    }
    return render(request,"mahsulate-kham.html",context)

