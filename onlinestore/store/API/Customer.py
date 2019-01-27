from django.http import JsonResponse
from store.serializers.CustomerSerializer import CreateCustomerRequest
from rest_framework.parsers import JSONParser
from store.Class.Customer import Customer
from rest_framework.decorators import api_view

@api_view(['POST'])
def create_agent(request):
    try:
        input = JSONParser().parse(request)
        createCustomerSerializer = CreateCustomerRequest(data=input)

        if not createCustomerSerializer.is_valid():
            return JsonResponse('Invalid request',safe=False,status=500)

        name = createCustomerSerializer.get_name()
        contact = createCustomerSerializer.get_contact()

        Customer.create_customer(name,contact)

        return JsonResponse({}, status=200)
    except Exception:
        return JsonResponse('Can not create agent.', safe=False, status=500)
