import requests
import json

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
        """
        Sends an email using Mandrill's API. Returns a
        Requests :class:`Response` object.
        At a minimum kwargs must contain the keys to, from_email, and text.
        Everything passed as kwargs except for the keywords 'key', 'async',
        and 'ip_pool' will be sent as key-value pairs in the message object.
        Reference https://mandrillapp.com/api/docs/messages.JSON.html#method=send
        for all the available options.
        """
        endpoint = self.messages_endpoint

        data = {
            'async': kwargs.pop('async', False),
            'ip_pool': kwargs.pop('ip_pool', ''),
            'key': kwargs.pop('key', self.api_key),
        }

        if not data.get('key', None):
            raise ValueError('No Mandrill API key has been configured')

        # Sending a template through Mandrill requires a couple extra args
        # and a different endpoint.
        if kwargs.get('template_name', None):
            data['template_name'] = kwargs.pop('template_name')
            data['template_content'] = kwargs.pop('template_content', [])
            endpoint = self.templates_endpoint

        data['message'] = kwargs

        if self.app:
            data['message'].setdefault(
                'from_email',
                self.app.config.get('MANDRILL_DEFAULT_FROM', None)
            )

        if endpoint != self.templates_endpoint and not data['message'].get('from_email', None):
            raise ValueError(
                'No from email was specified and no default was configured')


        response = requests.post(endpoint,
                                 data=json.dumps(data),
                                 headers={'Content-Type': 'application/json'})
        response.raise_for_status()
        return response

    @property
    def messages_endpoint(self):
        return 'https://mandrillapp.com/api/1.0/messages/send.json'

    @property
    def templates_endpoint(self):
        return 'https://mandrillapp.com/api/1.0/messages/send-template.json'
