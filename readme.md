### <ins> Python Flask Web Application </ins>

Python Flask is a web framework that is used to build web applications <br>
It is a lightweight WSGI web application framework <br>
It is designed to make getting started quick and easy, with the ability to scale up to complex applications <br>
It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks <br>

### <ins> Installation </ins> <br>

Command: _pip install Flask_ <br>

### <ins> Basic Setup </ins> <br>

```
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5000)
```

### <ins> Routing </ins> <br>

Routing is used to map URLs to functions <br>
It is used to define the URL patterns and the functions that should be called for each pattern <br>

```
@app.route('/')
def home():
    return 'Hello, World!'
```

<ins> Generic Routing </ins> <br>

Generic routing is used to pass the URL parameters to the function <br>
The parameters are passed as arguments to the function <br>

```
@app.route('/<name>')
def home(name):
    return f'Hello {name}'
```

<ins> Redirects </ins> <br>

Redirects are used to redirect the user to a different URL <br>

```
@app.round('/admin')
def admin():
    if is_administrator():
        return f'This is Admin Page'
    else:
        return redirect(url_for('home'))
```

<ins> Forward Slash Access </ins> <br>

Forward slash access is used to access the URL with or without the forward slash <br>

```
# W/O Forward Slash
@app.route('/page')
def page():
    return 'This is Page'

# W/ or W/O Forward Slash
@app.route('/page/')
def page():
    return 'This is Page'
```

### <ins> Templates (Render HTML) </ins> <br>

Templates are used to render HTML pages <br>
It is used to separate the HTML code from the Python code <br>

```
from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder='templates'
)

@app.route('/')
def home():
    return render_template('home.html')
```

### <ins> Static Files </ins> <br>

Static files are used to store the CSS, JavaScript, and images <br>
It is used to separate the static files from the Python code <br>

```
app = Flask(
    __name__,
    static_folder='static',
    template_folder='templates'
)
```

### <ins> Pass Information to Templates </ins> <br>

Information can be passed to the templates using the render_template function <br>

```
# index.html

<!DOCTYPE html>
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
        <h1>{{ message }}</h1>
    </body>
</html>

- - - - - - - - - -

# app.py

@app.route('/')
def home():
    return render_template('index.html', title='Home', message='Hello World!')
```

### <ins> Auto Detect Changes - Debug Mode </ins> <br>

Debug mode is used to auto-detect the changes in the code <br>
It is used to auto-reload the server when the code changes <br>

```
app.run(port=5000, debug=True)
```

### <ins> App Secret Key </ins> <br>

The secret key is used to secure the session data <br>

```
app.secret_key = os.urandom(24)

# or

app.config['SECRET_KEY'] = os.urandom(24)
```

### <ins> CRUD Operations </ins> <br>

CRUD stands for Create, Read, Update, and Delete <br>
It is used to perform the database operations <br>

```
# Create
@app.route('/create', methods=['POST'])
def create():
    print('Created !')

# Read
@app.route('/read', methods=['GET'])
def read():
    print('Read !')

# Update
@app.route('/update', methods=['PUT'])
def update():
    print('Updated !')

# Delete
@app.route('/delete', methods=['DELETE'])
def delete():
    print('Deleted !')
```

<ins> Multiple Methods </ins> <br>

Multiple methods can be used for the same URL <br>

```
@app.route('/crud', methods=['POST', 'GET'])
def crud():
    if request.method == 'POST':
        print('Created !')
    elif request.method == 'GET':
        print('Read !')
```

### <ins> Sessions </ins> <br>

Sessions are used to store the user data <br>
It is used to store the user data across the requests <br>

```
from flask import Flask, session

app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/login')
def login():
    session['user'] = 'admin'
    return 'Logged In'
```

<ins> Clear Session </ins> <br>

The session data can be cleared using the pop method <br>

```
@app.route('/logout')
def logout():
    session.clear()
    return 'Logged Out'
```

### <ins> Cookies </ins> <br>

Cookies are used to store the user data on the client side <br>

```
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/cookie')
def cookie():
    response = make_response('Cookie')
    response.set_cookie('user', 'admin')
    return response
```

<ins> Clear Cookie </ins> <br>

The cookie data can be cleared using the set_cookie method <br>

```
@app.route('/clear')
def clear():
    response = make_response('Cookie Cleared')
    response.set_cookie('user', '', expires=0)
    return response
```

### <ins> Error Handling </ins> <br>

Error handling is used to handle the errors in the application <br>

```
@app.errorhandler(404)
def not_found(error):
    return 'Not Found', 404
```

### <ins> Blueprints </ins> <br>

Blueprints are used to organize the application into components <br>

```
# admin.py
from flask import Blueprint

ADMIN = Blueprint('admin', __name__)

@admin.route('/')
def home():
    return 'Admin Page'
    
- - - - - - - - - -

# app.py

# BLUEPRINTS
from admin import admin
```

### <ins> Custom Flask - Recommendations </ins> <br>

<ins> API Authentication </ins> <br>

```
from flask import session


def api_auth(api):
    def wrapper(*args, **kwargs):
        # Authorised
        if 'client_id' in session:
            ret = api(*args, **kwargs)
            return ret
        # Unauthorised
        else:
            return 'Unauthorised', 401

    # Rename (Avoid func mapping overwriting error)
    wrapper.__name__ = api.__name__
    return wrapper
```

<ins> Router </ins> <br>

```
# router.py

from flask import Blueprint, render_template, send_from_directory, session
from properties import Properties

# BLUEPRINT
Router = Blueprint('Router', __name__)

# APIs
def render_route(route):
    if not route.startswith('api'):
        return render_template('index.html')  # FE Preparation
    return {}

# Pages
@Router.route('/', defaults={'path': ''})
@Router.route('/<path:path>')
def router(path):
    if path == '':
        session.clear()
    elif path in [/home', '/about', '/contact']:
        return render_route(path)
    return {'error': {'message': 'page not found'}}, 404
```