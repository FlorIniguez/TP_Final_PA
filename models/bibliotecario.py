from models.usuario import Usuario


class Bibliotecario(Usuario):
    def __init__(self, nombre, apellido, DNI, correo_electronico,legajo):
        super().__init__(nombre, apellido, DNI, correo_electronico)
        self.legajo = legajo
        
    def mostrar_info(self):
        return (
            f"Bibliotecario: {self.nombre} {self.apellido} "
            f"Legajo: {self.legajo}"
        )

    def cantidad_maxima_prestamos(self):
        return 10