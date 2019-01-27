import store.models as model

class Product:

    @staticmethod
    def create_product(name,price,store_id):
        model.Product(name= name, price= price, store_id= store_id).save()

    @staticmethod
    def get_store_products(store_id):
        return model.Product.objects.filter(store_id=store_id).values()