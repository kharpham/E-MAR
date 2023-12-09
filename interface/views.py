from django.shortcuts import render
from datetime import datetime, timedelta
from pytz import timezone
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    products = Product.objects.all()
    now = datetime.now(timezone('Asia/Ho_Chi_Minh'))
    target_datetime = datetime(2023, 12, 5, 20, 0, 0, tzinfo=timezone('Asia/Ho_Chi_Minh'))
    if target_datetime > now:
        return render(request, "interface/countdown.html")
    else:
        return render(request,  "interface/commerce.html", {
            "products": products,
        })
def blog(request):
    blogs = Blog.objects.all()
    return render(request, "interface/blog.html", {
      "blogs": blogs,
    })

def countdown(request):
    return render(request, "interface/countdown.html")

def blog_view(request, blog_id):
    try: 
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return HttpResponse("Page not found")
    return render(request, "interface/blog_view.html", {
        "blog": blog,
    })

def product_view(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return HttpResponse("Page not found")
    return render(request, "interface/product_view.html", {
        "product": product,
    })

def about_us(request):
    return render(request, "interface/about_us.html")
