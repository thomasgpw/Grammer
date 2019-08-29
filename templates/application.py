import logging
import logging.handlers

from wsgiref.simple_server import make_server


# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Handler 
LOG_FILE = '/opt/python/log/sample-app.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add Formatter to Handler
handler.setFormatter(formatter)

# add Handler to Logger
logger.addHandler(handler)

welcome = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <title>Welcome</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  <style>
  body {
    color: #ffffff;
    font-family: Arial, sans-serif;
    font-size:14px;
    -moz-transition-property: text-shadow;
    -moz-transition-duration: 4s;
    -webkit-transition-property: text-shadow;
    -webkit-transition-duration: 4s;
    text-shadow: none;
  }
  body.blurry {
    -moz-transition-property: text-shadow;
    -moz-transition-duration: 4s;
    -webkit-transition-property: text-shadow;
    -webkit-transition-duration: 4s;
    text-shadow: #fff 0px 0px 25px;
  }
  a {
    color: #0188cc;
  }
  .textColumn {
    position: absolute;
    top: 0px;
    right: 50%;
    bottom: 0px;
    left: 0px;

    text-align: right;
    padding-top: 11em;
    background-color: #1BA86D;
    background-image: -moz-radial-gradient(left top, circle, #6AF9BD 0%, #00B386 60%);
    background-image: -webkit-gradient(radial, 0 0, 1, 0 0, 500, from(#6AF9BD), to(#00B386));
  }
  .menuBar {
    position: absolute;
    top:0px;
    left: 0px;
    right:0px;
    height: 8%;
    background-color: #E0E0E0;
  }
  .content {
    position: absolute;
    top: 8%;
    right: 0px;
    bottom: 0px;
    left:0px;
    overflow: hidden;
  }
  .icon {
    margin: 15px;
    height: 50px;
    width: 50px;
    border-radius: 50%;
  }
  </style>
</head>
<body id="sample">
  <nav class="navbar navbar-expand-lg navbar-light bg-light d-flex justify-content-end">
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </nav>
  <div>
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col"></th>
          <th scope="col">Username</th>
          <th scope="col">Full Name</th>
          <th scope="col">URL</th>
          <th scope="col">Bio</th>
          <th scope="col">Posts</th>
          <th scope="col">Followers</th>
          <th scope="col">Following</th>
        </tr>
      </thead>
      <tbody>
        <tr scope="row" onclick="window.location='https://instagram.com/the_realest_kyle';">
          <td><img class="icon" src="assets/kyleicon.jpg"></td>
          <td>the_realest_kyle</td>
          <td>Kyle Stephens</td>
          <td>https://instagram.com/the_realest_kyle</td>
          <td>My name is Kyle.</td>
          <td>32</td>
          <td>272</td>
          <td>454</td>
        </tr>
        <tr scope="row" onclick="window.location='https://instagram.com/livelaughgrub';">
          <td><img class="icon" src="assets/grubicon.jpg"></td>
          <td>livelaughgrub</td>
          <td></td>
          <td>https://instagram.com/livelaughgrub</td>
          <td>Just eating my way through the 🌎</td>
          <td>68</td>
          <td>321</td>
          <td>427</td>
        </tr>
        <tr scope="row" onclick="window.location='https://instagram.com/toronto_food.tours';">
          <td><img class="icon" src="assets/torontoicon.jpg"></td>
          <td>toronto_food.tours</td>
          <td>Toronto Foodie And Food Tours</td>
          <td>https://instagram.com/toronto_food.tours</td>
          <td>Toronto Food Tours🔥 my name is Alex and I take people through the city showing off the best restaurants and dishes Toronto has to offer💯💯</td>
          <td>10</td>
          <td>1530</td>
          <td>2118</td>
        </tr>
        <tr scope="row" onclick="window.location='https://instagram.com/imafoodpiggie';">
          <td><img class="icon" src="assets/piggieicon.jpg"></td>
          <td>imafoodpiggie</td>
          <td></td>
          <td>https://instagram.com/imafoodpiggie</td>
          <td>Life of two hungry piggies🐷</td>
          <td>9</td>
          <td>776</td>
          <td>750</td>
        </tr>
        <tr scope="row" onclick="window.location='https://instagram.com/foodwithemmanbrooklyn';">
          <td><img class="icon" src="assets/emmaicon.jpg"></td>
          <td>foodwithemmanbrooklyn</td>
          <td>Brooklyn + Emma</td>
          <td>https://instagram.com/foodwithemmanbrooklyn</td>
          <td>📍Toronto<br>📨 DM for collabs and more!<br>🤠 @_brooklynwong @_emma_feng_</td>
          <td>15</td>
          <td>141</td>
          <td>68</td>
        </tr>
        <tr scope="row" onclick="window.location='https://instagram.com/the.scientific.philosopher';">
          <td><img class="icon" src="assets/scienceicon.jpg"></td>
          <td>the.scientific.philosopher</td>
          <td>Science & Such | 📚</td>
          <td>https://instagram.com/the.scientific.philosopher</td>
          <td>Some scientific philosophy and philosophical science for all you lovely lovers of wisdom 🤔🌌<br>scientificphilosopher.tumblr.com</td>
          <td>129</td>
          <td>757,194</td>
          <td>293</td>
        </tr>
        <tr scope="row" onclick="window.location='https://instagram.com/theellenshow';">
          <td><img class="icon" src="assets/ellenicon.jpg"></td>
          <td>theellenshow</td>
          <td>Ellen DeGeneres</td>
          <td>https://instagram.com/theellenshow</td>
          <td>@theellenfund<br>@ellentube<br>@edbyellen<br>@theellenshop<br>ellentube.com</td>
          <td>7731</td>
          <td>76,472,944</td>
          <td>369</td>
        </tr>
      </tbody>
    </table>
  </div>
</body>
</html>
"""

def application(environ, start_response):
    path    = environ['PATH_INFO']
    method  = environ['REQUEST_METHOD']
    if method == 'POST':
        try:
            if path == '/':
                request_body_size = int(environ['CONTENT_LENGTH'])
                request_body = environ['wsgi.input'].read(request_body_size).decode()
                logger.info("Received message: %s" % request_body)
            elif path == '/scheduled':
                logger.info("Received task %s scheduled at %s", environ['HTTP_X_AWS_SQSD_TASKNAME'], environ['HTTP_X_AWS_SQSD_SCHEDULED_AT'])
        except (TypeError, ValueError):
            logger.warning('Error retrieving request body for async work.')
        response = ''
    else:
        response = welcome
    status = '200 OK'
    headers = [('Content-type', 'text/html')]

    start_response(status, headers)
    return [response]


if __name__ == '__main__':
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()
