from django.http import JsonResponse
from store.serializers.StoreSerializer import CreateStoreRequest
from rest_framework.parsers import JSONParser
from store.Class.Store import Store
from rest_framework.decorators import api_view


@api_view(['POST'])
def create_store(request):
    try:
        input = JSONParser().parse(request)
        createStoreSerializer = CreateStoreRequest(data=input)

        if not createStoreSerializer.is_valid():
            return JsonResponse('Invalid request',safe=False,status=500)

        name = createStoreSerializer.get_name()
        address = createStoreSerializer.get_address()
        contact = createStoreSerializer.get_contact()

        Store.create_store(name,address,contact)

        return JsonResponse({}, status=200)
    except Exception:
        return JsonResponse('Can not create store.', safe=False, status=500)