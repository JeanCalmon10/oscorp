from django.urls import path
from . import views

app_name = 'pharmacies'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('products/', views.products, name='products'),
    path('create_product/', views.create_product, name='create_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('about_us/', views.about_us, name='about_us'),
    
]


