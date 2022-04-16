from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('register/', views.register, name='register'),
    path('basket/<slug:slug>/', views.basket, name='basket'),
    path('baskets/', views.basket_list, name='basket_list'),
    path('edit/<username>/', views.edit_account, name='edit_account'),
    path('likes/', views.like_user_list, name='like_user_list'),
]
