from product_app.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product_app.serializers import ProductSerializer
from rest_framework import status, generics
from django.http import Http404
from django.shortcuts import get_object_or_404


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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

product_create_apiview = ProductCreateAPIView.as_view()



class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_apiview = ProductListAPIView.as_view()


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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




class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

        # content = serializer.validated_data.get("content")
        # title = serializer.validated_data.get("title")
        # if not content:
        #     content = title
        # serializer.save(content=content)
        # return super().perform_update(serializer)


product_update_apiview = ProductUpdateAPIView.as_view()


class ProductDestroyPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


product_destroy_apiview = ProductDestroyPIView.as_view()



# Function Based :
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk:
            # queryset = Product.objects.filter(pk=pk)
            # if not queryset.exists():
            #     raise Http404
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if not content:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "Not a good data."}, status=status.HTTP_400_BAD_REQUEST)
    