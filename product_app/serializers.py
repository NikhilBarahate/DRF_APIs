from rest_framework import serializers 
from product_app.models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "price",
            "sale_price",
            "get_discount",
            "my_discount"
        ]

    def get_my_discount(self, obj):
        # try:
        #     return obj.get_discount()
        # except:
        #     return None

        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()