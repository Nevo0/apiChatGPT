from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.core.files.base import ContentFile
import openai, os, io,requests
from dotenv import load_dotenv


load_dotenv()
def index(request):
    response = requests.get("https://gw.eu")
    # print(response.json())
    if response.status_code == 200:
        print(response.text)

    return HttpResponse("Hello, world. You're at the polls index.2")