FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install flask requests flasgger
EXPOSE 5003
CMD ["python", "app.py"]