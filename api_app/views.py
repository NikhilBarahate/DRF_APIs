import json
from django.http import JsonResponse

def first_api_view(request, *args, **kwargs):

    # print(dir(request)) # Http Request of Django
    print(request.body) # byte string of json data
    # return JsonResponse({"message": "hi there, This is the Django APIs Response..."})
    
    print(request.GET)  #URL Querry Params
    print(request.POST)
    data = {}
    try:
        data = json.loads(request.body) # string of json data --> python dict
    except:
        pass
    print(data)
    data["params"] = dict(request.GET)
    print(data["params"])
    data["headers"] = dict(request.headers)  # request.META
    data["content_type"] = request.content_type
    return JsonResponse(data)
