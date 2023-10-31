from flask import Flask, request, jsonify
import json
import predict

app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/predict', methods=['POST'])
def get_prediction():


    # Validate input
    if 'Administrative' not in request.json:
        return "Administrative required", 400     

    try:
        data = request.get_json()
    except:
        return "Error parsing input JSON", 400

    data = json.loads(data)
    # Validate and parse fields
    try:
        administrative = int(data['Administrative'])
        product_related = int(data['ProductRelated'])
        product_duration = int(data['ProductRelated_Duration'])
        bounce_rates = int(data['BounceRates'])
        exit_rates = int(data['ExitRates'])
        page_values = int(data['PageValues'])
        month = int(data['Month'])
        visitor_type = int(data['VisitorType'])
    except ValueError:
        return "Invalid input data types", 400

    try:
        # Make prediction
        result = predict.predict(administrative, product_related,  
                                 product_duration, bounce_rates,
                                 exit_rates, page_values, month,
                                 visitor_type)
    except Exception as e:
                return "Prediction failed", 500

    return jsonify(result)
    
if __name__ == '__main__':
    app.run(debug=True)