from django.db import transaction
import store.models as m

class Order:

    @staticmethod
    def create_order(customer_id, address, products_list):
        """
        :param customer_id:
        :param address:
        :param products_list: Object with getId(), getQuantity(), getPrice() methods
        :return:
        """
        try:
            with transaction.atomic():
                order = m.Order(customer_id=m.Customer.objects.filter(id=customer_id).first(),
                                delivery_address=address)
                order.save()
                for p in products_list:
                    id = p.getId()
                    quantity = p.getQuantity()
                    price = p.getPrice()
                    m.OrderProduct(order_id=order,
                                   cost_per_item=price,
                                   quantity=quantity,
                                   product_id=m.Product.objects.filter(id=id).first())
        except Exception as e:
            print(e)
            raise e