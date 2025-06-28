# Guía de uso

## 1. Ejecutar el *broker*
Abre una terminal (*cmd*) 
```
python broker.py
```

Se mostrará como resultado lo siguiente:
```
[BROKER] Escuchando en localhost:14000....
```

## 2. Ejecutar uno o más suscriptores
Abre una terminal y ejecuta un suscriptor o más
```
python subscriber.py
```

Cuando se te pida, escribe el tema (*topic*), por ejemplo:
```
Tema a suscribirse: deportes
```

El sistema mantendrá la conexión abierta esperando mensajes del *broker*.

## 3. Ejecutar uno o más publicadores
En otra terminal: 
```
python publisher.py
```

Envía un mensaje en este formato:
```
deportes: ¡El América ganó 15-0!
```

Todos los *suscriptores* suscritos a *deportes* recibirán:
```
[deportes]: ¡El Pumas ganó 5-0!
```