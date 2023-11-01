import requests

end_point = "http://localhost:8000/api/product/4/update/" 

data = {
    "title": "updated hello",
    "price": 101
}

get_response = requests.put(end_point, json=data) 
print(get_response.json())