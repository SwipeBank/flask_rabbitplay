#!/usr/bin/env python
from flask import Flask
from flask.ext.rabbitplay import Rabbit
from time import sleep

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
    sleep_secs = 5
    rabbit.produce('test01')
    print 'sent one message..'
    print 'sleeping for {} seconds..'.format(sleep_secs)
    sleep(sleep_secs)
    rabbit.produce('test02')
    print 'sent another message..'
