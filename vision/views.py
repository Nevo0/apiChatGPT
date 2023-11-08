from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.core.files.base import ContentFile
import openai, os, io
from dotenv import load_dotenv


load_dotenv()
def index(request):
    api_key= os.getenv("OPENAI_KEY", None)
    # print(api_key)
    client = openai.OpenAI(api_key = api_key)    
    # client.api_key = api_key  
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
        {
            "role": "user",
                    "content": [
                        {"type": "text", "text": "Oprawa ATEX serii OptiLine jest wyposażona w moduł LED o wysokiej wydajności. W zależności od wersji można ją stosować jako oświetlenie podstawowe i/lub oświetlenie awaryjne. Korpusu wykonano z poliestru wzmocnionego włóknem szklanym (GRP) z kolei klosz z poliwęglanu stabilizowanego UV. Klosz oprawy występuje w trzech wariantach: transparentnym, mrożonym oraz mlecznym. Oprawa oświetleniowa Ex OptiLine umożliwia stosowanie soczewek, które pozwalają na łatwą zmianę kierunku świecenia.Przelotowe okablowanie z dwoma złączami zasilającymi oraz możliwość użycia nawet czterech dławnic M20 lub M25 umożliwia łączenie oprawy w różnych konfiguracjach bez konieczności stosowania puszek rozdzielczych. Rozwiązanie to ogranicza także długość kabli zasilających oraz koryt, a także pozwala stosować kable różnych producentów i o różnych przekrojach.Oprawa ATEX OptiLine nie posiada luźnych elementów, które mogłyby spaść podczas instalacji. Klosz i wewnętrzna płyta montażowa są połączone z korpusem poprzez zawiasy, a zatrzaski klosza i śruby płyty montażowej zintegrowane z obudową. Powyrzej troche kontekstu. Co jest na zdjeciu?"},
                        {
                            "type": "image_url",
                            "image_url": "https://hardo.tech/wp-content/uploads/2023/10/oprawa-oswietleniowa-ATEX-jak-otwierac-i-zamykac.gif",
                        },
                    ],
                }
            ],
            max_tokens=300,
    )
    print(response)
    # mp3_file.save()
    return HttpResponse("Hello, world. You're at the polls index.")