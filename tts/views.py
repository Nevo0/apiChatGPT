from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.core.files.base import ContentFile
import openai, os, io
from dotenv import load_dotenv

from .models import MP3File

load_dotenv()
def index(request):
    api_key= os.getenv("OPENAI_KEY", None)
    # print(api_key)
    client = openai.OpenAI(api_key = api_key)    
    # client.api_key = api_key  
    response = client.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input="Oprawa ATEX serii OptiLine jest wyposażona w moduł LED o wysokiej wydajności. W zależności od wersji można ją stosować jako oświetlenie podstawowe i/lub oświetlenie awaryjne. Korpusu wykonano z poliestru wzmocnionego włóknem szklanym (GRP) z kolei klosz z poliwęglanu stabilizowanego UV. Klosz oprawy występuje w trzech wariantach: transparentnym, mrożonym oraz mlecznym. Oprawa oświetleniowa Ex OptiLine umożliwia stosowanie soczewek, które pozwalają na łatwą zmianę kierunku świecenia.Przelotowe okablowanie z dwoma złączami zasilającymi oraz możliwość użycia nawet czterech dławnic M20 lub M25 umożliwia łączenie oprawy w różnych konfiguracjach bez konieczności stosowania puszek rozdzielczych. Rozwiązanie to ogranicza także długość kabli zasilających oraz koryt, a także pozwala stosować kable różnych producentów i o różnych przekrojach.Oprawa ATEX OptiLine nie posiada luźnych elementów, które mogłyby spaść podczas instalacji. Klosz i wewnętrzna płyta montażowa są połączone z korpusem poprzez zawiasy, a zatrzaski klosza i śruby płyty montażowej zintegrowane z obudową."
        )
    # print(response.content)
    byte_stream = io.BytesIO(response.content)
    mp3_url = response.content
    mp3_file = MP3File(title='test')

    # Create a Django File object from the audio data
    mp3_file.mp3.save(f"tedst.mp3", ContentFile(mp3_url))
    # mp3_file = MP3File(title="title", mp3=byte_stream )
    # mp3_file.save()
    return HttpResponse("Hello, world. You're at the polls index.")