import requests

end_point = "http://localhost:8000/api/product/list-create/" 

#GET:
# get_response = requests.get(end_point)

#POST:
get_response = requests.post(end_point, json={"title": "list-create_api_title_obj"})
print(get_response.json())