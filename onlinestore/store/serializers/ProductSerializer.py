from rest_framework import serializers

class CreateProductRequest(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.FloatField()
    store_id = serializers.IntegerField()

    def get_name(self):
        return self.validated_data.get('name')

    def get_price(self):
        return self.validated_data.get('price')

    def get_store_id(self):
        return self.validated_data.get('store_id')

class ListProductsResponse:
    PRODUCT_ID = 'id'
    PRODUCT_NAME = 'name'
    PRODUCT_PRICE = 'price'