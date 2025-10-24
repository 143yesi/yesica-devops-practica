# Proyecto: Tienda Online - Dockerizado

## Nombre
Yésica Ramírez Bernal

## Descripción
Proyecto de Python que implementa clases para representar productos, usuarios y pedidos de una tienda online.  
Incluye `main.py` que prueba los métodos de `TiendaService`. Esta versión está contenida en Docker para facilitar su ejecución en cualquier entorno.

---

## 🐳 Docker

### a. Construir la imagen
Desde la raíz del proyecto (donde está el Dockerfile y el requirements.txt) ejecuta:

```bash
docker build -t yesica-devops-practica:latest .

### b. Ejecutar la imagen
docker run --rm yesica-devops-practica:latest

### c. Variables de entorno: No aplica

### d. Salida esperada
        Al ejecutar la imagen, la aplicación debería:
        	1.	Crear instancias de productos (ProductoElectronico, ProductoRopa).
        	2.	Crear usuarios y clientes.
        	3.	Probar métodos de TiendaService:
        	    • Mostrar lista de productos.
        	    •	Comprobar stock.
        	    •	Actualizar stock tras compras.
        	4.	Imprimir en consola los resultados de estas operaciones.

