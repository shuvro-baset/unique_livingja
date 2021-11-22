from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, get_query, get_or_create_customer, send_contact_email
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils import timezone
from django.contrib import messages


def home(request):
    # todo: product start (FEATRED PRODUCTS)
    products = Product.objects.filter(is_featured=True).order_by('-id')
    # todo: product end

    # todo: sliders start
    first_slider = HomeSlider.objects.all()[0]
    sliders = HomeSlider.objects.all()[1:]
    # todo: sliders end

    return render(request, 'home.html', {'products': products, 'sliders': sliders, 'first_slider': first_slider, })


def bathroom(request):
    products = Product.objects.filter(main_category__name='bathroom').order_by('-id')
    # print(products.distinct('sub_category__name').order_by('-id')) # todo: get unique sub_catagory, will use this query for prosgresql DB
    sub_categories = [category.sub_category.name for category in products]

    # todo: pagination start
    paginator = Paginator(products, 1)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    # todo: pagination end
    context = {
        'products': products,
        # 'sub_categories': products,
        "page_obj": page_obj
    }
    return render(request, 'bathroom.html', context)


def sub_category(request, main_category, subcategory_name):
    products = Product.objects.filter(main_category__name=main_category, sub_category__name=subcategory_name).order_by(
        '-id').all()

    # todo: pagination start
    paginator = Paginator(products, 1)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    # todo: pagination end

    context = {
        'products': products,
        # 'sub_categories': sub_categories,
        "page_obj": page_obj,
        "main_category": main_category,
        "subcategory_name": subcategory_name,
    }
    return render(request, 'sub_category.html', context)


def add_category(request, main_category, addcategory_name):
    products = Product.objects.filter(main_category__name=main_category, add_category__name=addcategory_name).order_by(
        '-id').all()
    # todo: pagination start
    paginator = Paginator(products, 1)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    # todo: pagination end

    context = {
        'products': products,
        # 'sub_categories': sub_categories,
        "page_obj": page_obj,
        "main_category": main_category,
        "addcategory_name": addcategory_name,
    }
    return render(request, 'add_category.html', context)


def add_sup_category(request, main_category, addcategory_name, supcategory_name):
    products = Product.objects.filter(main_category__name=main_category, add_category__name=addcategory_name,
                                      sup_category__name=supcategory_name).order_by('-id').all()
    # todo: pagination start
    paginator = Paginator(products, 1)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    # todo: pagination end

    context = {
        'products': products,
        # 'sub_categories': sub_categories,
        "page_obj": page_obj,
        "supcategory_name": supcategory_name,
    }
    return render(request, 'add_sup_category.html', context)


def add_sup_brand(request, main_category, addcategory_name, brand_name):
    products = Product.objects.filter(main_category__name=main_category, add_category__name=addcategory_name,
                                      brand=brand_name).order_by('-id')
    print(products.count())
    # todo: pagination start
    paginator = Paginator(products, 1)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    # todo: pagination end
    context = {
        'products': products,
        'brand_name': brand_name,
        'main_category': main_category,
        # 'sub_categories': products,
        "page_obj": page_obj
    }
    return render(request, 'brands.html', context)


def kitchen(request):
    products = Product.objects.filter(main_category__name='kitchen').order_by('-id')
    # print(products.distinct('sub_category__name').order_by('-id')) # todo: get unique sub_catagory, will use this query for prosgresql DB
    sub_categories = [category.sub_category.name for category in products]

    # todo: pagination start
    paginator = Paginator(products, 1)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    # todo: pagination end
    context = {
        'products': products,
        # 'sub_categories': products,
        "page_obj": page_obj
    }
    return render(request, 'kitchen.html', context)


def commercial(request):
    products = Product.objects.filter(main_category__name='commercial').order_by('-id')
    # print(products.distinct('sub_category__name').order_by('-id')) # todo: get unique sub_catagory, will use this query for prosgresql DB
    sub_categories = [category.sub_category.name for category in products]

    # todo: pagination start
    paginator = Paginator(products, 1)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    # todo: pagination end
    context = {
        'products': products,
        # 'sub_categories': products,
        "page_obj": page_obj
    }
    return render(request, 'commercial.html', context)


def hardware(request):
    products = Product.objects.filter(main_category__name='hardware').order_by('-id')
    # print(products.distinct('sub_category__name').order_by('-id')) # todo: get unique sub_catagory, will use this query for prosgresql DB
    sub_categories = [category.sub_category.name for category in products]

    # todo: pagination start
    paginator = Paginator(products, 1)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    # todo: pagination end
    context = {
        'products': products,
        # 'sub_categories': products,
        "page_obj": page_obj
    }
    return render(request, 'hardware.html', context)


def brands(request, main_category, brand_name):
    products = Product.objects.filter(main_category__name=main_category, brand=brand_name).order_by('-id')
    # print(products.distinct('sub_category__name').order_by('-id')) # todo: get unique sub_catagory, will use this query for prosgresql DB

    # todo: pagination start
    paginator = Paginator(products, 1)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    # todo: pagination end
    context = {
        'products': products,
        'brand_name': brand_name,
        'main_category': main_category,
        # 'sub_categories': products,
        "page_obj": page_obj
    }
    return render(request, 'brands.html', context)


def brand(request, brand_name):
    products = Product.objects.filter(brand=brand_name).order_by('-id')
    # print(products.distinct('sub_category__name').order_by('-id')) # todo: get unique sub_catagory, will use this query for prosgresql DB

    # todo: pagination start
    paginator = Paginator(products, 1)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    # todo: pagination end
    context = {
        'products': products,
        'brand_name': brand_name,
        # 'sub_categories': products,
        "page_obj": page_obj
    }
    return render(request, 'brand.html', context)


def closets(request):
    products = Product.objects.filter(main_category__name='closet').order_by('-id').all()
    # todo: pagination start
    paginator = Paginator(products, 1)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    # todo: pagination end
    return render(request, 'closet.html', {"page_obj": page_obj})


def enclosure(request):
    return render(request, 'enclosure.html')


def noSearch(request):
    return render(request, 'no-search-result.html')


def search(request):
    return render(request, 'search.html')


def singleProduct(request, main_category, sku):
    product_ins = Product.objects.filter(main_category__name=main_category, sku=sku).first()
    if product_ins is not None:
        if product_ins.finishes is not None:
            if '|' in product_ins.finishes:
                finishes = product_ins.finishes.split('|')
            else:
                finishes = [product_ins.finishes]
                print(finishes)
            return render(request, 'singleProduct.html', {'product': product_ins, 'finishes': finishes})
        else:
            finishes = []
            return render(request, 'singleProduct.html', {'product': product_ins, 'finishes': finishes})
    else:
        return HttpResponse('product not found')


def search(request):
    # data = cartData(request)
    # cartItems = data["cartItems"]
    # order = data["order"]
    # items = data["items"]

    query_string = ""
    found_entries = None
    query_string = request.GET["query"]

    entry_query = get_query(
        query_string,
        ["name", "brand"],
    )
    products = Product.objects.filter(entry_query).order_by('-id').all()

    paginator = Paginator(products, 1)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "query_string": query_string,
        "products": products,
        # "cartItems": cartItems,
        "page_obj": page_obj,
        "total_result": products.count(),
    }
    if products:
        return render(request, "search.html", context)
    else:
        return render(request, "no-search-result.html")


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.POST:
        send_contact = send_contact_email(request)
        if send_contact:
            messages.error(
                request,
                "Thanks for your message. We will contact with sortly.",
            )
            return render(request, 'contact.html')
        else:
            messages.error(
                request,
                "Something wrong. please try again.",
            )
            return render(request, 'contact.html')
    return render(request, 'contact.html')
