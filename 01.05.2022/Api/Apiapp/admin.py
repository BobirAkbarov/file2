from django.contrib import admin

from .models import Mailing_list, Custom, Message


admin.site.register(Mailing_list)
admin.site.register(Custom)
admin.site.register(Message)
