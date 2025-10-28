import datetime
from django.urls import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product

from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


# @login_required(login_url='/login')
def show_main(request):

    filter_type = request.GET.get("filter", "all")
    category_filter = request.GET.get("category", None)

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    if category_filter:
        product_list = product_list.filter(category=category_filter)
    
    context = {
        'nama_aplikasi' : 'FootyBall Shop',
        'npm' : '2406401792',
        'nama': 'Sean Marcello Maheron',
        'kelas': 'PBP F',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'current_user': request.COOKIES.get('current_user', 'Anonymous'),
        'active_category': category_filter, 
        'categories': Product.CATEGORY_CHOICES,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

# @login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

# def show_json(request):
#     product_list = Product.objects.all()
#     json_data = serializers.serialize("json", product_list)
#     return HttpResponse(json_data, content_type="application/json")

def show_json(request):
    filter_type = request.GET.get("filter", "all")
    category_filter = request.GET.get("category", None)

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    if category_filter:
        product_list = product_list.filter(category=category_filter)

    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'added_at': product.added_at.isoformat() if product.added_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
       return HttpResponse(status=404)
    

# def show_json_by_id(request, product_id):
#     try:
#         product_item = Product.objects.filter(pk=product_id)
#         json_data = serializers.serialize("json", product_item)
#         return HttpResponse(json_data, content_type="application/json")
#     except Product.DoesNotExist:
#         return HttpResponse(status=404)
    
def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price' : product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'added_at': product.added_at.isoformat() if product.added_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)


# def register(request):
#     form = UserCreationForm()

#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your account has been successfully created!')
#             return redirect('main:login')
#     context = {'form':form}
#     return render(request, 'register.html', context)

@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password1 = request.POST.get("password1", "").strip()
        password2 = request.POST.get("password2", "").strip()

        if not username or not password1 or not password2:
            return JsonResponse({"error": "All fields are required."}, status=400)
        if password1 != password2:
            return JsonResponse({"error": "Passwords do not match."}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already taken."}, status=400)

        user = User.objects.create_user(username=username, password=password1)
        user.save()
        return JsonResponse({"message": "Account created successfully!"}, status=201)

    return render(request, "register.html")

# def login_user(request):
#    if request.method == 'POST':
#       form = AuthenticationForm(data=request.POST)

#       if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             response = HttpResponseRedirect(reverse("main:show_main"))
#             response.set_cookie('last_login', str(datetime.datetime.now()))
#             response.set_cookie('current_user', user.username)
#             return response

#    else:
#       form = AuthenticationForm(request)
#    context = {'form': form}
#    return render(request, 'login.html', context)

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = JsonResponse({"message": "Login successful!"})
            response.set_cookie('last_login', str(datetime.datetime.now()))
            response.set_cookie('current_user', user.username)
            return response
        else:
            return JsonResponse({"error": "Invalid username or password."}, status=401)
    return render(request, "login.html")

# def logout_user(request):
#     logout(request)
#     response = HttpResponseRedirect(reverse('main:login'))
#     response.delete_cookie('last_login')
#     response.delete_cookie('current_user')
#     return response

@require_POST
def logout_user(request):
    logout(request)
    response = JsonResponse({"message": "Logged out successfully!"})
    response.delete_cookie('last_login')
    response.delete_cookie('current_user')
    return response

# def edit_product(request, id):
#     product = get_object_or_404(Product, pk=id)
#     form = ProductForm(request.POST or None, instance=product)
#     if form.is_valid() and request.method == 'POST':
#         form.save()
#         return redirect('main:show_main')

#     context = {
#         'form': form
#     }
#     return render(request, "edit_product.html", context)

# @csrf_exempt
# def delete_product(request, id):
#     product = get_object_or_404(Product, pk=id)
#     product.delete()
#     return HttpResponseRedirect(reverse('main:show_main'))

def delete_product(request, id):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=405)

    product = get_object_or_404(Product, pk=id)

    if request.user.is_authenticated and product.user == request.user:
        product.delete()
        return JsonResponse({"message": "Product deleted successfully!"}, status=200)
    else:
        return JsonResponse({"error": "Forbidden: you do not own this product."}, status=403)

# @csrf_exempt: Menonaktifkan CSRF protection untuk request AJAX ini
# @require_POST: Memastikan hanya HTTP POST yang diterima
@login_required
@require_POST
def add_product_entry_ajax(request):
    if request.method == "POST":
        # Ambil data dari form
        name = request.POST.get("name", "").strip()
        price_str = request.POST.get("price", "").strip()
        description = request.POST.get("description", "").strip()
        category = request.POST.get("category", "merchandise").strip()
        thumbnail = request.POST.get("thumbnail", "").strip()
        is_featured = request.POST.get("is_featured") == "on"

        # Validasi input
        if not name or not price_str or not description:
            return JsonResponse({"error": "Incomplete data"}, status=400)

        try:
            price = int(price_str)
        except ValueError:
            return JsonResponse({"error": "Invalid price format"}, status=400)

        # Buat product baru
        product = Product.objects.create(
            name=name,
            price=price,
            description=description,
            category=category,
            thumbnail=thumbnail or None,
            is_featured=is_featured,
            user=request.user,
        )

        return JsonResponse({
            "message": "Product added successfully",
            "id": str(product.id),
            "name": product.name,
            "price": product.price,
        }, status=201)

    return JsonResponse({"error": "Invalid request"}, status=405)

@require_POST
def edit_product_ajax(request, id):
    p = get_object_or_404(Product, pk=id)
    if p.user_id and p.user_id != request.user.id:
        return JsonResponse({"error": "Forbidden"}, status=403)

    name = request.POST.get("name", "").strip()
    price_str = request.POST.get("price", "").strip()
    description = request.POST.get("description", "").strip()
    category = request.POST.get("category", "").strip()
    thumbnail = request.POST.get("thumbnail", "").strip()
    is_featured = request.POST.get("is_featured") in ("on", "true", "1", "True")

    if name:
        p.name = name
    if price_str:
        try:
            p.price = int(price_str)
        except ValueError:
            return JsonResponse({"error": "Invalid price format"}, status=400)
    if description:
        p.description = description
    if category:
        p.category = category
    p.thumbnail = thumbnail or None
    p.is_featured = is_featured
    p.save()

    return JsonResponse({"message": "updated", "product": _product_to_dict(p)}, status=200)

def _product_to_dict(p: Product):
    return {
        "id": str(p.id),
        "name": p.name,
        "price": p.price,
        "description": p.description,
        "category": p.category,
        "thumbnail": p.thumbnail,
        "added_at": p.added_at.isoformat() if p.added_at else None,
        "is_featured": p.is_featured,
        "user_id": p.user_id,
        "user_username": getattr(p.user, "username", None) if p.user_id else None,
    }