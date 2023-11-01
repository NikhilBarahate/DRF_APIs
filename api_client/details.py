import requests

end_point = "http://localhost:8000/api/product/4/" 

get_response = requests.get(end_point) 
print(get_response.json())
