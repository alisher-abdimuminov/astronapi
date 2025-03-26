from django.http import HttpRequest, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from .models import Counter, Announcement

@api_view(http_method_names=["POST"])
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

@api_view(http_method_names=["GET"])
def announcement(request: HttpRequest):
    a = Announcement.objects.last()
    if a:
        return Response({
            "content": a.content,
            "created": a.created.strftime("%d/%m/%Y")
        })
    else:
        return Response({
            "announcement": None,
            "created": None
        })
