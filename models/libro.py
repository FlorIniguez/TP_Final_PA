class Libro:
    def __init__(self,titulo,autor,isbn,anio_publicacion,cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.anio_publicacion = anio_publicacion
        self.cantidad_paginas = cantidad_paginas
        self.disponible = True

    def mostrar_info_libro(self):
        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"ISBN: {self.isbn}\n"
            f"Año: {self.anio_publicacion}\n"
            f"Páginas: {self.cantidad_paginas}"
        )
        
    def __str__(self):
        return f"{self.titulo} - {self.autor}"
