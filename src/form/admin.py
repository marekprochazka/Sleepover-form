from django.contrib import admin

# Register your models here.
from form.models import Request


class RequestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Request, RequestAdmin)
