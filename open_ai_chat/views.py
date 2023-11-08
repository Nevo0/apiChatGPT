import logging
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
import openai, os
from dotenv import load_dotenv

logger = logging.getLogger("django")
load_dotenv()
def index(request):    
    
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_protect
def chatBot(request):
    api_key= os.getenv("OPENAI_KEY", None)
    chatbot_resppons=None
    logger.info(request)
    print(logger)
    if api_key is not None and  request.method == 'POST':
        model='text-davinci-001'
        user_input= request.POST.get('input_value')

        prompt= f"translate this tax to polish: {user_input}"
        prompt2= f"if the question is related to weather - answer it: {user_input} ,else  return Nie wiem"
        openai.api_key = api_key
        chatbot_resppons= openai.Completion.create(
        model=model,
        prompt=prompt2,
        max_tokens=100,
        temperature=0.7
        )
        user_input= request.POST.get('input_value')
        # model_list= openai.Model.list()
        # print(model_list)
        respons = chatbot_resppons['choices'][0]
        print((prompt2))
        respons = chatbot_resppons['choices'][0]['text']
        return render(request, 'main.html',{"respons":respons})
    return HttpResponse("Hello, world. You're at the polls index.")

# chatBot("request")