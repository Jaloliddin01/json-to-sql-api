from django.http import HttpRequest, JsonResponse, HttpResponse
from django.contrib.auth.models import User

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
