from product_app.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product_app.serializers import ProductSerializer
from rest_framework import status, generics
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, authentication

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.DjangoModelPermissions]
    

    def perform_create(self, serializer):
        # we can update the data and validate data
        # serializer.save(user=self.request.user)
        print(serializer)
        print(serializer.validated_data)

        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if not content:
            content = title
        serializer.save(content=content)
        # send a Django signal

product_list_create_apiview = ProductListCreateAPIView.as_view()