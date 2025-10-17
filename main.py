from models.Producto import Producto, ProductoElectronico, ProductoRopa
from models.Usuario import Cliente, Administrador
from Services.Tienda_service import TiendaService

    # ------------------- Punto de entrada -------------------
if __name__ == "__main__":
    # Crear instancia de TiendaService
    tienda = TiendaService()

    # ------------------- Registrar usuarios -------------------
    clientes_info = [
        {"nombre": "Ana", "correo": "ana@mail.com", "direccion": "Calle 123, Ciudad"},
        {"nombre": "Luis", "correo": "luis@mail.com", "direccion": "Avenida 45, Ciudad"},
        {"nombre": "Marta", "correo": "marta@mail.com", "direccion": "Plaza 67, Ciudad"}
    ]

    clientes = []
    for info in clientes_info:
        cliente = tienda.registrar_usuario(tipo="cliente", **info)
        clientes.append(cliente)

    admin = tienda.registrar_usuario(
        tipo="administrador",
        nombre="Jorge",
        correo="jorge@mail.com"
    )

    # ------------------- Mostrar usuarios -------------------
    print("......USUARIOS REGISTRADOS......\n")
    for usuario in tienda.usuarios:
        tipo = "Administrador" if usuario.is_admin() else "Cliente"
        print(f"    {tipo}:\nNombre: {usuario.nombre}\nCorreo: {usuario.correo}")
    print("\n")

    # ------------------- Añadir productos -------------------
    productos = [
        ProductoElectronico("Smartphone", 500, 10, 24),
        ProductoRopa("Camiseta", 20, 50, "M", "Roja"),
        ProductoElectronico("Laptop", 1000, 5, 12),
        ProductoRopa("Pantalón", 40, 20, "L", "Azul"),
        ProductoElectronico("Auriculares", 80, 15, 6)
    ]

    for prod in productos:
        tienda.añadir_producto(prod)

    # ------------------- Listar productos -------------------
    print("......PRODUCTOS EN LA TIENDA......\n")
    tienda.listar_productos()

    # ------------------- Realizar pedidos -------------------
    pedido1 = tienda.realizar_pedido(clientes[0].id, [(productos[0], 1), (productos[1], 2)])
    pedido2 = tienda.realizar_pedido(clientes[1].id, [(productos[2], 1)])
    pedido3 = tienda.realizar_pedido(clientes[2].id, [(productos[3], 1), (productos[4], 2)])

    # ------------------- Mostrar pedidos realizados -------------------
    print("......PEDIDOS REALIZADOS......\n")
    for pedido in [pedido1, pedido2, pedido3]:
        print(pedido)
        print()  

    # ------------------- Histórico de pedidos de un cliente -------------------
    cliente_hist = clientes[0]
    print(f"......HISTÓRICO DE PEDIDOS DE {cliente_hist.nombre}......\n")
    tienda.listar_pedidos_cliente(cliente_hist.id)

    # ------------------- Comprobar stock actualizado -------------------
    print("\n......STOCK ACTUALIZADO DE LOS PRODUCTOS......\n")
    tienda.listar_productos()
    
    
