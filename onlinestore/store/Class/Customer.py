import store.models

class Customer:

    @staticmethod
    def create_customer(name,contact):
        store.models.Customer(name= name, contact= contact).save()

    @staticmethod
    def get_customer(customer_id):
        return store.models.Customer.objects.filter(id=customer_id).first()