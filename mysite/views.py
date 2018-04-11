from django.http import JsonResponse
from django.core import serializers
from custom.models import *

def get_compa(request):
    hardId = request.GET['hwid']
    hard = serializers.serialize('json', [Compa.objects.get(hardware=hardId)])
    data = {
        'hard':hard
    }
    return JsonResponse(data)