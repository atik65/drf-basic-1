from rest_framework import serializers
from . import models

class ProductSerializer(serializers.ModelSerializer):

    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Product
        fields = [
       
            'id',
            'name',
            'price',
            'discount'
        ]

    def get_discount(self,obj):
            return obj.get_discounted_price
    