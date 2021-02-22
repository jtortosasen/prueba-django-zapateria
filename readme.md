# README.md
## Contenido
- Este proyecto está realizado con Django 3.1
- Ha sido desarrollado con VSCode bajo WSL2 sobre Windows 10
- Para este proyecto además se ha hecho uso de `Git`, `Docker`, `djangorestframework` y `drf_yasg` para la generación automática de documentación
- Se hace uso del modulo django-admin para las operaciones CRUD

## Docker
Para ejecutar el entorno con Docker basta con ejecutar dentro de la carpeta raíz:
`sudo docker build -f development/Dockerfile -t zapateria-bernini .`
Y luego
`sudo docker-compose -f development/docker-compose.yml up -d`

# Tareas asignadas y changelog
A continuación voy a desgranar las tareas que me he asignado a la hora de realizar la prueba para poder llevarla acabo, para así reflejar la organización en un entorno de trabajo real. No se ve reflejado en los commits porque al ser el inicio de un proyecto pequeño no lo veo necesario.
###  Etapa 1:
- Creación de django-admin de aplicación principal y website
- Creación de modelos que reflejen las necesidades del problema/negocio
- Añadir automaticamente usuario actual a la compra
- Crear grupo y usuario con acceso restringido
- ManyToManyFields en list_display en admin form
- Sumatorio total artículos
- Precio artículos en forms
- Formateo moneda decimal
- Mostrar únicamente los pedidos del usuario actual
- Mostrar precio al hacer pedido

###  Etapa 2:
- Añadir correo al usuario
- Enviar correo tras el evento de guardar

### Etapa 3:
- Crear endpoint para consulta de artículos
- Añadir documentación con OpenAPI a endpoint

### Etapa 4:
- Sacar fuera parámetros de configuración email
- Crear imágen y entorno desarrollo con Docker
- Sanitizar logging
