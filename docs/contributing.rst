.. _contributing:

=============
Contributing
=============

Naming conventions
==================

The official name of this project is **django-SHOP**. Third party plugins for **django-SHOP** shall
follow the same naming convention as for plugins of **django-CMS**: Third party package names shall
start with **djangoshop** followed by a dash; no space or dash shall be added between **django** and
**shop**, for example: ``djangoshop-stripe``

**Django-SHOP** should be capitalised at the start of sentences and in title-case headings.


Running tests
==============

It's important to run tests before committing :)

Python 3.11 and Django 5.2
--------------------------

The GitHub Actions workflow uses pyenv to install Python 3.11.15 and runs the
suite on Django 5.2.19 with django CMS 3.11.11. It uploads JUnit test results and
installed dependency versions. The Django 2.2 and 3.0 baselines passed before
moving forward; they are no longer supported by the current source tree.
Django 4.2 also passed before this step; the current target is Django 5.2,
while django CMS remains on version 3.11.

To reproduce the CI environment::

    pyenv install --skip-existing 3.11.15
    PYENV_VERSION=3.11.15 pyenv exec python -m venv /tmp/django-shop-dev
    . /tmp/django-shop-dev/bin/activate
    python -m pip install pip==24.3.1 setuptools==69.5.1 wheel==0.45.1
    python -m pip install -r tests/django52-requirements.txt
    python -m pip install --no-deps --no-build-isolation -e .
    python -m pip check
    cd tests
    DJANGO_DEBUG=1 python manage.py makemigrations testshop --noinput
    DJANGO_DEBUG=1 python -m pytest

Alternatively, run ``tox -e py311-django52`` with Python 3.11 available.

The source is modernized with ``pyupgrade --py311-plus`` and
``django-upgrade --target-version 5.2``. Run these tools on changed Python files.

Upgrade notes
~~~~~~~~~~~~~

* Replace ``django-fsm`` and ``django-fsm-admin`` with ``django-fsm-2`` and
  ``django-fsm-2-admin``. The ``django_fsm`` and ``fsm_admin`` import paths and
  installed app labels remain the same. Remove the old distributions before
  installing the replacements because they provide the same Python modules.
* Replace ``django-rest-auth`` with ``dj-rest-auth``, change the installed app
  from ``rest_auth`` to ``dj_rest_auth``, and move the login serializer setting
  from ``REST_AUTH_SERIALIZERS`` into ``REST_AUTH``.
* The ``djng`` module and its assets are now bundled with django-SHOP to support
  Django 5.2. Uninstall the separately installed ``django-angular`` distribution
  before upgrading django-SHOP.
  Its original MIT license and the changes are recorded in ``djng/NOTICE.txt``.
* Cascade 2.3.14 is now bundled because its upstream dependency constraint
  excludes Django 5.2. Uninstall the separately installed ``djangocms-cascade``
  distribution before upgrading django-SHOP to avoid overlapping modules.
  Its MIT license and changes are
  recorded in ``cmsplugin_cascade/NOTICE.txt``. Existing content is not migrated
  to CMS 4 or 5 by this upgrade.
  Treebeard remains on its 4.x API for compatibility with CMS 3's plugin trees.
* Apply the dependency migrations and the ``email_auth`` migration that expands
  ``first_name`` to 150 characters. Register the user model in the admin for
  Filer's user autocomplete fields.
* Keep ``DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'`` in merchant settings
  to preserve existing primary key types for materialized shop models.


Community
==========

Most of the discussion around django SHOP takes place on IRC (Internet Relay Chat), on the freenode
servers in the #django-shop channel.

We also have a mailing list and a google group::

	http://groups.google.com/group/django-shop


Code guidelines
================

Unless otherwise specified, follow :pep:`8` as closely as possible.

An exception to PEP 8 is our rules on line lengths. Don’t limit lines of code to 79 characters if it
means the code looks significantly uglier or is harder to read. Consider 100 characters as a soft,
and 119 as a hard limit. Here soft limit means, that unless a line must be splitted across two
lines, it is more readable to stay with a long line.

Use the issue tracker only to report bugs. Send unsolicited pull requests only to fix bug – never
to add new features.

Use stack-overflow to ask for questions related to **django-SHOP**.

Most pull requests will be rejected without proper unit testing.

Before adding a new feature, please write a specification using the style for
`Django Enhancement Proposals`_.

More information about how to send a Pull Request can be found on GitHub:
https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request

.. _Django Enhancement Proposals: https://github.com/django/deps/blob/master/final/0001-dep-process.rst
