from . import views
from django.urls import path

urlpatterns = [

    path('', views.home, name='home'),
    path('<slug:slug_c>/', views.home, name='product_by_category'),
    path('<slug:slug_c>/<slug_p>/', views.prod_det, name='product_det'),


    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('base/', views.base, name='base'),

]
