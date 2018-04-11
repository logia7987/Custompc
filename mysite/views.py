from django.http import JsonResponse
from django.core import serializers
from custom.models import *

def get_compa(request):
    hardId = request.GET['hwid']
    ifBrd = Hardware.objects.get(id=hardId)
    brdFilter = Hardware.objects.filter(id=hardId,hardware_kind="BRD")
    if ifBrd in brdFilter:
        objectQuery = Compa.objects.filter(hardware=hardId)
        hard = serializers.serialize('json', list(objectQuery))
    else:
        hard = serializers.serialize('json', [Compa.objects.get(hardware=hardId)])
    data = {
        'hard':hard
    }
    return JsonResponse(data)