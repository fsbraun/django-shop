from django.urls import include, path
from shop.urls import rest_api
from shop.urls import auth
from shop.urls import payment


app_name = 'shop'

urlpatterns = [
    path('api/', include(rest_api)),
    path('auth/', include(auth)),
    path('payment/', include(payment)),
]
