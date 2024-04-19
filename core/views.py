import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


def hello_world(request):
    return JsonResponse({"message": "Hello World"})


@csrf_exempt
def create_user(request):
    data = json.loads(request.body)
    username = data["username"]
    password = data["password"]
    email = data["email"]
    user = User(username=username,email=email)
    user.set_password(password)
    user.save()
    return JsonResponse(
        {
            "message": "User created",
            "user": {
                "username": user.username,
                "email": user.email,
            },
        }
    )
