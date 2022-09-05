# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from .views import *


urlpatterns = [

    # The home page
    path('', PlayerDetailView.as_view(), name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
