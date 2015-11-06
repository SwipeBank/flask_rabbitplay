# RabbitPlay (Flask extension)

Flask extension on top of [rabbitplay](https://github.com/SwipeBank/rabbitplay) library.

## Examples  

### Produce a message:  
Code:
```py
from flask import Flask
from flask.ext.rabbitplay import Rabbit

app = Flask(__name__)

rabbit = Rabbit(app)

@app.route('/', methods=['GET'])
def send_msg():
    return str(rabbit.produce('rabbit_queue1', 'test01'))

app.run()
```
Command line:
```sh
python -m examples.flask_produce
```
