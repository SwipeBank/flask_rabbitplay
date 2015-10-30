# Flaks_RabbitPlay

Flask extension on top of [rabbitplay](https://github.com/SwipeBank/rabbitplay) library.

## Examples  

### Produce a message:  
Code:
```py
from flask import Flask
from flask.ext.rabbitplay import Rabbit

app = Flask('rabbit_example')

rabbit = Rabbit(app)
with app.app_context():
    rabbit.produce('test')

```
Command line:
```sh
python -m examples.flask_produce
```
