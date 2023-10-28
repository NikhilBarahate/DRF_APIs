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
        # print("self:", self)
        # print("obj:", obj.id)
        # return obj.price  # you can acces the obj.user --> user.username
        return obj.get_discount()
