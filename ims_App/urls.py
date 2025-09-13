from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/', views.create_view, name='create'),
    path('read/', views.read_view, name='read'),
    path('update/<int:product_id>/', views.update_view, name='update'),
    path('delete/<int:product_id>', views.delete_view, name='delete'),

]
