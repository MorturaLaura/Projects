from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_neighborhood_names', methods=['GET'])
def get_neighborhood_names():
    response = jsonify({
        'neighborhood': util.get_neighborhood_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_new_building_names', methods=['GET'])
def get_new_building_names():
    response = jsonify({
        'new_building': util.get_new_building_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_partitioning_names', methods=['GET'])
def get_partitioning_names():
    response = jsonify({
        'partitioning': util.get_partitioning_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_rooms_names', methods=['GET'])
def get_rooms_names():
    response = jsonify({
        'rooms': util.get_rooms_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_floor_names', methods=['GET'])
def get_floor_names():
    response = jsonify({
        'floor': util.get_floor_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_rent_price', methods=['GET', 'POST'])
def predict_rent_price():
    neighborhood = request.form.get('neighborhood')
    partitioning = request.form.get('partitioning')
    new_building = request.form.get('new_building')
    space = float(request.form.get('space'))
    floor = request.form.get('floor')
    rooms = request.form.get('rooms')

    response = jsonify({
        'estimated_rent_price': util.get_estimated_rent_price(neighborhood, partitioning, new_building, space, floor, rooms)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print('Starting Python Flask Server For Rent Price Prediction ... ')
    util.load_saved_artifacts()
    app.run()
