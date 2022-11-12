import json
from django.http import JsonResponse 
from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie


def train(request):
        rawData = request.GET.get('trainingData')
        rows = rawData.split('\n')
        return JsonResponse({"status": 'Success'}) 