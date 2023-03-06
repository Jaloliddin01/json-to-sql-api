from django.http import HttpRequest, JsonResponse, HttpResponse
from django.contrib.auth.models import User
from .models import Person
import json

def get_users(request: HttpRequest) -> JsonResponse:
    users = User.objects.all()
    
    res = []

    for user in users:
        res.append(
            {
                'id': user.id,
                'username': user.username,
                'password': user.password
            }
        )

    return JsonResponse(res, safe=False)

    # data = {
    #     'id': users[0].id
    # }

    # return JsonResponse(data)

def get_people(request: HttpRequest, pk: int) -> JsonResponse:
    people = Person.objects.get(id=pk)

    res = [
        {
            'id': pk,
            'First name': people.first_name,
            'Last name': people.last_name,
        }
    ]

    # for person in people:
    #     res.append(
    #         {
    #             'id': person.id,
    #             'First name': person.first_name,
    #             'Last name': person.last_name
    #         }
    #     )

    return JsonResponse(res, safe=False)

def get_people(request: HttpRequest) -> JsonResponse:
    people = Person.objects.all()

    res = []

    for person in people:
        res.append(
            {
                'id': person.id,
                'First name': person.first_name,
                'Last name': person.last_name
            }
        )

    return JsonResponse(res, safe=False)

def add_user(request: HttpRequest) -> JsonResponse:
    body = request.body.decode()
    data = json.loads(body)

    p = Person(
        first_name= data['first_name'],
        last_name = data['last_name']
    )

    p.save()

    return JsonResponse({
        "Status": "OK",
        "Status code": 200,
    })