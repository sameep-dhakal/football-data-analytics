from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager)
from django.core.mail import EmailMessage, send_mail
from django.db import transaction
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View

from .forms import *
from .models import *
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from apps.home.forms import PlayerDetailsForm



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


class PlayerDetailView(View):
    def get(Self , request):   
        form = PlayerDetailsForm()

        context ={
            "form":form
        }

        # return render(request, "/home/sameep/Desktop/soft-ui-dashboard-django/apps/templates/home/index.html", context)
        return render(request, "home/index.html", context)


