from django.forms.forms import BaseForm
from django.forms.models import BaseModelForm
from djng.forms import NgDeclarativeFieldsMetaclass, NgModelFormMetaclass, NgFormBaseMixin


class Bootstrap3FormMixin:
    field_css_classes = 'form-group has-feedback'
    widget_css_classes = 'form-control'
    form_error_css_classes = 'djng-form-errors'
    field_error_css_classes = 'djng-form-control-feedback djng-field-errors'
    label_css_classes = 'control-label'

    def as_div(self):
        """
        Returns this form rendered as HTML with <div class="form-group">s for each form field.
        """
        return self.render('djng/forms/bootstrap3/form.html')


class Bootstrap3Form(Bootstrap3FormMixin, NgFormBaseMixin, BaseForm, metaclass=NgDeclarativeFieldsMetaclass):
    """
    Convenience class to be used instead of Django's internal ``forms.Form`` when declaring
    a form to be used with AngularJS and Bootstrap3 styling.
    """


class Bootstrap3ModelForm(Bootstrap3FormMixin, NgFormBaseMixin, BaseModelForm, metaclass=NgModelFormMetaclass):
    """
    Convenience class to be used instead of Django's internal ``forms.ModelForm`` when declaring
    a model form to be used with AngularJS and Bootstrap3 styling.
    """
