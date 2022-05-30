"""A demo to get start with flask framework."""
from flask import Flask


def celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return fahrenheit


app = Flask(__name__)


# Setup app's route
@app.route('/f')
@app.route('/f/<celsius>')
def greet(celsius=""):
    """Return a string message with helpful text and show the celsius - fahrenheit converting."""
    message = f"<h1>Celsius of {celsius} to fahrenheit is " \
              f"{str(celsius_to_fahrenheit(celsius))}</h1>"
    return message


if __name__ == '__main__':
    app.run()
