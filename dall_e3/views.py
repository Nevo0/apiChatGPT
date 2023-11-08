from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.core.files.base import ContentFile
import openai, os, io
from dotenv import load_dotenv

from dall_e3.models import DallE3File


load_dotenv()
def index(request):
    api_key= os.getenv("OPENAI_KEY", None)
    # print(api_key)
    client = openai.OpenAI(api_key = api_key)    
    # client.api_key = api_key  
    response = client.images.generate(
        model="dall-e-3",
        prompt="na podstawie opisu wygeneruj zdjecie, zdjecie powinno być realistyczne . Na zdjęciu widać przemysłowe urządzenia związane z oczyszczaniem powietrza. Widoczne są duże obiekty przypominające filtry, które służą do oddzielania cząstek stałych od gazów. Z lewej strony znajduje się duża, zielona konstrukcja, która może być skrzynią filtracyjną, z rurami prowadzącymi do innych części urządzenia. Poniżej tej konstrukcji ustawiony jest big-bag (wielkogabarytowy worek), który może służyć do gromadzenia materiałów z procesu przemysłowego. Dodatkowo, w tle widoczne są inne elementy przemysłowe, w tym coś, co wygląda n wentylatory przemysłowe oraz metalowy budynek z profilowanej blachy. Wygląd tego miejsca sugeruje, że jest to część fabryki, gdzie przetwarzane są różne materiały i gdzie istotny",
        size="1024x1024",
        quality="standard",
        n=1,
        )

    image_url = response.data[0].url
    print(image_url)
    mp3_url = response.content
    image = DallE3File(title='test')

    # Create a Django File object from the audio data
    image.image.save(f"tedst.mp3", ContentFile(image))
    # mp3_file.save()
    return HttpResponse("Hello, world. You're at the polls index.")