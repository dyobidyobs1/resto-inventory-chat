from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),
    # INVENTORY
    path('inventory/', views.inventory, name='inventory'),
    path('createstock/', views.createstock, name='createstock'),
    path('updatestock/<str:pk>', views.updatestock, name='updatestock'),
    path('deletestock/<str:pk>', views.deletestock, name='deletestock'),
    # ORDER
    path('fooddetails/<str:pk>', views.fooddetails, name='fooddetails'),
    path('cart/', views.cart, name='cart'),
    path('summary_order/', views.summary_order, name='summary_order'),
    path('payment/', views.payment, name='payment'),
    path('orderprocess/', views.orderprocess, name='orderprocess'),
    path('deletecart/<str:pk>', views.deletecart, name='deletecart'),
    # SALES
    path('sales/', views.sales, name='sales'),
    path('updatesales/<str:pk>', views.updatesales, name='updatesales'),
    path('delivered/<str:pk>', views.deliveredorder, name='delivered'),
    # AUTH
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    path('register/', views.Register, name='register'),
    # ADMIN
    path('admin/', views.adminpage, name='admin'),
    # CUSTOMER
    path('order/', views.createsales, name='order_menu'),
    path('order_history/', views.customer_order, name='customer_order'),
    # VALIDATIONS
    path('validation1/', views.validation1, name='validation1'),
]
