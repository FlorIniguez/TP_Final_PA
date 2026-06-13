from datetime import date
from typing import List

from models.prestamo import Prestamo


class GestorPrestamos:
    def __init__(self):
        self.prestamos =[]
        
    def registrar_prestamo(self, usuario, libro):
        if not libro.disponible:
            return "El libro no está disponible"
    # Verificar si el libro ya está prestado
        for prestamo in self.prestamos:
            if prestamo.libro.isbn == libro.isbn and prestamo.esta_activo():
                return "El libro ya se encuentra prestado"
        # Contar préstamos activos del usuario
        prestamos_activos = 0
        for prestamo in self.prestamos:
            if prestamo.usuario == usuario and prestamo.esta_activo():
                prestamos_activos += 1
        if prestamos_activos >= usuario.cantidad_maxima_prestamos():
            return "El usuario alcanzó el límite de préstamos"
        
        nuevo_prestamo = Prestamo(usuario,libro,date.today(),None)
        self.prestamos.append(nuevo_prestamo)
        libro.disponible = False
        return "Préstamo registrado correctamente"
    
    def registrar_devolucion(self, prestamo):
        if prestamo.esta_activo():
            prestamo.fecha_devolucion = date.today()
            prestamo.libro.disponible = True
            return "Devolución registrada correctamente"
        else:
            return "El préstamo ya fue devuelto"
        
    def consultar_prestamos_activos(self):
        prestamos_activos = []
        for prestamo in self.prestamos:
            if prestamo.esta_activo():
                prestamos_activos.append(prestamo)
        return prestamos_activos