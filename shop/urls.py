from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.view_cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('register/', views.register, name='register'),
    path('invoice/<int:order_id>/', views.download_invoice, name='download_invoice'),
    path('supplier/dashboard/', views.supplier_dashboard, name='supplier_dashboard'),
    path('supplier/add_product/', views.add_product, name='add_product'),
    path('albums/', views.album_list, name='album_list'),
    path('add-album/', views.add_album, name='add_album'),
    path('search/', views.search_albums, name='search_albums'),
]