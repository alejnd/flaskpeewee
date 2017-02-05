# Participa

## Introducción:
Por ahora el objetivo de este repo es probar aprender y mejorar, este
readme aunque no sea la herramienta adecuada servirá como log de las
decisiones cambios y lecciones aprendidas en el desarrollo de apps
con flask.

### Virutal env: básico para cualquier proyecto python.
Entra en el directorio de tu proyecto y crea el virtualenv con: 
`virtualenv venv`

esto crea el directorio venv (ignorado en el **.gitignore**) y guardará todas las dependencias necesarias.

Lo activamos con: `source venv/bin/activate`

Ahora cualquier paquete que bajemos con pip se guardará en el virtual env sin afectar al sistema.
Como este proyecto ya tiene las depndencias guardas en **requirements.txt** podemos instalaras con:

`pip install -r requirements.txt`

Si instalamos mas paquetes con pip y queremos guardar el estado actual de las dependencias las guardamos con:

`pip freeze > requirements.txt` 

Y por último para salir del virtual env ejecutamos: `deactivate`

**Eso es todo!**

## WorkLog
---
###### Fri Feb 3 16:00:42 CET 2017
No estoy satisfecho con la organización del código y los imports, es posible que cree una rama para ello.
Tampoco están bien organizados los test (lo que es normal ya que solo estaba probando), creo que es lo
primero que cambiaré.

---
###### Sun Feb 5 20:29:15 CET 2017
Ya estan mejor organizados los test, pero el tema de tener los context.py para lidiar con los imports es
poco elegante, tengo que ver como ceñirme a los estandares de organización de proyectos de flask.
---

