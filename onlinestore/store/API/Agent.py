from django.http import JsonResponse
from store.serializers.AgentSerializer import CreateAgentRequest
from rest_framework.parsers import JSONParser
from store.Class.Agent import Agent
from rest_framework.decorators import api_view

@api_view(['POST'])
def create_agent(request):
    try:
        input = JSONParser().parse(request)
        createAgentSerializer = CreateAgentRequest(data=input)

        if not createAgentSerializer.is_valid():
            return JsonResponse('Invalid request',safe=False,status=500)

        name = createAgentSerializer.get_name()
        contact = createAgentSerializer.get_contact()

        Agent.create_agent(name,contact)

        return JsonResponse({}, status=200)
    except:
        return JsonResponse('Can not create agent.', safe=False, status=500)

@api_view(['GET'])
def list_orders(request):
    try:
        print(request)

        return JsonResponse({},status=200)
    except:
        return JsonResponse('Can not send list of orders belongs to agent',safe=False,status=200)