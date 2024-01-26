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

