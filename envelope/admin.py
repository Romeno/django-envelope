# -*- coding: utf-8 -*-
from django.contrib import admin
from envelope.models import Appeal


class AppealAdmin(admin.ModelAdmin):
    readonly_fields = ('sender', 'email', 'message')
    list_display = ('__unicode__', 'sender', 'email', 'date_sent')

admin.site.register(Appeal, AppealAdmin)


