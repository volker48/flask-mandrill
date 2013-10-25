from setuptools import setup


setup(
    name='Flask-Mandrill',
    version='0.1',
    url='http://github.com/volker48/flask-mandrill',
    license='MIT',
    author='Marcus McCurdy',
    author_email='marcus.mccurdy@gmail.com',
    description='Adds Mandrill support to Flask applications',
    long_description=__doc__,
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
