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


@app.route("/login", methods=["POST"])
def login():
    login = request.form.get('login')
    password = request.form.get('password')
    # user = User.query.filter_by(login=login, password=password).first()
    query = f"SELECT * FROM User WHERE login='{login}' and password='{password}'"
    user = db.engine.execute(query).first()
    if user:
        return f'Logged in as {user.login}'
    return 'Invalid credentials'


if __name__ == "__main__":
    # user = User(login='admin2', password='qwerty2')
    # db.session.add(user)
    # db.session.commit()
    app.run('127.0.0.1', '8888')