from django.db import transaction
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from store.Class.Order import Order
from store.Class.Product import Product
from store.Class.Store import Store
from store.serializers.OrderSerializer import CreateOrderRequest, ProductListFields


@api_view(['POST'])
def create_order(request):
    try:
        input = JSONParser().parse(request)
        createOrderSerializer = CreateOrderRequest(data=input)

        if not createOrderSerializer.is_valid():
            return JsonResponse('Invalid request',safe=False,status=500)

        products = []
        for product in createOrderSerializer.get_products():
            pObj = ProductListFields()
            pObj.setId(product[pObj.ID_FIELD])
            pObj.setQuantity(product[pObj.QUANTITY_FIELD])
            pObj.setPrice(product[pObj.PRICE_FIELD])
            products.append(pObj)

        Order.create_order(createOrderSerializer.get_customer_id(),
                           createOrderSerializer.get_address(),
                           products)

        return JsonResponse({}, status=200)
    except Exception:
        return JsonResponse('Can not create Order.', safe=False, status=500)
