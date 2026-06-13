from models.bibliotecario import Bibliotecario
from models.socio import Socio

#
class FabricaUsuarios:
#Metodo estatico porque no necesito instanciarlo, solo lo uso para crear usuarios
    @staticmethod
    def crear_usuario(tipo, nombre, apellido, dni, email, nro_socio=None, legajo=None):

        if tipo.lower() == "socio":
            return Socio(nombre, apellido, dni, email)

        elif tipo.lower() == "bibliotecario":
            if legajo is None:
                raise ValueError("Falta legajo para crear Bibliotecario")
            return Bibliotecario(nombre, apellido, dni, email, legajo)