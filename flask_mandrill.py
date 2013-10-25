import requests

class Mandrill(object):
    app = None
    mandrill_api = None
    api_key = None

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.api_key = app.config['MANDRILL_API_KEY']
        self.app = app

    def send_email(self, **kwargs):
        if not self.api_key:
            raise ValueError('No Mandrill API key has been configured')
        kwargs.setdefault('key', self.api_key)
        requests.post(self.messages_endpoint, data=kwargs)

    @property
    def messages_endpoint(self):
        return 'https://mandrillapp.com/api/1.0/messages/send.json'
