from flask import Flask, jsonify, render_template, request
import itertools
import json
import math

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


# root endpoint
@app.route('/')
def home():
    return render_template('index.html')


# GET /coins
@app.route('/coins')
def get_stores():
    possible_combinations = []
    combination_count = 0

    for quarter_count in range(4+1):
        for dime_count in range(10+1):
            for nickel_count in range(20+1):
                for penny_count in range(100+1):
                    if 25*quarter_count + 10*dime_count + 5*nickel_count + penny_count == 100:
                        possible_combinations.append({'quarters': quarter_count, 'dimes': dime_count,
                                                      'nickels': nickel_count, 'pennies': penny_count})
                        combination_count = combination_count + 1

    return jsonify({'count': combination_count, 'combinations': possible_combinations})


# GET /demo
@app.route('/demo')
def get_demo():
    with open("denomination_values.txt", "r") as read_file:
        lines = read_file.readlines()

        if len(lines) % 2 == 0:
            even = []
            odd = []
            count = 0
            while count < len(lines):
                if count % 2 == 0:
                    lines[count] = lines[count].strip('\n')
                    even.append(lines[count])
                else:
                    odd.append(lines[count])
                count += 1

            ranges = []
            for i in odd:
                i = math.floor(float(i))
                ranges.append(range(i + 1))

            highest = 0
            while_counter = 0
            while while_counter < len(odd):
                for j in odd:
                    if math.floor(float(j)) > float(highest):
                        highest = j
                while_counter += 1

            calculated_array = []
            for i in odd:
                i = float(i)
                value = float(highest) / i
                calculated_array.append(value)

            possible_total_combinations = []
            combo_count = 0

            for xs in itertools.product(*ranges):
                products = []
                for x, y in zip(calculated_array, xs):
                    products.append(x * y)

                if len(products) == len(odd):
                    product_sum = 0
                    for p in products:
                        product_sum = product_sum + p
                if product_sum == float(highest):
                    data = {}
                    final_count = 0
                    while final_count < len(odd):
                        data[even[final_count]] = xs[final_count]
                        final_count += 1
                    json_data = json.loads(json.dumps(data))
                    possible_total_combinations.append(json_data)
                    combo_count += 1

            return jsonify({'count': combo_count, 'combinations': possible_total_combinations})

        else:
            return jsonify({'message': 'some values are missing from the input file'})


app.run(port=5000)
