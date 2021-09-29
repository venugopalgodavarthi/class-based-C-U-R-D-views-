from django.contrib import admin
from formview.models import empmodel
# Register your models here.


class empadmin(admin.ModelAdmin):
    list_display=['name','email','sal']

admin.site.register(empmodel,empadmin)
