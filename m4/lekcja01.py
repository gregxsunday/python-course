from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    # print(request.headers)
    hello = request.args.get('hello')
    if hello:
        return "Hello World!"
    else:
        return 'Bye World!'


@app.route("/login", methods=["POST"])
def test():
    login = request.form.get('login')
    password = request.form.get('password')
    if login == 'admin' and password == 'qwerty':
        return f'Logged in as {login}'
    return 'Invalid credentials'


if __name__ == "__main__":
    app.run('127.0.0.1', '8888')