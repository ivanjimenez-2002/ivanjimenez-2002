from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    sqft = float(request.form['sqft'])
    landsqft = float(request.form['landsqft'])
    neighbors = int(request.form['neighbors'])
    stories = int(request.form['stories'])
    pools = int(request.form['pools'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    response = jsonify({
        'estimated_price': util.get_estimated_price(sqft, landsqft, neighbors, stories, pools, bedrooms, bathrooms)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)