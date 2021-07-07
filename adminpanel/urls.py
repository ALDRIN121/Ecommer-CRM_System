from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.mainpg),
    path('review', views.reviewpg),
    path('reviewmsg', views.emailpg),
    path('sentmail', views.sent_email),
    path('demographic', views.demographic),
    path('loc', views.loc_prd),
    path('add_prd', views.add_prd),
    path('addpd', views.addpd),
    path('allusr', views.allusr),
    path('allorder', views.allorder),
    path('month', views.monthly),
    path('months', views.monthlys),
















]
