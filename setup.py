#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Django',
    'djangorestframework',
    'requests',
    'pyjwt'
]

test_requirements = [ ]

setup(
    author="Lucas Paula",
    author_email='luolcami@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='keycloak_django_utils',
    name='keycloak_django_utils',
    packages=find_packages(include=['keycloak_django_utils', 'keycloak_django_utils.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/lucas8107/keycloak_django_utils',
    version='0.2.0',
    zip_safe=False,
)
