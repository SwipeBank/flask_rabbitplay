#!/usr/bin/env python
from flask import Flask
from flask.ext.rabbitplay import Rabbit

# make an app
app = Flask('rabbit_example')

# set some configurations
app.config['RABBIT_QUEUE'] = 'hello_world_queue'
app.config['RABBIT_VHOST'] = 'vhost'
app.config['RABBIT_USER'] = 'user'
app.config['RABBIT_PASSWORD'] = 'password'

# down the rabbit hole
rabbit = Rabbit(app)
with app.app_context():
    rabbit.produce('test')
