from models.Usuario import Cliente, Administrador
from models.Producto import Producto
from models.Pedido import Pedido


class TiendaService:
    """Clase que gestiona los servicios principales de la tienda online."""

    def __init__(self):
        """
        Inicializa la tienda con listas vacías de usuarios, productos y pedidos.
        """
        self.usuarios = []
        self.productos = []
        self.pedidos = []

    # -------------------- Gestión de usuarios --------------------
    def registrar_usuario(self, tipo: str, **atributos):
        """
        Registra un nuevo usuario en la tienda según su tipo.

        Args:
            tipo (str): Tipo de usuario ('cliente' o 'administrador').
            **atributos: Atributos necesarios para inicializar el usuario.

        Returns:
            Usuario: Objeto Usuario creado.
        
        Raises:
            ValueError: Si el tipo de usuario no es válido.
        """
        if tipo.lower() == "cliente":
            usuario = Cliente(**atributos)
        elif tipo.lower() == "administrador":
            usuario = Administrador(**atributos)
        else:
            raise ValueError("Tipo de usuario no válido")
        self.usuarios.append(usuario)
        return usuario

    # -------------------- Gestión de productos --------------------
    def añadir_producto(self, producto: Producto):
        """
        Añade un producto al inventario de la tienda.

        Args:
            producto (Producto): Producto a añadir.
        """
        self.productos.append(producto)

    def eliminar_producto(self, id: str):
        """
        Elimina un producto del inventario usando su identificador único.

        Args:
            id (str): Identificador del producto a eliminar.
        """
        self.productos = [p for p in self.productos if p.id != id]

    def listar_productos(self):
        """
        Imprime en consola todos los productos disponibles en la tienda.
        """
        for p in self.productos:
            print(p)
            print()

    # -------------------- Gestión de pedidos --------------------
    def realizar_pedido(self, cliente_id: str, lista_productos: list):
        """
        Realiza un pedido para un cliente verificando stock y actualizando inventario.

        Args:
            cliente_id (str): Identificador del cliente que realiza el pedido.
            lista_productos (list): Lista de tuplas (Producto, cantidad).

        Returns:
            Pedido: Objeto Pedido creado.

        Raises:
            ValueError: Si el cliente no existe o no hay suficiente stock de algún producto.
        """
        # Buscar cliente
        cliente = next((u for u in self.usuarios if u.id == cliente_id and isinstance(u, Cliente)), None)
        if not cliente:
            raise ValueError("Cliente no encontrado")

        # Verificar stock
        for prod, cant in lista_productos:
            if not prod.hay_stock(cant):
                raise ValueError(f"No hay suficiente stock de {prod.nombre}")

        # Actualizar stock
        for prod, cant in lista_productos:
            prod.actualizar_stock(-cant)
            
        # Crear y almacenar pedido
        pedido = Pedido(cliente, lista_productos)
        self.pedidos.append(pedido)
        return pedido

    def listar_pedidos_cliente(self, cliente_id: str):
        """
        Lista todos los pedidos realizados por un cliente específico.

        Args:
            cliente_id (str): Identificador del cliente.
        """
        pedidos_cliente = [p for p in self.pedidos if p.cliente.id == cliente_id]
        # Ordenar por fecha de creación
        pedidos_cliente.sort(key=lambda p: p.fecha)
        for p in pedidos_cliente:
            print(p)
            print()
    