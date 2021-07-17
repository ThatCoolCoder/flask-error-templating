from flask import *
from flask_error_templating import *

app = Flask(__name__)

@app.route('/')
def homepage():
    return '<h1>Homepage of test_with_long_message</h1>'

error_pages = [
    ErrorPage(404, 'The page you are looking for does not exist',
        'long message ' * 50)
]
create_http_error_handlers(app, error_pages, 'long_message.html')

if __name__ == '__main__':
    app.run()