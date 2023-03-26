from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # INVENTORY
    path('inventory/', views.inventory, name='inventory'),
    path('createstock/', views.createstock, name='createstock'),
    path('updatestock/<str:pk>', views.updatestock, name='updatestock'),
    path('deletestock/<str:pk>', views.deletestock, name='deletestock'),
    # SALES
    path('sales/', views.sales, name='sales'),
    path('updatesales/<str:pk>', views.updatesales, name='updatesales'),
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
