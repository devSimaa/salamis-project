from django.urls import path
from . import views

app_name = 'goods'
urlpatterns = [
    path('', views.catalog, name='index'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<int:product_id>', views.product, name='product'),
    path('product/<slug:product_slug>', views.product, name='product'),

]
