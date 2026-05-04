Django Project Level learnings

1. __init__.py -> This entire directory is a Python Package
2. settings.py -> Main configuration file in Django
3. wsgi.py -> web server gateway interface (For deploying our applications)
4. asgi.py -> Asynchronous Server Gateway Interface (For handling asynchronous web protocols like websockets)
5. urls.py -> URL Patterns 

Internal Working of the URLPatterns
-------------------------------------

Django -> Root_urlconf mentioned in the settings.py file -> project/urls.py -> match with incoming requests -> Call the view

