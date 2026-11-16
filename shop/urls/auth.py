from django.urls import re_path
from shop.forms.auth import RegisterUserForm, ContinueAsGuestForm
from shop.views.auth import AuthFormsView, LoginView, LogoutView, PasswordChangeView, PasswordResetRequestView

urlpatterns = [
    re_path(r'^password/reset/?$', PasswordResetRequestView.as_view(),
        name='password-reset-request'),
    re_path(r'^login/?$', LoginView.as_view(),
        name='login'),
    re_path(r'^register/?$', AuthFormsView.as_view(form_class=RegisterUserForm),
        name='register-user'),
    re_path(r'^continue/?$', AuthFormsView.as_view(form_class=ContinueAsGuestForm),
        name='continue-as-guest'),

    re_path(r'^logout/?$', LogoutView.as_view(),
        name='logout'),
    re_path(r'^password/change/?$', PasswordChangeView.as_view(),
        name='password-change'),
]
