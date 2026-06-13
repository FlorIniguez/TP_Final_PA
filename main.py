from biblioteca import Biblioteca
from gestor_prestamos import GestorPrestamos
from menu import mostrar_menu
from models.libro import Libro
from utils_patrones.fabrica_usuarios import FabricaUsuarios


def main():
    biblioteca = Biblioteca("Central", "Buenos Aires")
    biblioteca.cargar_libros_iniciales()

    gestor_prestamos = GestorPrestamos()

    while True:
        mostrar_menu()
        opcion = input("Opción: ")

        if opcion == "1":
            biblioteca.listar_libros()

        elif opcion == "2":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN (10 a 13 digitos): ")
            anio = int(input("Año: "))
            paginas = int(input("Páginas: "))

            libro = Libro(titulo, autor, isbn, anio, paginas)
            print(biblioteca.agregar_libro(libro))

        elif opcion == "3":
            isbn = input("ISBN: ")
            libro = biblioteca.buscar_libro(isbn)
            print(libro.mostrar_info_libro() if libro else "No encontrado")

        elif opcion == "4":
            isbn = input("ISBN a modificar: ")

            titulo = input("Nuevo título (ENTER para omitir): ") or None
            autor = input("Nuevo autor (ENTER para omitir): ") or None
            anio = input("Nuevo año (ENTER para omitir): ")
            paginas = input("Nuevas páginas (ENTER para omitir): ")

            anio = int(anio) if anio else None
            paginas = int(paginas) if paginas else None

            print(biblioteca.modificar_libro(isbn, titulo, autor, anio, paginas))

        elif opcion == "5":
            isbn = input("ISBN: ")
            print(biblioteca.eliminar_libro(isbn))


        elif opcion == "6":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            email = input("Email: ")

            usuario = FabricaUsuarios.crear_usuario("socio", nombre, apellido, dni, email)
            print(biblioteca.agregar_usuario(usuario))

        elif opcion == "7":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            email = input("Email: ")
            legajo = input("Legajo: ")

            usuario = FabricaUsuarios.crear_usuario(
                "bibliotecario", nombre, apellido, dni, email, legajo=legajo
            )
            print(biblioteca.agregar_usuario(usuario))

        elif opcion == "8":
            biblioteca.listar_usuarios()

        elif opcion == "9":
            dni = input("DNI usuario: ")

            nombre = input("Nuevo nombre (ENTER para omitir): ") or None
            apellido = input("Nuevo apellido (ENTER para omitir): ") or None
            email = input("Nuevo email (ENTER para omitir): ") or None

            print(biblioteca.modificar_usuario(dni, nombre, apellido, email))

        elif opcion == "10":
            dni = input("DNI: ")
            print(biblioteca.eliminar_usuario(dni))

    
        elif opcion == "11":
            isbn = input("ISBN libro: ")
            dni = input("DNI usuario: ")

            libro = biblioteca.buscar_libro(isbn)
            usuario = biblioteca.buscar_usuario(dni)

            if libro and usuario:
                print(gestor_prestamos.registrar_prestamo(usuario, libro))
            else:
                print("Libro o usuario no encontrado")

        elif opcion == "12":
            isbn = input("ISBN libro: ")

            prestamo = next(
                (p for p in gestor_prestamos.prestamos
                 if p.libro.isbn == isbn and p.esta_activo()),
                None
            )

            if prestamo:
                print(gestor_prestamos.registrar_devolucion(prestamo))
            else:
                print("Préstamo no encontrado")

        elif opcion == "13":
            prestamos = gestor_prestamos.consultar_prestamos_activos()

            if prestamos:
                for p in prestamos:
                    print(f"Libro: {p.libro.titulo} - Socio:{p.usuario.nombre} - Número de socio:{p.usuario.nro_socio}")
            else:
                print("No hay préstamos activos")

 
        elif opcion == "0":
            print("Saliendo...")
            break
        
main()