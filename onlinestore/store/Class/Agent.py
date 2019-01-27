import store.models

class Agent:

    @staticmethod
    def create_agent(name,contact):
        store.models.Agent(name= name, contact= contact).save()


    @staticmethod
    def list_orders(agent_id):
        orders = store.models.Order.objets.filter(agent_id=agent_id)
        return orders