from rest_framework import serializers

class CreateCustomerRequest(serializers.Serializer):
    name = serializers.CharField()
    contact = serializers.IntegerField()

    def get_name(self):
        return self.validated_data.get('name')

    def get_contact(self):
        return self.validated_data.get('contact')