# Utiliza la imagen oficial de Python como imagen principal
FROM python:3.9-slim-buster
# Establece el directorio de trabajo en el contenedor
WORKDIR /app
# Copia el contenido del directorio actual al contenedor en /app
COPY . /app
# Instala los paquetes necesarios especificados en requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# Expone el puerto 80 al mundo exterior desde este contenedor
EXPOSE 80
# Define una variable de entorno
ENV NAME World
# Ejecuta script.py cuando se inicie el contenedor
CMD ["python", "script.py"]