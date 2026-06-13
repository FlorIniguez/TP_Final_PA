from models.libro import Libro
from models.usuario import Usuario


class Prestamo():
    def __init__(self, usuario: Usuario,libro: Libro,fecha_prestamo,fecha_devolucion):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
    
    def esta_activo(self):
        return self.fecha_devolucion is None
        
    def mostrar_info(self):
        estado = "Activo" if self.esta_activo() else "Devuelto"
        return (
            f"{self.usuario.nombre} {self.usuario.apellido} - "
            f"{self.libro.titulo} - "
            f"Prestado: {self.fecha_prestamo}\n"
            f"Estado: {estado}"
        )
    