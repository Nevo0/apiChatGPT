

pip install -r requirements.txt
pip freeze > requirements.txt

python manage.py runserver 
python manage.py createsuperuser
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate



https://pypi.org/project/Markdown/
https://www.honeybadger.io/blog/python-markdown/