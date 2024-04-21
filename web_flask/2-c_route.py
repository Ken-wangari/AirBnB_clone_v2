from flask import Flask

app = Flask(__name__)

def hello_hbnb():
    """ Prints a Message when / is called """
    return 'Hello HBNB!'

def hbnb():
    """ Prints a Message when /hbnb is called """
    return 'HBNB'

def c_is_fun(text):
    """ Prints a Message when /c is called """
    return "C " + text.replace('_', ' ')

app.add_url_rule('/', 'hello_hbnb', hello_hbnb)
app.add_url_rule('/hbnb', 'hbnb', hbnb)
app.add_url_rule('/c/<text>', 'c_is_fun', c_is_fun)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

