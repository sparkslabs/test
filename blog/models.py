
django-admin startproject mysite .
Update TIME_ZONE in mysite/settings.py to something like Europe/London
Add STATIC_ROOT in mysite/settings.py
Check DATABASES in mysite/settings.py
python manage.py migrate
python manage.py runserver
  - visit http://127.0.0.1:8000/
python manage.py startapp blog
Install blog in INSTALLED_APPS in mysite/settings.py
edit -- blog/models.py
python manage.py makemigrations blog
python manage.py migrate blog
edit - blog/admin.py
