"""
Flask-RabbitPlay
-------------

Flask extension on top of rabbitplay library.
"""
from setuptools import setup

rabbit_url = 'git+https://github.com/SwipeBank/rabbitplay.git'
rabbit_ver = '0.7'

setup(
    name='Flask-RabbitPlay',
    version='0.1',
    url='https://github.com/SwipeBank/flask_rabbitplay',
    license='GPLv2',
    author='Michael Voropaiev',
    author_email='m.voropaiev@gmail.com',
    description='Flask extension on top of rabbitplay library.',
    long_description=__doc__,
    py_modules=['flask_rabbitplay'],
    platforms='any',
    install_requires=[
        'Flask==0.10.1',
        'pika==0.10.0',
        'rabbitplay=={ver}'.format(
            ver=rabbit_ver
        )
    ],
    dependency_links=[
        '{url}@{ver}#egg=rabbitplay-{ver}'.format(
            url=rabbit_url,
            ver=rabbit_ver
        )
    ]
)
