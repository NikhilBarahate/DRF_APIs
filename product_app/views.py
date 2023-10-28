from product_app.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product_app.serializers import ProductSerializer
from rest_framework import status


@api_view(["POST"])
def model_instance_view(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        # data = serializer.save()
        # print(data)
        print(serializer.data)
        return Response(serializer.data)
    # return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    # return Response({"invalid data:": "Not a good Data"}, status=status.HTTP_400_BAD_REQUEST)
