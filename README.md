# Django Crud con Docker
Aplicación crud de control de gastos hecha con Django, Virtualenv y Docker

### Ejecutando la aplicación:
Para ejecutar esta aplicación sin tener que instalar todas las dependencias, usa Docker y Docker Compose. Sigue las instrucciones a continuación:
- Si no tienes [Docker](https://docs.docker.com/install/) y [Docker Compose](https://docs.docker.com/compose/install/), instálalos haciendo clic en sus respectivos enlaces.
- A continuación, clona o descarga este proyecto. Si eliges clonar, escribe:
``` bash
$ git clone https://github.com/isacmoura/django-crud-with-docker.git
```
- Ingresa a la carpeta del proyecto:
```bash
$ cd django-crud-with-docker
```
- Luego, ejecuta el comando **docker-compose**:
```bash
$ docker-compose up -d
```
Es posible que tengas que usar `sudo` con el comando anterior.
Este comando construirá los contenedores. Luego instalará pip (si no lo tienes) y usando pip instalaremos Virtualenv y Django. Finalmente, nuestro servidor comenzará a funcionar y se ejecutará en la dirección ip `0.0.0.0:8000`.

### Cambios post-instalación
Puedes usar tu aplicación en la dirección `0.0.0.0:8000`, pero, si quieres, puedes hacer algunos cambios.
Para hacer esto, sigue las instrucciones:
- Crea el módulo:
`docker-compose run web ./manage.py startapp app`. **cambia "app" por un nombre de tu preferencia**
- Ejecuta las migraciones:
`docker-compose run web ./manage.py migrate`
- Crea un superusuario para el área de Django Admin:
`docker-compose run web ./manage.py createsuperuser`

#### Contribuciones
Siéntete libre de contribuir con este proyecto, envía un Pull Request o abre un issue.
