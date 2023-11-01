import requests

end_point = "http://localhost:8000/api/product/create/" 

data = {
    "title": "New title having same content",
    "price": 200
}

get_response = requests.post(end_point, json=data) 
print(get_response.json())