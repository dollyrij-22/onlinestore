from rest_framework import serializers

class CreateCustomerRequest(serializers.Serializer):
    name = serializers.CharField()
    contact = serializers.IntegerField()

    def get_name(self):
        return self.validated_data.get('name')

    def get_contact(self):
        return self.validated_data.get('contact')

class AddCustomerAddressRequest(serializers.Serializer):
    customer_id = serializers.IntegerField()
    address = serializers.CharField()

    def get_customer_id(self):
        return self.validated_data.get('customer_id')

    def get_address(self):
        return self.validated_data.get('address')

class ListCustomerAddressResponse:
    ADDRESS_ID= 'id'
    ADDRESS= 'address'