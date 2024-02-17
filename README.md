# ProyectoFinal_RiveroBrahimRoger

## Entornos virtuales

Un entorno virtual en Python es una herramienta 
que te permite crear un espacio aislado donde puedes instalar 
y manejar las dependencias (bibliotecas y versiones de Python) 
específicas para un proyecto en particular, sin afectar al sistema global

- `pip list`: Muestra las bibliotecas instaladas en el entorno virtual o global

¿Cómo crear un entorno virtual? (entorno aislado del global)

- `python -m venv .venv` (Windows)
- `python3 -m venv .venv` (Linux o Mac)

¿Cómo activar el entorno virtual?
- `.\.venv\Scripts\activate`  (Windows Powershell)
- `source .venv/bin/activate` (Linux o Mac)

## Instalación Django

- `pip install django`

## ¿Cómo crear requirements.txt?
- `pip freeze >> requirements.txt
`

¿Cómo instalar paquetes desde requirements.txt?
- `pip install -r requirements.txt`

## git comandos
'git branch' --> para ver en que rama estoy ubicado y ver las ramas que tengo
'git branch"nombre_de_rama"' --> crear y nombrar rama
'git checkout "nombre_de_rama"' --> me mueve a la rama que mencione
'git checkout -b "nombre_de_nueva_rama" --> para crear una nuva rama y posicionarme en ella 

---- ahora tenes que ver el video anterior para hacer carpeta project-----

## creamos project

-creo una carpeta 'project'
- 'mkdir project'
-  accedemos a la carpeta 'project'
- ' cd project'
- crear el proyecto Django
- 'django-admin startproject config .'
- ejecutar el servidor:
- 'python manage.py runserver'

## creamos una aplicación:
1-estar ubicado dentro de 'project' pero fuera de 'config'
- 'cd ..'
- 'ls'
2- crear una carpeta para que contenga la apps
- 'md apps'
3- acceder a la carpeta 'apps'
- 'cd apps'
4- crear la aplicación Django con el nombre que desee
- 'django-admin startapp core'

5- agregar el nombre de la lista 'config.settings.INSTALLED_APPS' 

6- Agregarel siguiente codigo a 'config.settings'
''' import sys

 

sys.path.append(str(BASE_DIR / "apps"))'''

## establecer 'config.settings.SECRET_KEY' 
'''
from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key()
'''

## creando app cliente 
- posicionarce en apps
cd apps
- crear app 'cliente' 
 en terminal ->  'django-admin startapp cliente'

- registra la app en settings.py 
linea 51 
INSTALLED_APP[
    "core", #app que ya figuraba depues de crearla la escribimos
    "cliente",
]

-copiar la urls de "core" en app "cliente"
- seguidamente copiar el contenido de views.py de core en views de cliente


- crear una carpeta "templates" para app cliente 
- dentro de templates crear carpeta cliente
- y copiar el index.html que tiene core dentro de la careta recien hecha llamada cliente que esta dentro 
de templates( pero donde decia "INICIO" ya colocamos el nombre de "CLIENTE")

IR A LAS URLS DE CONFIG
y de igual formato como se ve el path de core
copiarlo abajo y reemplasar los caracteres por los nombres de la app que estamos trabajando 
app cliente 
'''
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("core.urls", "core"))),
    path("cliente/", include(("cliente.urls", "cliente"))),
]
'''
a continuacion vamos a la terminal, vamos hacia atras con comando 
cd.. windows
cd .. linux 

y una vez corroborado que estan en la carpeta project 
ejecutar -> 'python manage.py runserver'

ir a views.py de cliente y cambiar "core" (porque de ahi habiammos copiado)
por "cliente"
'''
def index(request):
    context = {"app_name": "VirtualPlanet"}
    return render(request, "cliente/index.html", context)
'''

crea un boton (button)
en la pag pricipal o sear en index.html de core
"""
"<button><a href="{% url 'cliente:index' %}">CLIENTE</a></button>"
""" la clave cliente hace refernecia al nombre de la urls que figura en urls.py de  app config
e index y el valor quese ve con el nombre index es de la urls que esta dentro de app cliente 

-en el index de cliente podemos crear un boton que haga lo mismo spero en reversa , que vaya de cliente al inicio
    '''<button><a href="{% url 'core:index' %}">inicio</a></button>'''
    
### crear base de datos

crear archivo python pre-SQL:
- 'python manage.py makemigrations'
ese comando crear un archivo.py dentro de la carpeta migrations que no se va a tocar hasta mayor conocimiento,es la encargada de crear codigo en cadenas referente a la base de datos .

crear SQL Y modificar base de datos:
- 'python manage.py migrate'
hs 01.31.50 aprox de video

### crear super usuario
- 'python manage.py createsuperuser'
 cree el superusuario 
 pero con el nombre de usuario brahim (porque habia creado el co admin y no me dejaba)
 clave si es 123

 para registrar los modelos que crfeaste anteriormente y se vean en admin
 ir a admin.py de la carpeta que creaste para hacer la app en este caaso se llama cliente

 ## escribir la funsion pra crear cliente
 ...

 ### usar archivos Bootstrap
 crear carpeta en core llamada "static"
 y dentro una carpeta "core"
 descargar ahi los archivos extraidos de ña seleccion hecha en la pagina de bootstrap
 "assets" contiene la trasparencia
 "css" todo el lenguaje html 
 "js" nada 

 renombramos los arch hatml de templates usando conmo prefijo un guion bajo:
 _base.html
 _inddex.html
 para que ?
 para mover el index del archivo anteriormente extraido a core de templates
  
vas a entrar en index, el archivo que acabas de copiar y vas a ir a la linea 1 y colocar 
 ###{% load static %} 
 obviio sin los #  esto es para que el codigo cada ves que se encuentre con un static vaya a la direccion que vas a poner en la linea 14 donde dice donde buscar 
 ###"{% static 'core/css/styles.css' %}" rel="stylesheet"
 al igual que en la linea 12 
 ###href="{% static 'core/assets/favicon.ico' %}"
 tambien en la linea 85 
 ###" {% static 'core/js/scripts.js' %}"></script>

 todo los que son archivos 

 ### asignar el index descargado como base, y desacer la base que teniamos
 antes obviamente de la base anterior extraemos lo que necesitamos y ya creamos 
 y lo colocamos donde va 

###alternativas para colocar imagenes 
una es la buscar un archivo de internet una imagen copiar vinculo y pegarla en el index line 21 
la otra 
en crear una carpeta en en core de static que se llame img , descargar las imagenes en formato webp y copiar en la linea 19 de index de esta manera #src="{% static 'core/img/apple_producto.webp' %}"
recorda que la imagen debe de estar en formato webp
 





 