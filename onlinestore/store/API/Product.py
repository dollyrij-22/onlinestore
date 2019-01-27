from django.http import JsonResponse

from store.Class.ErrorMessage import ErrorMessage
from store.Class.StatusCode import StatusCode
from store.serializers.ProductSerializer import CreateProductRequest, ListProductsResponse
from rest_framework.parsers import JSONParser
from store.Class.Product import Product
from store.Class.Store import Store
from rest_framework.decorators import api_view

@api_view(['POST'])
def create_product(request):
    try:
        input = JSONParser().parse(request)
        createProductSerializer = CreateProductRequest(data=input)

        if not createProductSerializer.is_valid():
            return JsonResponse('Invalid request',safe=False,status=500)

        name = createProductSerializer.get_name()
        price = createProductSerializer.get_price()
        store_id = createProductSerializer.get_store_id()

        store = Store.get_store(store_id)

        Product.create_product(name,price,store)

        return JsonResponse({}, status=200)
    except Exception:
        return JsonResponse('Can not create product.', safe=False, status=500)

@api_view(['GET'])
def list_product(request, store_id):
    try:
        response = []
        for p in Product.get_store_products(store_id):
            response.append( {ListProductsResponse.PRODUCT_ID: p['id'],
                              ListProductsResponse.PRODUCT_NAME: p['name'],
                              ListProductsResponse.PRODUCT_PRICE:p['price']})
        return JsonResponse(response, safe=False, status=StatusCode.SUCCESS)
    except Exception as e:
        print(e)
        return JsonResponse(ErrorMessage.EXCEPTION_OCCURRED, safe=False, status=StatusCode.EXCEPTION_CODE)
