
from django.urls import path 
from . import views
app_name = 'common'

urlpatterns = [
   path('home',views.index, name = 'home'),
   path('customer/',views.customer_reg , name = 'customer_registration'),
   path('seller/',views.seller_reg , name = 'seller_registration'),
   path('seller-log/',views.seller_log, name = 'seller_login'),
   path('customer-log/',views.customer_log, name = 'customer_login'),

]