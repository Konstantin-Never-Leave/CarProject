from django.contrib import admin
from .models import CustomUser, CommercialUser


@admin.register(CustomUser)
class CarAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'second_name']
    list_editable = ['first_name', 'second_name']


@admin.register(CommercialUser)
class CommercialUserAdmin(admin.ModelAdmin):
    list_display = ['legal_name', 'owner', 'legal_address']
    filter_horizontal = ['employees', 'service_list', 'serviced_car']
