from flask import Flask
from flask import jsonify
from flask import request
import math
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#create a flask route and method to verify if a given number is prime and even
@app.route('/is_prime/<int:number>')
def is_prime(number):
    prime = True
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                prime = False
                break
    else:
        prime = False
    return jsonify({"is_prime": prime})


#create a flask route and method to check if given zipcode is valid in US or not
@app.route('/zipcode/<zipcode>')
def zipcode(zipcode):
    if len(zipcode) == 5:
        if zipcode.isdigit():
            return jsonify({"valid": True})
        else:
            return jsonify({"valid": False})
    else:
        return jsonify({"valid": False})


#create a flask route and method to check if a given string contains digits
@app.route('/has_digits/<string:word>')
def has_digits(word):
    return str(any(char.isdigit() for char in word))
#create a flask route and method to output if roots of a Quadratic equation are real or imaginary  and the number of roots
#https://beta.openai.com/playground/p/vuxYLaARAevZORZv4yHS4383?model=davinci-codex
@app.route('/quadratic/<a>/<b>/<c>')
def quadratic(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    d = b**2 - 4*a*c
    if d < 0:
        return "This equation has imaginary roots"
    elif d == 0:
        x = (-b + math.sqrt(d)) / (2 * a)
        return "This equation has one real root: " + str(x)
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return "This equation has two real roots: " + str(x1) + ", " + str(x2)
