from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Product, Order, OrderItem
from django.db import transaction
from django.core.paginator import Paginator
from .models import Product
from .models import Cart, CartItem
from django.contrib import messages
from .models import Album
from .forms import AlbumForm, SearchForm
from django.db.models import Q
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})

@login_required

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    with transaction.atomic():
        order, created = Order.objects.get_or_create(customer=request.user.customer, status='Pending')
        order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
        order_item.quantity += 1
        order_item.save()
    return redirect('cart')

@login_required
def checkout(request):
    # Handle checkout process here
    return render(request, 'shop/checkout.html')

@login_required
def download_invoice(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer=request.user.customer)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{order_id}.pdf"'
    
    p = canvas.Canvas(response)
    
    p.drawString(100, 750, f"Invoice for Order {order_id}")
    p.drawString(100, 730, f"Customer: {order.customer.user.username}")
    p.drawString(100, 710, f"Total Amount: ${order.total}")
    
    # Add more details as needed
    
    p.showPage()
    p.save()
    
    return response

@login_required
def supplier_dashboard(request):
    return render(request, 'shop/supplier_dashboard.html')

@login_required
def add_product(request):
    # Your logic here
    return render(request, 'shop/add_product.html')

def product_list(request):
    products = Product.objects.all().order_by('-id')
    paginator = Paginator(products, 12)  # Show 12 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop/product_list.html', {'page_obj': page_obj})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.cartitem_set.all()
    total = sum(item.product.price * item.quantity for item in items)
    return render(request, 'shop/cart.html', {'items': items, 'total': total})

def homepage_view(request):
    return render(request, 'homepage.html')

def homepage(request):
    return render(request, 'shop/homepage.html')

def homepage(request):
    albums = Album.objects.all()
    return render(request, 'shop/homepage.html', {'albums': albums})

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'shop/add_album.html', {'form': form})

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'shop/album_list.html', {'albums': albums})

def search_albums(request):
    form = SearchForm(request.GET)
    albums = []
    query = ''
    if form.is_valid():
        query = form.cleaned_data['query']
        albums = Album.objects.filter(
            Q(title__icontains=query) |
            Q(artist__icontains=query) |
            Q(keywords__icontains=query)
        )
    
    context = {
        'form': form,
        'albums': albums,
        'query': query,
    }
    return render(request, 'shop/search_results.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})