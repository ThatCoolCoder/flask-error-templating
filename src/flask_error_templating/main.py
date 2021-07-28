from dataclasses import dataclass

from flask import Flask, render_template

@dataclass
class ErrorPage:
    error_code: int
    message: str
    long_message: str = None

class HttpErrorHandler:
    def __init__(self, app: Flask, error_page: ErrorPage,
        page_template_file: str, template_arguments={}):

        # Register this object to be a handler
        app.register_error_handler(error_page.error_code, self)

        # Render the template now so that we don't have to do it every time
        # that there is a request
        template_options = {
            'error_code' : error_page.error_code,
            'message' : error_page.message,
            **template_arguments
        }
        if error_page.long_message is None:
            template_options['long_message'] = ''
        else:
            template_options['long_message'] = error_page.long_message
        with app.app_context():
            self.rendered_template = render_template(page_template_file,
                **template_options)
    
    def __call__(self, *args, **kwargs):
        return self.rendered_template

def create_http_error_handlers(app: Flask, error_pages: list,
    page_template_file, **kwargs) -> None:
    '''Main function of this package.
    Create error handlers for each item in error_page_data

    @app: your Flask application

    @error_pages: a list of ErrorPage objects

    @page_template_file: name of the file (in the project's template folder)
        to be used for rendering the templates. The file must have all of the fields of
        an ErrorPage object.
        
    All following arguments will be passed to Flask render_template()
    '''
    for page in error_pages:
        HttpErrorHandler(app, page, page_template_file, kwargs)