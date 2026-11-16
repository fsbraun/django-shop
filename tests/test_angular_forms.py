from django.forms.renderers import DjangoTemplates
import pytest

from djng.forms import NgForm, NgFormValidationMixin, NgModelFormMixin, fields
from djng.forms.fields import DefaultFieldMixin
from djng.styling.bootstrap3.forms import Bootstrap3Form
from shop.forms.checkout import CustomerForm


class EmailForm(NgModelFormMixin, NgFormValidationMixin, NgForm):
    email = fields.EmailField()


class BootstrapEmailForm(NgModelFormMixin, NgFormValidationMixin, Bootstrap3Form):
    email = fields.EmailField()


@pytest.mark.parametrize('form_class,render_method', [
    (EmailForm, 'as_p'),
    (BootstrapEmailForm, 'as_div'),
])
def test_invalid_form_renders_angular_validation(form_class, render_method):
    form = form_class(data={'email': 'invalid'}, renderer=DjangoTemplates())
    assert not form.is_valid()
    html = getattr(form, render_method)()
    assert 'ng-model' in html
    assert 'ng-show' in html
    assert 'Enter a valid email address.' in html


def test_model_form_keeps_angular_model_fields():
    assert isinstance(CustomerForm.base_fields['salutation'], DefaultFieldMixin)
