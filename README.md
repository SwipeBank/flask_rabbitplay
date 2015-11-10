# RabbitPlay (Flask extension)

Flask extension on top of [rabbitplay](https://github.com/SwipeBank/rabbitplay) library.

## Installation

* Using [pip](https://pip.readthedocs.org/en/stable/):
  ```sh
  # master branch:
  pip install --process-dependency-links git+https://github.com/SwipeBank/flask_rabbitplay.git#egg=flask_rabbitplay
  # specific version (tag):
  pip install --process-dependency-links git+https://github.com/SwipeBank/flask_rabbitplay.git@0.1#egg=flask_rabbitplay-0.1
  ```

* Manual installation:
  ```sh
  git clone https://github.com/SwipeBank/flask_rabbitplay.git
  cd rabbitplay
  # git checkout 0.1
  python setup.py install
  ```

## Examples  

### Produce a message:  
* Code:

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

* [Command line](/examples/flask_produce.py):

  ```sh
  python -m examples.flask_produce
  ```
