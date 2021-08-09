from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

db.create_all()

@app.route("/", methods=["GET"])
def hello():
    hello = request.args.get('hello')
    if hello:
        return "Hello World!"
    else:
        return 'Bye World!'


@app.route('/login', methods=["GET"])
def login_page():
    return '''<!DOCTYPE html>
<html>
<body>

<h2>Login Panel</h2>

<form action="/login" method="POST">
  <label for="login">Login:</label><br>
  <input type="text" id="login" name="login"><br>
  <label for="password">Password:</label><br>
  <input type="password" id="password" name="password"><br><br>
  <input type="submit" value="Submit">
</form> 

</body>
</html>'''

@app.route("/login", methods=["POST"])
def login():
    login = request.form.get('login')
    password = request.form.get('password')
    user = User.query.filter_by(login=login, password=password).first()
    if user:
        return f'''<!DOCTYPE html>
<html>
<head>
<title>Login</title>
</head>
<body>

<h1>Success!</h1>
<p>Logged in as {user.login}.</p>

</body>
</html>'''
    return f'''<!DOCTYPE html>
<html>
<head>
<title>Login</title>
</head>
<body>

<h1>Login failed.</h1>
<p>Invalid credentials</p>

</body>
</html>'''


if __name__ == "__main__":
    app.run('127.0.0.1', '8888')