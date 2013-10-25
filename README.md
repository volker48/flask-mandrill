flask-mandrill
==============

Flask plugin to simplify sending emails through Mandrill.


Installation
------------

    pip install flask-mandrill

Usage
-----

    app = Flask(__name__)
    app.config['MANDRILL_API_KEY'] = 'your api key'
    mandrill = Mandrill(app)
    mandrill.send_email(
        from_email='someone@yourdomain.com',
        to=[{'email': 'someoneelse@someotherdomain.com'}],
        text='Hello World'
    )