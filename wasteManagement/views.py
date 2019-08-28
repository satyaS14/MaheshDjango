# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, update_session_auth_hash
from django.contrib.auth import login
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings

from .models import *
import os
from django.conf import settings
# from django.contrib.gis.geoip  import GeoIP


def setEnv():
    
    f = open(os.path.join(settings.BASE_DIR, "wasteManagement", "cred.txt"), "r")
    text = f.read()
    l = text.split()

    for i in range(len(l)):
        
        data = l[i].split("=")[1].strip()
        key = l[i].split("=")[0]
        
        # Gmail Username
        if key == "GMAIL_USERNAME":
            os.environ["GMAIL_USERNAME"] = data
        
        # Gmail Password
        elif key == "GMAIL_PASSWORD":
            os.environ["GMAIL_PASSWORD"] = data

        # Google Maps API Key
        elif key == "MAPS_API_KEY":
            os.environ["MAPS_API_KEY"] = data



# Create your views here.
def userLogin(request):
    context = {}
    template_name = 'wasteManagement/login.html'

    setEnv()

    # g = GeoIP()
    # ip = request.META.get('REMOTE_ADDR', None)
    # if ip:
    #     city = g.city(ip)['city']
    #     print "\n\n\n"+str(city)+"\n\n\n"

    if request.method == "POST":

        username = request.POST.get('username2')
        password = request.POST.get('pass')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active: 
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

        context['error_message'] = 'Invalid username or password.'

    return render(request, template_name, context)


def userLogout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


@login_required(login_url='/userLogin')
def index(request):
    context = {}
    context["API_KEY"] = os.environ["MAPS_API_KEY"]
    template_name = 'wasteManagement/index.html'
    
    if request.user.usertype.isAgent:
        context['userType'] = "agent"
        context['score'] = Agent.objects.get(user=request.user).agentScore

    elif request.user.usertype.isGovt or request.user.userType.isAdmin:
        context['userType'] = "govt"
        context['dumpYards'] = dumpYard.objects.all()
        context['agents'] = Agent.objects.all()

    else:
        context['userType'] = "others"
        context['score'] = 0

    return render(request, template_name, context)


@csrf_exempt
def assignAgents(request):
    
    if request.method == "POST":

        agents = request.POST["agentsList"]
        yard = request.POST["yard"]

        subject = 'Alert -- MaheshDjango'
        message = 'Agent - Please check yard-1. Levels at that yard crosssed thresholds !!!'
        email_from = os.environ["GMAIL_USERNAME"]
        recipient_list = ['urs.prasanthvja@gmail.com',]
        
        send_mail( subject, message, email_from, recipient_list, auth_user=email_from, auth_password=os.environ["GMAIL_PASSWORD"] )
        
        return HttpResponse("Notification sent !!! " + str(agents) + " " + str(yard))

    else:
        return HttpResponse("Some unknown error occurred !! Received GET request !!!!")