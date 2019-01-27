import store.models

class Store:

    @staticmethod
    def create_store(name,address,contact):
        store.models.Store(name= name, address= address, contact= contact).save()

    @staticmethod
    def get_store(store_id):
        return store.models.Store.objects.filter(id=store_id).first()