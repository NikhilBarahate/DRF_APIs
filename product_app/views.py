from product_app.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product_app.serializers import ProductSerializer
from rest_framework import status, generics
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import mixins


class ProductMixinView(
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):  #HTTP--->get
        pk = kwargs.get("pk")
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")
        if not content:
            content = "mixin view performing perform_create action"
        
        serializer.save(content=content)
    

    # We can Write any method to overide any other method by returning that method 
    # def post(self, request, *args, **kwargs):  #HTTP--->post
    #     return self.list(request, *args, **kwargs)


    
