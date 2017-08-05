# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Status, Comment, NestedComment

# Register your models here.
admin.site.register(Status)
admin.site.register(Comment)
admin.site.register(NestedComment)
