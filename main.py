from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/reverse', methods=['GET'])
# Route to reverse a given name
# Input: name (string) - The name to be reversed
# Output: reversed_name (string) - The reversed name
def reverse_name():
    name = request.args.get('name')
    reversed_name = name[::-1]
    return name + reversed_name

@app.route('/add', methods=['GET'])
# Route to add a random number to a given number
# Input: number (string) - The number to be added to
# Output: result (string) - The sum of the given number and a random number
def add_random_number():
    number = request.args.get('number')
    random_number = random.randint(1, 10)
    result = int(number) + random_number
    return str(result)

if __name__ == '__main__':
    app.run()