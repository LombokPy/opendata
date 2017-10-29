# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Member

# Register your models here.
class MemberDisplay(admin.ModelAdmin):
    list_display = ('nama','email')

admin.site.register(Member, MemberDisplay)
