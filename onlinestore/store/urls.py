from django.urls import path
from store.API import Store,Agent

urlpatterns = [
    path('store', Store.create_store),
    path('agent', Agent.create_agent)
]