# Microservicios con Docker (Contenerización)
## 1. Construye y ejecuta los servicios
Ejecuta todos los microservicios con un solo comando:

~~~bash
docker-compose up --build
~~~
Esto levanta tres contenedores:

- user_service (puerto 5001)
- product_service (puerto 5002)
- order_service (puerto 5003)

## 2. Pruebas rápidas con curl

Crear un usuario
~~~bash
curl -X POST http://localhost:5001/users -H "Content-Type: application/json" -d '{"name":"Ana"}'
~~~
Consultar un producto (por ejemplo, ID 2)
~~~bash
curl http://localhost:5002/products/2
~~~
Crear un pedido
~~~bash
curl -X POST http://localhost:5003/orders -H "Content-Type: application/json" -d '{"user_id":"1", "product_id":"2"}'
~~~