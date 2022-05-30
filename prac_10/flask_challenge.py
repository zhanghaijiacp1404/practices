"""A demo to get start with flask framework that call python functions."""
from flask import Flask


def celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return fahrenheit


app = Flask(__name__)


# Setup app's routes and their corresponding web content
@app.route("/")
def welcome():
    """Return a string welcome message with guidance."""
    return "<h1>Welcome to Celsius to Fahrenheit Demo Web! " \
           "Enter \"f\" at the end the route to see more information</h1>"


@app.route('/f')
def promote_user():
    """Return a string guidance message."""
    return "<h1>Add \"/(celsius)\" at the end of route to see your convention result!</h1>"


@app.route('/f/<celsius>')
def convert(celsius=""):
    """
    Return a string message with helpful text and
    show the result on webpage for celsius - fahrenheit
    converting.
    """
    return f"<h1>Celsius of {celsius} to fahrenheit is " \
           f"{str(celsius_to_fahrenheit(celsius))}</h1>"


if __name__ == '__main__':
    app.run()
