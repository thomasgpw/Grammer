import logging
import logging.handlers

from wsgiref.simple_server import make_server
from flask import Flask
from flask import render_template

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Handler 
LOG_FILE = 'log/app.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add Formatter to Handler
handler.setFormatter(formatter)

# add Handler to Logger
logger.addHandler(handler)

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
@application.route('/')
def welcome():
  return render_template('welcome.html')

# add a rule when the page is accessed with a name appended to the site
# URL.
@application.route('/<username>')
def search_username():
  return render_template('welcome.html', username=username)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

# def application(environ, start_response):
#     path    = environ['PATH_INFO']
#     method  = environ['REQUEST_METHOD']
#     if method == 'POST':
#         try:
#             if path == '/':
#                 request_body_size = int(environ['CONTENT_LENGTH'])
#                 request_body = environ['wsgi.input'].read(request_body_size).decode()
#                 logger.info("Received message: %s" % request_body)
#             elif path == '/scheduled':
#                 logger.info("Received task %s scheduled at %s", environ['HTTP_X_AWS_SQSD_TASKNAME'], environ['HTTP_X_AWS_SQSD_SCHEDULED_AT'])
#         except (TypeError, ValueError):
#             logger.warning('Error retrieving request body for async work.')
#         response = ''
#     else:
#         response = welcome
#     status = '200 OK'
#     headers = [('Content-type', 'text/html')]

#     start_response(status, headers)
#     return [response]


# if __name__ == '__main__':
#     httpd = make_server('', 8000, application)
#     print("Serving on port 8000...")
#     httpd.serve_forever()
