from django.http import JsonResponse

from store.Class.StatusCode import StatusCode
from store.serializers.CustomerSerializer import CreateCustomerRequest,AddCustomerAddressRequest,ListCustomerAddressResponse
from rest_framework.parsers import JSONParser
from store.Class.Customer import Customer
from store.Class.CustomerAddress import CustomerAddress
from rest_framework.decorators import api_view
from store.Class.ErrorMessage import ErrorMessage

@api_view(['POST'])
def create_customer(request):
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
        return JsonResponse(ErrorMessage.EXCEPTION_OCCURRED, safe=False, status=StatusCode.EXCEPTION_CODE)

@api_view(['POST'])
def add_customer_address(request):
    try:
        input = JSONParser().parse(request)
        addCustomerAddressSerializer = AddCustomerAddressRequest(data=input)

        if not addCustomerAddressSerializer.is_valid():
            return JsonResponse('Invalid request to add customer address', safe=False, status=500)

        customer_id = addCustomerAddressSerializer.get_customer_id()
        address = addCustomerAddressSerializer.get_address()

        customer = Customer.get_customer(customer_id)

        CustomerAddress.add_customer_address(customer,address)

        return JsonResponse({}, status=200)
    except:
        return JsonResponse(ErrorMessage.EXCEPTION_OCCURRED, safe=False, status=StatusCode.EXCEPTION_CODE)


@api_view(['GET'])
def list_customer_address(request,customer_id):
    try:
        customer_id = customer_id
        addresses = CustomerAddress.get_customer_address(customer_id)

        response = []
        for address in addresses:
            addressObj = {ListCustomerAddressResponse.ADDRESS_ID: address[ListCustomerAddressResponse.ADDRESS_ID]}
            addressObj[ListCustomerAddressResponse.ADDRESS] = address[ListCustomerAddressResponse.ADDRESS]
            response.append(addressObj)
        return JsonResponse(response, safe=False, status=StatusCode.SUCCESS)
    except:
        return JsonResponse(ErrorMessage.EXCEPTION_OCCURRED,safe=False,status=StatusCode.EXCEPTION_CODE)

