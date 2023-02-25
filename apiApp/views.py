

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def my_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        search = meaning(data["word"])
        response_data = {'Meaning':search}
        return JsonResponse(response_data, status=200)
    else:
        response_data = {'error': 'Invalid request method'}
        return JsonResponse(response_data, status=400)


def meaning(word):
    name2 = "./apiApp/Word.txt"

    with open(name2,"r",encoding="utf-8") as data:
        lines = data.readlines()
    for line in lines:
        jason = json.loads(line)
        if(jason['word']):
            return jason






