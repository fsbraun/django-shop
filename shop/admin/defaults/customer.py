from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.translation import gettext_lazy as _
from shop.admin.customer import CustomerProxy, CustomerInlineAdminBase, CustomerAdminBase


class CustomerInlineAdmin(CustomerInlineAdminBase):
    fieldsets = [
        (None, {'fields': ['get_number', 'salutation']}),
        (_("Addresses"), {'fields': ['get_shipping_addresses', 'get_billing_addresses']})
    ]
    readonly_fields = ['get_number', 'get_shipping_addresses', 'get_billing_addresses']

    @admin.display(
        description=_("Customer Number")
    )
    def get_number(self, customer):
        return customer.get_number() or '–'

    @admin.display(
        description=_("Shipping")
    )
    def get_shipping_addresses(self, customer):
        addresses = [(a.as_text(),) for a in customer.shippingaddress_set.all()]
        return format_html_join('', '<address>{0}</address>', addresses)

    @admin.display(
        description=_("Billing")
    )
    def get_billing_addresses(self, customer):
        addresses = [(a.as_text(),) for a in customer.billingaddress_set.all()]
        return format_html_join('', '<address>{0}</address>', addresses)


@admin.register(CustomerProxy)
class CustomerAdmin(CustomerAdminBase):
    class Media:
        css = {'all': ['shop/css/admin/customer.css']}

    inlines = [CustomerInlineAdmin]

    def get_list_display(self, request):
        list_display = list(super().get_list_display(request))
        list_display.insert(1, 'salutation')
        return list_display

    @admin.display(
        description=_("Salutation"),
        ordering='customer__salutation',
    )
    def salutation(self, user):
        if hasattr(user, 'customer'):
            return user.customer.get_salutation_display()
        return ''
