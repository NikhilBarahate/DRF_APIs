import json
from product_app.models import Product
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from product_app.serializers import ProductSerializer


@api_view(["GET", "POST"])
def model_instance_view(request, *args, **kwargs):
    """
    DRF API View
    """
    # if request.method != "POST":
    #     return Response({"details:":"GET method is not Allowed"}, status=405)
    # model_data = Product.objects.all().order_by("?").first()
    instance = Product.objects.all().order_by("?").first()

    data = {}
    if instance:   
        # data = model_to_dict(instance, fields=["id", "title", "price", "sales_price"])
        data = ProductSerializer(instance).data
    return Response(data)
