import uuid
from datetime import datetime
from .Usuario import Cliente
from .Producto import Producto


class Pedido:   
    """Clase que representa un pedido realizado por un cliente."""

    def __init__(self, cliente, productos: list):
        """
        Inicializa un pedido con un cliente y una lista de productos.
        
        Args:
            cliente (Cliente): El cliente que realiza el pedido.
            productos (List[Tuple[Producto, int]]): Lista de tuplas con productos y cantidades.
        """
        self.id: str = str(uuid.uuid4())   # Identificador único
        self.cliente = cliente
        self.productos = productos  # lista de tuplas (Producto, cantidad)
        self.fecha = datetime.now() # Fecha de creación del pedido

    def calcular_total(self) -> float:
        """
        Calcula el importe total del pedido sumando el precio * cantidad de cada producto.
        
        Returns:
            float: Total del pedido
        """
        return sum(prod.precio * cant for prod, cant in self.productos)

    def __str__(self) -> str:
        """
        Genera una representación legible del pedido.
        
        Returns:
            str: Resumen del pedido, incluyendo cliente, total y lista de productos.
        """
        productos_str = ", ".join([f"{prod.nombre} x{cant}" for prod, cant in self.productos])
        return f"Pedido de {self.cliente.nombre}\nTotal: {self.calcular_total():.2f}€\nProductos: {productos_str}"
