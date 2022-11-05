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
    # SALES
    path('sales/', views.sales, name='sales'),
    path('createsales/', views.createsales, name='createsales'),
    path('updatesales/<str:pk>', views.updatesales, name='updatesales'),
    # AUTH
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
]
