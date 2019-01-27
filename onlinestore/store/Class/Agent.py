import store.models

class Agent:

    @staticmethod
    def create_agent(name,contact):
        store.models.Agent(name= name, contact= contact).save()