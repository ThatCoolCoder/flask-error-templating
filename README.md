# flask-error-templating

Create Flask HTTP error handlers that use template rendering. This is a very small and simple idea but I couldn't find anything like it so I made it myself.

## Installation

Install with `pip install flask-error-templating`.

## Usage

```python
create_http_error_handlers(app, error_pages, page_template_file, **kwargs)
```

#### Parameters

###### app
`app` is a handle to your `Flask` object. Need I write more?

###### error_pages

`error_pages` is a list of `ErrorPage` objects. It accepts three arguments: `error_code`, `message` and `long_message`. `error_code` and `message` are required; `long_message` is optional and if it is not present then it will not be rendered into the template. Note that it's possible to have some `ErrorPage` objects with `long_message` set and others without.

Example of `error_pages`:
```python
error_pages = [
    ErrorPage(400, 'Bad request'),
    ErrorPage(400, 'Access is denied to this page.'),
    ErrorPage(403, 'You are forbidden to view this page.',
        'A very long message that we also want to display in the long_message field'),
    ErrorPage(404, 'The page you are looking for does not exist'),
    ErrorPage(418, 'I\'m a teapot!')
]
```

###### page_template_file

`page_template_file` is the filename of a HTML file in your projects `templates` folder. Parameters supplied to the file for template rendering are `error_code`, `message` and `long_message`. See the above paragraph for information on these parameters. If `long_message` is not present then an empty string will be rendered in its place - this allows the same template to serve pages with long message and also without.

Example of `page_template_file`:
```html
<!DOCTYPE html>
<html>
    <body>
        <h1>{{ error_code }}</h1>
        <h2>{{ message }}</h2>
        <br>
        <p>{{ long_message }}</p>
    </body>
</html>
```

###### keyword arguments

Often, you will want to pass things like the name of your app to the template when it is being rendered. To allow passing this value, all keyword arguments after `page_template_file` will be passed to Flask's `render_template()` function.

#### Complete basic example:
```python
from flask import *
from flask_error_templating import ErrorPage, create_http_error_handlers

app = Flask(__name__)

@app.route('/')
def homepage():
    return '<h1>Homepage</h1>'

error_pages = [
    ErrorPage(400, 'Bad request'),
    ErrorPage(400, 'Access is denied to this page.'),
    ErrorPage(403, 'You are forbidden to view this page.',
        'A very long message that we also want to display in the long_message field'),
    ErrorPage(404, 'The page you are looking for does not exist'),
    ErrorPage(418, 'I\'m a teapot!')
]
create_http_error_handlers(app, error_pages, 'http_error.html', app_name='Some testing app')

if __name__ == '__main__':
    app.run()
```