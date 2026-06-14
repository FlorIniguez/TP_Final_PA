from models.usuario import Usuario


class Socio(Usuario):
    contador =1
    def __init__(self, nombre, apellido, DNI, correo_electronico):
        super().__init__(nombre, apellido, DNI, correo_electronico)
        
        self.nro_socio = Socio.contador
        Socio.contador +=1
        
    def mostrar_info_usuario(self):
        return (
            f"Socio: {self._nombre} {self._apellido}\n"
            f"Número de socio: {self.nro_socio}"
        )
        
    def cantidad_maxima_prestamos(self):
        return 3