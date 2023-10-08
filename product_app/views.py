import json
from product_app.models import Product
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

def model_instance_view(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        """Same as model_to_dict() """
        # data["id"] = model_data.id
        # data["title"] = model_data.title
        # data["content"] = model_data.content
        # data["price"] = model_data.price

        # data = model_to_dict(model_data)
        data = model_to_dict(model_data, fields=["id", "title"])
        json_data_str = json.dumps(data)
        
    # return HttpResponse(data)
    # return HttpResponse(json_data_str)
    return HttpResponse(json_data_str, headers={"content-type": "application/json"})
    return JsonResponse(data)

