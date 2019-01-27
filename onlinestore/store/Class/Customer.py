import store.models

class Customer:

    @staticmethod
    def create_customer(name,contact):
        store.models.Customer(name= name, contact= contact).save()