# creación de los contenedores
FROM python:3.10-slim
                     # hace referencia a un archivo grande 
                     # slim es la version 
WORKDIR /app 
                    # WORKDIR es lo que hace que se ejecute en el programa
                    # /app es donde se esta ejecutando, porque el objetivo es ponerlo en nuestro sistema
COPY . .
                    # el punto a nivel de direcciones / rutas = hace referencia a que estamos copiando y los puntos son las direcciones 
                    # first poit -> es el host y second point -> contenedor 
RUN pip install -r requirements.txt
                    # pip = es una herramienta / gestor de paquetes de python, busca 
                    # en este caso el comando pip nos esta diciendo que se vana a instalar y aplicar los requerimientos del archivo 
CMD ["python", "app.py"]
                    # la CMD invoca a un shell, un interprete 
                    # ["python", "app.py"] = le pasamos los parametros que necesita para ejecutarse 