@app.route('/is-even/<int:number>')
def is_even(number):
    return f'{number} is {"even" if number % 2 == 0 else "odd"}'