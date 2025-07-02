FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install flask requests 
# con pip instala las dependencias necesarias
EXPOSE 5004
# se usará en el port 5004
CMD ["python", "app.py"]