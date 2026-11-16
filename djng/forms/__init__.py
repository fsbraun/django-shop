from django.forms.forms import DeclarativeFieldsMetaclass, BaseForm
from django.forms.models import BaseModelForm, ModelFormMetaclass
from .angular_base import BaseFieldsModifierMetaclass, NgFormBaseMixin
from .angular_model import NgModelFormMixin
from .angular_validation import NgFormValidationMixin


class NgDeclarativeFieldsMetaclass(BaseFieldsModifierMetaclass, DeclarativeFieldsMetaclass):
    pass


class NgForm(NgFormBaseMixin, BaseForm, metaclass=NgDeclarativeFieldsMetaclass):
    """
    Convenience class to be used instead of Django's internal ``forms.Form`` when declaring
    a form to be used with AngularJS.
    """


class NgModelFormMetaclass(BaseFieldsModifierMetaclass, ModelFormMetaclass):
    def __new__(cls, name, bases, attrs):
        meta = attrs.get('Meta')
        if meta is None:
            meta = next((base.Meta for base in bases if hasattr(base, 'Meta')), object)
        attrs['Meta'] = type('Meta', (meta,), {
            'formfield_callback': staticmethod(cls.formfield_callback),
        })
        return super().__new__(cls, name, bases, attrs)


class NgModelForm(NgFormBaseMixin, BaseModelForm, metaclass=NgModelFormMetaclass):
    """
    Convenience class to be used instead of Django's internal ``forms.ModelForm`` when declaring
    a model form to be used with AngularJS.
    """
