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




@app.route('/is_prime/<int:number>')
def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return str(number) + " is not a prime number"
                break
        else:
            return str(number) + " is a prime number"
    else:
        return str(number) + " is not a prime number"


@app.route('/is_valid', methods=['POST'])
def is_valid():
    email = request.get_json()
    if re.match(r"[^@]+@[^@]+\.[^@]+", email['email']):
        return jsonify({'email': email['email'], 'valid': True})
    return jsonify({'email': email['email'], 'valid': False})


@app.route('/is_prime/<int:number>')
def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return str(number) + " is not a prime number"
                break
        else:
            return str(number) + " is a prime number"
    else:
        return str(number) + " is not a prime number"

