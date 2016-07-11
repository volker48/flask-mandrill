flask-mandrill
==============

Flask plugin to simplify sending emails through Mandrill.

## Installation

`pip install flask-mandrill`

## Usage

```python
from flask.ext.mandrill import Mandrill

app = Flask(__name__)
app.config['MANDRILL_API_KEY'] = 'your api key'
app.config['MANDRILL_DEFAULT_FROM'] = 'admin@yourdomain.com'
mandrill = Mandrill(app)
mandrill.send_email(
    from_email='someone@yourdomain.com',
    subject='Subject',
    to=[{'email': 'someone@somedomain.com'}, {'email': 'someoneelse@someotherdomain.com'}],
    text='Hello World'
)
```

To use a templated e-mail, specify template_name='some template name as an argument.

## send_email API Documentation

For additional information about send_email parameters: https://mandrillapp.com/api/docs/messages.html

## License

[MIT](https://github.com/volker48/flask-mandrill/blob/master/README.md) © [Marcus McCurdy](https://github.com/volker48)