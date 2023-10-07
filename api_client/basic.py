import requests

end_point = "https://httpbin.org/anything"

# get_response = requests.get(end_point, json={"query": "hello request"}) # json = data attributes, 'Content-Type': 'application/json'
get_response = requests.get(end_point, data={"query": "hello request"}) # data = form attributes, 'Content-Type': 'application/x-www-form-urlencoded'

# print(get_response.text) # print raw text
print(get_response.json()) # javascripts object notation = python dict
print(get_response.status_code)
