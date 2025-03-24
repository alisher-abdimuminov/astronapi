from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Counter

@csrf_exempt
def count(request: HttpRequest, date: str):
    counter = Counter.objects.filter(date=date)
    if counter:
        counter = counter.first()
        counter.count += 1
        counter.save()
    else:
        counter = Counter.objects.create(
            date=date,
            count=1
        )
    return JsonResponse({
        "count": counter.count
    })
