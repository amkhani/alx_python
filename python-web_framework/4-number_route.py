
"""
models number route
~~~~~~~~~~~~~

"""

from flask import Flask, escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def show_c_text(text):
    processed_text = escape(text).replace('_', ' ')
    return f"C {processed_text}"

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python_text(text):
    processed_text = escape(text).replace('_', ' ')
    return f"Python {processed_text}"

@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    return f"{n} is a number"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
