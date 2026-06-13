from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self,nombre,apellido,dni,correo_electronico):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.correo_electronico = correo_electronico
        
    @abstractmethod
    def mostrar_info(self):
        pass
    
    @abstractmethod
    def cantidad_maxima_prestamos(self):
        pass