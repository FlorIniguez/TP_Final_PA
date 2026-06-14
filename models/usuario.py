from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self,nombre,apellido,dni,correo_electronico):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._correo_electronico = correo_electronico
        
    @abstractmethod
    def mostrar_info_usuario(self):
        pass
    
    @abstractmethod
    def cantidad_maxima_prestamos(self):
        pass