"""
Flask-RabbitPlay
-------------

Flask extension on top of rabbitplay library.
"""
from setuptools import setup

setup(
    name='Flask-RabbitPlay',
    version='0.1',
    url='https://github.com/SwipeBank/flask_rabbitplay',
    license='GPLv2',
    author='Eugene <f0t0n> Naydenov, Michael <m1kev> Voropaiev',
    author_email='t.34.oxygen@gmail.com, m.voropaiev@gmail.com',
    description='Flask extension on top of rabbitplay library.',
    long_description=__doc__,
    py_modules=['flask_rabbitplay'],
    platforms='any',
    install_requires=[
        'Flask==0.10.1',
        'rabbitplay==0.7.1'
    ]
)
