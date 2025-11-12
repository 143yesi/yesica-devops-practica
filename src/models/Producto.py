import uuid


class Producto:
    """Clase base que representa un producto genérico en la tienda."""
    
    def __init__(self, nombre: str, precio: float, stock: int):
        """
        Inicializa un producto con un nombre, precio y cantidad en stock.

        Args:
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
            stock (int): Cantidad disponible en inventario.
        """
        self.id: str = str(uuid.uuid4())  # Identificador único
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def hay_stock(self, cantidad: int) -> bool:
        """
        Comprueba si hay suficiente stock de un producto.

        Args:
            cantidad (int): Cantidad que se desea verificar.

        Returns:
            bool: True si hay stock suficiente, False en caso contrario.
        """
        return self.stock >= cantidad    
    
    def actualizar_stock(self, cantidad: int):
        """
        Actualiza la cantidad de stock disponible.

        Args:
            cantidad (int): Cantidad a añadir o restar del stock (negativa si es venta).
        """
        self.stock += cantidad  # cantidad negativa si es venta
    
    def __str__(self) -> str:
        """
        Representación legible del producto.

        Returns:
            str: Información básica del producto.
        """
        return f"   {self.nombre}\nPrecio: {self.precio} €\nStock: {self.stock} "
    
    
class ProductoElectronico(Producto):
        """Clase que representa un producto electrónico, con garantía."""

        def __init__(self, nombre: str, precio: float, stock: int, garantia_meses: int):
            """
            Inicializa un producto electrónico con garantía.

            Args:
                nombre (str): Nombre del producto.
                precio (float): Precio del producto.
                stock (int): Cantidad disponible en inventario.
                garantia_meses (int): Meses de garantía del producto.
            """
            super().__init__(nombre, precio, stock)
            self.garantia_meses = garantia_meses
        
        def __str__(self) -> str:
            """
            Representación legible del producto electrónico.

            Returns:
                str: Información del producto incluyendo garantía.
            """
            return f"{super().__str__()}\nGarantia: {self.garantia_meses} meses"


class ProductoRopa(Producto):
        """Clase que representa un producto de ropa, con talla y color."""

        def __init__(self, nombre: str, precio: float, stock: int, talla: str, color: str):
            """
            Inicializa un producto de ropa con talla y color.

            Args:
                nombre (str): Nombre del producto.
                precio (float): Precio del producto.
                stock (int): Cantidad disponible en inventario.
                talla (str): Talla de la prenda.
                color (str): Color de la prenda.
            """
            super().__init__(nombre, precio, stock)
            self.talla = talla
            self.color = color
            
        def __str__(self) -> str:
            """
            Representación legible del producto de ropa.

            Returns:
                str: Información del producto incluyendo talla y color.
            """
            return f"{super().__str__()}\nTalla: {self.talla}\nColor: {self.color}"
