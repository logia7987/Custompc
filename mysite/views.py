from django.http import JsonResponse
from django.core import serializers
from custom.models import *

def get_compa(request):
    hardId = request.GET['hwid']
    hardType = request.GET['hwtype']
    hard = serializers.serialize('json', [Hardware.objects.get(id=hardId, hardware_kind=hardType)])
    objectQuery = Compa.objects.filter(hardware=hardId)
    compa = serializers.serialize('json', list(objectQuery))
    data = {
        'hard':hard,
        'compa':compa
    }
    return JsonResponse(data)