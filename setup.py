#!/usr/bin/env python
from setuptools import setup, find_packages
import shop

with open('README.md') as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'Django>=5.2,<5.3',
    'django-filer>=3.6,<4',
    'django-ipware',
    'django-fsm-2>=4.3,<5',
    'django-fsm-2-admin>=2.0.1,<3',
    'djangorestframework>=3.16,<4',
    'dj-rest-auth>=4,<5',
    'Django-Select2>=7.11',
    'django-admin-sortable2',
    'django-formtools',
    'django-polymorphic>=4,<5',
    'django-post-office>=3.11',
    'django-cms>=3.11.11,<4',
    'django-treebeard>=4.8,<5',
    'django-entangled>=0.5.4',
    'djangocms-text-ckeditor>=5.1.7,<6',
    'requests',
]

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.11',
    'Framework :: Django',
    'Framework :: Django :: 5.2',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

setup(
    author="Jacob Rief",
    author_email="jacob.rief@gmail.com",
    name="django-shop",
    version=shop.__version__,
    description="A RESTful e-commerce framework based on Django",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/fsbraun/django-shop',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    packages=find_packages(exclude=['tests', 'docs']),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    python_requires='>=3.11',
)
