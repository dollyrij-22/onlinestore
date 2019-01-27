from rest_framework import serializers

class ProductListFields:
    ID_FIELD = 'id'
    QUANTITY_FIELD = 'quantity'
    PRICE_FIELD = 'price'

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setQuantity(self, quantity):
        self.quantity = quantity

    def getQuantity(self):
        return self.quantity

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

class ProductList(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    price = serializers.FloatField()

class CreateOrderRequest(serializers.Serializer):
    customer_id = serializers.IntegerField()
    address = serializers.CharField()
    products = serializers.ListField(child=ProductList())

    def get_customer_id(self):
        return self.validated_data.get('customer_id')

    def get_address(self):
        return self.validated_data.get('address')

    def get_products(self):
        return self.validated_data.get('products')
