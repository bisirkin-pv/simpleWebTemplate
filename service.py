from flask import Flask, request
from apis import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)


@app.route("/rpc")
def rpc():
    return "<h1>Hello There!</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')