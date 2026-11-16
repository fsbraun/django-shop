from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from shop.admin.defaults.order import OrderAdmin
from shop.admin.delivery import DeliveryOrderAdminMixin
from shop.admin.order import PrintInvoiceAdminMixin
from shop.models.defaults.order import Order

admin.site.register(get_user_model(), UserAdmin)


@admin.register(Order)
class OrderAdmin(PrintInvoiceAdminMixin, DeliveryOrderAdminMixin, OrderAdmin):
        pass
