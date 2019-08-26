# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(dumpYard)
admin.site.register(Agent)
admin.site.register(actions)
admin.site.register(userType)