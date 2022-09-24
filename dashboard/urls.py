from django.urls import path
from . import views
from django.views import View
from .views import *

urlpatterns = [
    path('', views.index, name='home_page'),
    path('main/', views.home, name='main'),
     path('matches/', views.matches, name='matches'),
    path('players/', EditorChartView.as_view(), name='players'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog/single', views.single_blog, name='single_blog')
]
