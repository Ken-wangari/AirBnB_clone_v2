from flask import Flask

app = Flask(__name__)


def hello_route():
    """
    Displays 'Hello HBNB!'
    Returns:
        str: "Hello HBNB"
    """
    return "Hello HBNB!"


app.add_url_rule('/', 'hello_route', hello_route)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

