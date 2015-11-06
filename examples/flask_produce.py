#!/usr/bin/env python
from flask import Flask
from flask.ext.rabbitplay import Rabbit
from time import sleep

# make an app
app = Flask(__name__)

# set some configurations
app.config['RABBIT_VHOST'] = 'vhost'
app.config['RABBIT_USER'] = 'user'
app.config['RABBIT_PASSWORD'] = 'password'
app.config['DEBUG'] = True

# down the rabbit hole
rabbit = Rabbit(app)


@app.route('/test', methods=['GET'])
def test():
    run1 = rabbit.produce('rabbit_queue1', 'test01')
    run2 = rabbit.produce('rabbit_queue2', 'test01')
    run3 = rabbit.produce('rabbit_queue2', 'test01')
    return ', '.join(map(str, (run1, run2, run3)))

app.run()
