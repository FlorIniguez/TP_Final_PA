from models.libro import Libro
from utils_patrones.validar_isbn import validar_isbn
from utils_patrones.meta_singleton import MetaSingleton


class Biblioteca(metaclass=MetaSingleton):
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.libros = []
        self.usuarios = []

    # metodos para libros
    @validar_isbn
    def agregar_libro(self, libro):
        self.libros.append(libro)
        return "Libro agregado correctamente"

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def eliminar_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        if libro:
            self.libros.remove(libro)
            return "Libro eliminado correctamente"
        else:
            return "No existe un libro con ese ISBN"

    def modificar_libro(self, isbn,titulo=None, autor=None, anio_publicacion=None, cantidad_paginas=None):
        libro = self.buscar_libro(isbn)
        if libro:
            if titulo is not None:
                libro.titulo = titulo
            if autor is not None:
                libro.autor = autor
            if anio_publicacion is not None:
                libro.anio_publicacion = anio_publicacion
            if cantidad_paginas is not None:
                libro.cantidad_paginas = cantidad_paginas
            return "Libro modificado correctamente"
        else:
            return "No existe un libro con ese ISBN"

    def listar_libros(self):
        if self.libros:
            for libro in self.libros:
                print(libro.mostrar_info_libro())
                print("----------------------")
        else:
            print("No hay libros registrados")

    # Metodos para usuarios
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        return "Usuario agregado correctamente"

    def buscar_usuario(self, dni):
        for usuario in self.usuarios:
            if usuario.dni == dni:
                return usuario

        return None

    def modificar_usuario(self, dni,nombre=None, apellido=None, correo_electronico=None):
        usuario = self.buscar_usuario(dni)
        if usuario:
            if nombre is not None:
                usuario.nombre = nombre
            if apellido is not None:
                usuario.apellido = apellido
            if correo_electronico is not None:
                usuario.correo_electronico = correo_electronico
            return "Usuario modificado correctamente"
        else:
            return "No existe un usuario con ese DNI"

    def eliminar_usuario(self, dni):
        usuario = self.buscar_usuario(dni)
        if usuario:
            self.usuarios.remove(usuario)
            return "Usuario eliminado correctamente"
        else:
            return "No existe un usuario con ese DNI"

    def listar_usuarios(self):
        if self.usuarios:
            for usuario in self.usuarios:
                print(usuario.mostrar_info())
        else:
            print("No hay usuarios registrados")
            
    def cargar_libros_iniciales(self):
        libros_iniciales = [
            ("1984", "George Orwell", "1234567890", 1949, 328),
            ("El Hobbit", "J.R.R. Tolkien", "9876543210", 1937, 310),
            ("Fahrenheit 451", "Ray Bradbury", "1112223334", 1953, 256),
            ("Don Quijote", "Miguel de Cervantes", "5556667778", 1605, 863),
            ("Clean Code", "Robert C. Martin", "4443332221", 2008, 464),
        ]

        for titulo, autor, isbn, anio, paginas in libros_iniciales:
            libro = Libro(titulo, autor, isbn, anio, paginas)
            self.libros.append(libro)