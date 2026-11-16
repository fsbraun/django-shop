import pytest
from cms.api import add_plugin
from cms.models import Placeholder
from cms.utils.plugins import copy_plugins_to_placeholder


@pytest.mark.django_db
def test_cascade_plugin_tree_can_be_copied():
    source = Placeholder.objects.create(slot='source')
    target = Placeholder.objects.create(slot='target')
    container = add_plugin(source, 'BootstrapContainerPlugin', 'en', glossary={})
    assert isinstance(container.path, str), (container.path, container.depth, container.numchild)
    row = add_plugin(source, 'BootstrapRowPlugin', 'en', target=container, glossary={})
    column = add_plugin(source, 'BootstrapColumnPlugin', 'en', target=row, glossary={})
    cart = add_plugin(source, 'ShopCartPlugin', 'en', target=column,
                      glossary={'render_type': 'summary'})

    copy_plugins_to_placeholder(source.get_plugins('en'), target, 'en')
    plugins = list(target.get_plugins('en').order_by('path'))
    assert [plugin.plugin_type for plugin in plugins] == [
        'BootstrapContainerPlugin', 'BootstrapRowPlugin',
        'BootstrapColumnPlugin', 'ShopCartPlugin',
    ]
    assert plugins[-1].parent_id == plugins[-2].pk
    copied_cart, _ = plugins[-1].get_plugin_instance()
    assert copied_cart.glossary == cart.glossary
    assert copied_cart._meta.app_label == 'cmsplugin_cascade'
