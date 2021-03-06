from flask import Flask
from flask import jsonify
from flask import request
import math
import regex as re

# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1> Welcome to API server of CODELESS APP DEV </h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)


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


#create a flask route and method to check if a given string is a palindrome
@app.route('/palindrome/<string:word>')
def palindrome(word):
    return str(word == word[::-1])

@app.route('/isDivisibleBy19/<int:number>')
def isDivisibleBy19(number):
    if number % 19 == 0:
        return '{} is divisible by 19'.format(number)
    else:
        return '{} is not divisible by 19'.format(number)


@app.route('/is_email/<email>')
def is_email(email):
    if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return '{} is a valid email'.format(email)
    else:
        return '{} is not a valid email'.format(email)
 

@app.route('/evenDigits/<int:num>')
def evenDigits(num):
    count = 0
    for i in str(num):
        if int(i) % 2 == 0:
            count += 1
    return str(count)

@app.route('/is_leap_year/<int:year>')
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return str(year) + ' is a leap year'
            else:
                return str(year) + ' is not a leap year'
        else:
            return str(year) + ' is a leap year'
    else:
        return str(year) + ' is not a leap year'




@app.route('/is-divisible-by-11/<int:number>')
def is_divisible_by_11(number):
    return str(number % 11 == 0)


@app.route('/isDivBy21/<int:num>')
def isDivBy21(num):
    if num % 21 == 0:
        return '{} is divisible by 21'.format(num)
    else:
        return '{} is not divisible by 21'.format(num)

