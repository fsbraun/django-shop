from django.utils.translation import gettext_lazy as _

from cms.app_base import CMSApp


class CatalogListCMSApp(CMSApp):
    name = _("Catalog List")

    def get_urls(self, page=None, language=None, **kwargs):
        raise NotImplementedError(f"{self.__class__} must implement method `.get_urls()`.")


class CatalogSearchApp(CMSApp):
    """
    This CMS apphook shall be used to render the list view for generic search results.
    These results are just determined by the search query and not influenced by other means,
    such as filters and categories. Usually this `Catalog Search` app is attached to a CMS
    page named "Search Results". That CMS page must be tagged with the ID: 'shop-search-product'.
    """
    name = _("Catalog Search")

    def get_urls(self, page=None, language=None, **kwargs):
        from django.urls import re_path
        from shop.search.mixins import CatalogSearchViewMixin
        from shop.views.catalog import ProductListView

        SearchView = type('SearchView', (CatalogSearchViewMixin, ProductListView), {})
        return [
            re_path(r'^', SearchView.as_view(
                filter_backends=[],
                search_fields=['product_name', 'product_code', 'body']
            )),
        ]


class OrderApp(CMSApp):
    name = _("View Orders")
    cache_placeholders = False

    def get_urls(self, page=None, language=None, **kwargs):
        from django.urls import re_path
        from shop.views.order import OrderView

        return [
            re_path(r'^(?P<slug>[\w-]+)/(?P<secret>[\w-]+)', OrderView.as_view(many=False)),  # publicly accessible
            re_path(r'^(?P<slug>[\w-]+)', OrderView.as_view(many=False)),  # requires authentication
            re_path(r'^', OrderView.as_view()),  # requires authentication
        ]


class PasswordResetApp(CMSApp):
    name = _("Password Reset Confirm")

    def get_urls(self, page=None, language=None, **kwargs):
        from django.urls import re_path
        from shop.views.auth import PasswordResetConfirmView

        return [
            re_path(r'^(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})',
                PasswordResetConfirmView.as_view(),
            )
        ]
