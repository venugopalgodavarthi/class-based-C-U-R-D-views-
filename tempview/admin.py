from django.contrib import admin
from tempview.models import emp
# Register your models here.


class empadmin(admin.ModelAdmin):
    list_display=['name','email','sal']

admin.site.register(emp,empadmin)
