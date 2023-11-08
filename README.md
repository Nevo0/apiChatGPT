
Projekt ma na celu testowanie API dostarczanego przez OpenAI, które pozwala na wykorzystanie modelu GPT-4 
Text generation models
Function calling
Embeddings
Image generation
Text to speech
Speech to text
Vision
Moderation

pip install -r requirements.txt
pip freeze > requirements.txt

python manage.py runserver 
python manage.py createsuperuser
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate

python manage.py startapp app_name

https://pypi.org/project/Markdown/
https://www.honeybadger.io/blog/python-markdown/