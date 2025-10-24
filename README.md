# Proyecto: Tienda Online - Dockerizado

## Nombre
Yésica Ramírez Bernal

## Descripción
Proyecto de Python que implementa clases para representar productos, usuarios y pedidos de una tienda online.  
Incluye `main.py` que prueba los métodos de `TiendaService`. Esta versión está contenida en Docker para facilitar su ejecución en cualquier entorno.

---

## 🐳 Docker

### a. Construir la imagen
```bash
docker build -t yesica-devops-practica:latest .
```

### b. Ejecutar la imagen
```bash
docker run --rm yesica-devops-practica:latest
```
### c. Variables de entorno: 
No aplica

### d. Salida esperada
Al ejecutar la imagen, la aplicación debería:
1. Crear instancias de productos.
2. Crear usuarios y clientes.
3. Probar métodos de TiendaService:
   - Mostrar lista de productos
   - Comprobar stock
   - Actualizar stock
4. Imprimir los resultados en consola.

