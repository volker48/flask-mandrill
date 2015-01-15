import unittest
from mock import patch, MagicMock
from flask_mandrill import Mandrill
import json

# Set up test API key for emails
app = MagicMock()
app.config = {}
app.config['TESTING'] = True
app.config['MANDRILL_API_KEY'] = '12345'
app.config['MANDRILL_DEFAULT_FROM'] = 'from'

headers={'Content-Type': 'application/json'}

class FlaskMandrillTest(unittest.TestCase):

    def setUp(self):
        self.mail = Mandrill(app)

    def test_get_api_key(self):
        self.assertEqual(self.mail.api_key, app.config['MANDRILL_API_KEY'])

    @patch('flask_mandrill.requests')
    def test_base_email(self, mock_requests):
        self.mail.send_email(
            subject="subject",
            text="text",
            from_email='from',
            to=[{'email': 'a@pop'}]
        )

        data = {
            'async': False,
            'ip_pool': '',
            'key': app.config['MANDRILL_API_KEY'],
            'message': {
                'subject': 'subject',
                'text': 'text',
                'from_email': 'from',
                'to': [{'email': 'a@pop'}]
            }
        }

        mock_requests.post.assert_called_with(
            self.mail.messages_endpoint,
            data=json.dumps(data),
            headers=headers
        )

    @patch('flask_mandrill.requests')
    def test_specify_key(self, mock_requests):
        mail = Mandrill()
        mail.send_email(
            key="ABCDEFG",
            from_email='from'
        )

        data = {
            'async': False,
            'ip_pool': '',
            'key': "ABCDEFG",
            'message': {'from_email': 'from'}
        }

        mock_requests.post.assert_called_with(
            self.mail.messages_endpoint,
            data=json.dumps(data),
            headers=headers
        )

    def test_fails_no_key(self):
        mail = Mandrill()
        self.assertRaises(ValueError, mail.send_email)

    def test_fails_no_sender(self):
        mail = Mandrill()
        self.assertRaises(ValueError, mail.send_email, key='ABCDEFG')

    @patch('flask_mandrill.requests')
    def test_default_sender(self, mock_requests):
        self.mail.send_email()

        data = {
            'async': False,
            'ip_pool': '',
            'key': app.config['MANDRILL_API_KEY'],
            'message': {'from_email': 'from'}
        }

        mock_requests.post.assert_called_with(
            self.mail.messages_endpoint,
            data=json.dumps(data),
            headers=headers
        )

    @patch('flask_mandrill.requests')
    def test_sends_to_template(self, mock_requests):
        self.mail.send_email(template_name="a_name")

        data = {
            'async': False,
            'ip_pool': '',
            'key': app.config['MANDRILL_API_KEY'],
            'template_name': 'a_name',
            'template_content': [],
            'message': {'from_email': 'from'}
        }

        mock_requests.post.assert_called_with(
            self.mail.templates_endpoint,
            data=json.dumps(data),
            headers=headers
        )
