Per fer funcionar el que hi ha al repositori, simplement hem de fer

```
$ pip install -r requirements.txt
$ python manage.py runserver
```

De totes formes, l'important es com desevolupat cadascuna de les aplicacions


Pas a Pas
=========

Primer de tot, configurem l'entorn de Django

- Creem un fitxer requirements.txt que digui Django i l'instalem
```
$ pip install -r requirements.txt
```
- I seguidament creem l'aplicació pare 
```
$ django-admin startproject curs
```

Aplicació Hello
---------------

Segueixo aixo com a guia:

https://docs.djangoproject.com/en/1.11/intro/tutorial01/
```
$ python manage.py startapp hello
```
Toco 3 fitxers de l'aplicació hello:

- urls.py per mapejar l'index
- views.py per crear una funcio index que carrega una plantilla index.html
- plantilla hello/index.html

I llavos a l'aplicacio pare curs:

- afegeixo hello a la llista d'aplicacions INSTALLED_APPS
- Toco el urls.py de curs per afegir les urls de l'aplicació hello 
```
$ python manage.py runserver
```
I ja està funcional a http://localhost:8000/hello


Client OAuth 2.0
----------------
```
$ python manage.py startapp client
```
- Afegeixo requests_oauthlib al requirements.txt
- Creo la url /client/login que fa la petició del authorization code a Google
- Coloco el link per fer login a la plantilla
- Creo la url /client/oauth2callback que recull el codi i obté el token i el guarda a la sessió
- Crido a la funció que obté les dades personals de l'usuari a partir del token