from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.register(Size)
admin.site.register(ProdType)
admin.site.register(Branch)
admin.site.register(FoodInventory)
admin.site.register(OrderCart)
admin.site.register(MOP)
admin.site.register(OrderProcess)

@admin.register(DailySales)
class DailySalesAdmin(admin.ModelAdmin):
    readonly_fields = ["reference_number"]