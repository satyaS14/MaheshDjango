from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
import wasteManagement.views as wasteManagementViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^accounts/login', wasteManagementViews.userLogin, name='userLogin'),
    url('', include('wasteManagement.urls')),
    
]
