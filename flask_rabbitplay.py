from flask import current_app
from rabbitplay import Producer
import ssl
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

CONFIG_DEFAULTS = {
    'RABBIT_QUEUE': 'queue',
    'RABBIT_HOST': 'localhost',
    'RABBIT_PORT': 5672,
    'RABBIT_VHOST': None,
    'RABBIT_USER': None,
    'RABBIT_PASSWORD': None,
    'RABBIT_CLEAN_CREDS': True,
    'RABBIT_HEARTBEAT_INTERVAL': 30,
    'RABBIT_SSL_ENABLE': False,
    'RABBIT_SSL_VERSION': ssl.PROTOCOL_SSLv23,
    'RABBIT_CERTFILE': None,
    'RABBIT_KEYFILE': None,
    'RABBIT_CA_CERTS': None,
    'RABBIT_CERT_REQS': ssl.CERT_NONE
}


class Rabbit(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        for key, value in CONFIG_DEFAULTS.items():
            app.config.setdefault(key, value)

        app.extensions['rabbitplay'] = self

        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

    def connect(self):
        self.rabbit = Producer(
            queue=current_app.config['RABBIT_QUEUE'],
            host=current_app.config['RABBIT_HOST'],
            port=current_app.config['RABBIT_PORT'],
            vhost=current_app.config['RABBIT_VHOST'],
            user=current_app.config['RABBIT_USER'],
            password=current_app.config['RABBIT_PASSWORD'],
            clean_creds=current_app.config['RABBIT_CLEAN_CREDS'],
            heartbeat_interval=current_app.config['RABBIT_HEARTBEAT_INTERVAL'],
            ca_certs=current_app.config['RABBIT_CA_CERTS'],
            cert_reqs=current_app.config['RABBIT_CERT_REQS'],
            certfile=current_app.config['RABBIT_CERTFILE'],
            keyfile=current_app.config['RABBIT_KEYFILE'],
            ssl_enable=current_app.config['RABBIT_SSL_ENABLE'],
            ssl_version=current_app.config['RABBIT_SSL_VERSION']
        )
        return self.rabbit.get_channel()

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'rabbitplay_conn'):
            ctx.rabbitplay_conn.close()

    @property
    def connection(self):
        ctx = stack.top
        if ctx is not None:
            if not (hasattr(ctx, 'ctx_rabbitplay_ch') or
                    hasattr(ctx, 'rabbitplay_conn')):
                ctx_rabbitplay_ch, ctx.rabbitplay_conn = self.connect()
            return ctx_rabbitplay_ch, ctx.rabbitplay_conn

    def produce(self, message):
        channel, connection = self.connection
        self.rabbit.publish(message)
