from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('home', views.mainpg),
    path('mobile', views.mobile),
    path('laptop', views.laptop),
    path('tv', views.tv),
    path('speaker', views.speaker),
    path('prd_detail', views.product_detail),
    path('', views.login),
    path('register', views.register),
    path('signup', views.signup),
    path('signin', views.signin),
    path('transact', views.transact),
    path('review', views.review),
    path('review_save', views.review_save),
    path('cart', views.cart),
    path('checkout', views.checkout),
    path('edit_cart', views.edit_cart),
    path('update_cart', views.update_cart),
    path('logout', views.logout_user),








]
