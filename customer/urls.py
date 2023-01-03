from django.urls import path 
from . import views
app_name = 'customer'

urlpatterns = [
   path('customer_home',views.index, name = 'customer_home'),
   path('product_details/',views.product_details, name = 'product_details'),
   path('change_password/',views.change_password, name = 'change_password'),
   path('my_cart/',views.cart, name = 'cart'),
   path('my_orders/',views.order, name = 'orders'),
   
]