import store.models

class Store:

    @staticmethod
    def create_store(name,address,contact):
        store.models.Store(name= name, address= address, contact= contact).save()