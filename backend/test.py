import json 
import requests
# Input values 
admin = 100
product_related = 10 
product_duration = 999
bounce_rate = 1234
exit_rate = 0.8
page_values = 12
month = 11
visitor_type = 1

# Create input data JSON
input_data = {
   "Administrative": admin,
   "ProductRelated": product_related,
   "ProductRelated_Duration": product_duration,
   "BounceRates": bounce_rate,
   "ExitRates": exit_rate,
   "PageValues": page_values,
   "Month": month,
   "VisitorType": visitor_type
}

# Convert to JSON string 
input_json = json.dumps(input_data)

headers = {'Content-Type': 'application/json'}

# POST request
response = requests.post('http://localhost:5000/predict', json=input_json, headers=headers)

# Print response 
print(response.text)