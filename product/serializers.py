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
            
            # do this or next if
            if not hasattr(obj, 'id'):
                 return None
            
            # do previous if or this one
            if not isinstance(obj,models.Product):
                 return None

            return obj.get_discounted_price
    