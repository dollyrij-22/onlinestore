from rest_framework import serializers

class CreateStoreRequest(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    contact = serializers.IntegerField()

    def get_name(self):
        return self.validated_data.get('name')

    def get_address(self):
        return self.validated_data.get('address')

    def get_contact(self):
        return self.validated_data.get('contact')