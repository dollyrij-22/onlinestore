from django.urls import path
from store.API import Store, Agent, Customer, Product, Order

urlpatterns = [
    path('store', Store.create_store),
    path('agent', Agent.create_agent),
    path('customer', Customer.create_customer),
    path('customer-address', Customer.add_customer_address),
    path('customer/<int:customer_id>/address', Customer.list_customer_address),

    path('product', Product.create_product),
    path('product/store/<int:store_id>', Product.list_product),

    path('order', Order.create_order),

    #path('agent/<int:agent_id>/orders',Agent.list_orders)
]