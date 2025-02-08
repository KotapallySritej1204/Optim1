from django.urls import path
from .views import *


urlpatterns = [
    path('home/',home,name = 'home'),
    path('product_list/', product_list, name='product_list'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', order_history, name='order_history'),
    path('cancel_order/<int:order_id>/', cancel_order, name='cancel_order'),
     path('user-login/', user_login, name='user_login'),
    path('vendor-login/', vendor_login, name='vendor_login'),
    path('logout/', logout_view, name='logout'),
]