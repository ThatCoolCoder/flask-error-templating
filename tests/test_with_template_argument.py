from flask import *
from flask_error_templating import *

app = Flask(__name__)

@app.route('/')
def homepage():
    return '<h1>Homepage</h1>'

error_pages = [
    ErrorPage(404, 'The page you are looking for does not exist')
]
create_http_error_handlers(app, error_pages, 'template_argument.html',
    template_argument='Hello there. Writing more to make this more impressive')

if __name__ == '__main__':
    app.run()