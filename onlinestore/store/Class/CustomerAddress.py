import store.models

class CustomerAddress:
    @staticmethod
    def add_customer_address(customer_id, address):
        store.models.CustomerAddress(customer_id=customer_id, address=address).save()

    @staticmethod
    def get_customer_address(customer_id):
        return store.models.CustomerAddress.objects.filter(customer_id= customer_id).values()
