import uuid

class Usuario:
    """Clase base que representa un usuario de la tienda."""

    def __init__(self, nombre: str, correo: str):
        """
        Inicializa un usuario con nombre y correo electrónico.

        Args:
            nombre (str): Nombre del usuario.
            correo (str): Correo electrónico del usuario.
        """
        self.id: str = str(uuid.uuid4())   # Identificador único
        self.nombre = nombre
        self.correo = correo
    
    def is_admin(self) -> bool:
        """
        Indica si el usuario es administrador.

        Returns:
            bool: Siempre False para la clase base.
        """
        return False


class Cliente(Usuario):
    """Clase que representa un cliente de la tienda."""

    def __init__(self, nombre: str, correo: str, direccion: str):  
        """
        Inicializa un cliente con dirección además de los atributos de Usuario.

        Args:
            nombre (str): Nombre del cliente.
            correo (str): Correo electrónico del cliente.
            direccion (str): Dirección postal del cliente.
        """          
        super().__init__(nombre, correo)
        self.direccion = direccion
    

class Administrador(Usuario):
    """Clase que representa un administrador de la tienda."""

    def is_admin(self) -> bool:
        """
        Indica que este usuario es administrador.

        Returns:
            bool: True
        """
        return True
    