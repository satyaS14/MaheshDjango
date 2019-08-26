from django.conf.urls import include, url

from . import views

urlpatterns = [
    
    url('^userLogin/.*', views.userLogin, name='userLogin'),
    url('^userLogout/', views.userLogout, name='userLogout'),

    url('^assignAgents/', views.assignAgents, name='assignAgents'),


    url('^$', views.index, name='index'),
]