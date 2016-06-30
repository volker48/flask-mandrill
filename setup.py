"""
Flask-Mandrill
==============

A Flask Extension to remove some of the boiler plate encountered when
sending emails with `Mandrill <http://www.mandrill.com/>`_

Installation
````````````

.. code:: bash

    $ pip install flask-mandrill


Usage
`````

.. code:: python

        from flask import Flask
        from flask.ext.mandrill import Mandrill

        app = Flask(__name__)
        app.config['MANDRILL_API_KEY'] = 'your api key'
        mandrill = Mandrill(app)
        mandrill.send_email(
            from_email='someone@yourdomain.com',
            to=[{'email': 'someoneelse@someotherdomain.com'}],
            text='Hello World'
        )
"""

from setuptools import setup


setup(
    name='Flask-Mandrill',
    version='0.3',
    url='http://github.com/volker48/flask-mandrill',
    license='MIT',
    author='Marcus McCurdy',
    author_email='marcus.mccurdy@gmail.com',
    description='Adds Mandrill support to Flask applications',
    long_description=__doc__ + '\n\n' +
                     open('HISTORY.rst').read(),
    py_modules=['flask_mandrill'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'requests'
        ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)
