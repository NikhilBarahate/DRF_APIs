import requests

end_point = "http://localhost:8000/api/"  #http://127.0.0.1:8000/

get_response = requests.get(end_point, json={"query": "hello request"}, params={"product_id": 123}) 

print(get_response.json())
print(get_response.status_code)
