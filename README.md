📚 Sistema de Biblioteca
📌 Descripción

Sistema de gestión de biblioteca desarrollado en Python. Permite administrar libros, usuarios y préstamos mediante programación orientada a objetos.

El sistema permite realizar operaciones de alta, baja, modificación y consulta, además de controlar préstamos y devoluciones con validaciones de negocio.

Se aplican patrones de diseño y conceptos avanzados de POO.

👥 Integrantes
Marcelo Albarenque
Cristian Matías Torres
María Florencia Iñiguez Trejo
Lucas Juarez

🚀 Instrucciones de ejecución
Requisitos
Python 3.10 o superior
Ejecución del sistema
python main.py
📦 Funcionalidades
📚 Gestión de libros
Agregar libro
Listar libros
Buscar por ISBN
Modificar libro
Eliminar libro
Ver información de un libro
👤 Gestión de usuarios
Crear socio
Crear bibliotecario
Listar usuarios
Modificar usuario
Eliminar usuario
🔄 Préstamos
Registrar préstamo de libro
Registrar devolución
Control de disponibilidad de libros
Límite de préstamos por tipo de usuario
🏗️ Conceptos aplicados
Programación Orientada a Objetos (POO): uso de clases, objetos y encapsulación.
Herencia: Socio y Bibliotecario heredan de Usuario.
Polimorfismo: distintos comportamientos según tipo de usuario, mostrar info usuario y cantidad máxima de prestamos.
Patrones de diseño:
Singleton: clase Biblioteca
Factory Method: creación de usuarios
Decorador: validación de ISBN antes de agregar libros.
🧠 Notas
El sistema funciona por consola.
La biblioteca carga libros iniciales automáticamente.
Se controla la disponibilidad de los libros en préstamos.
El sistema evita préstamos duplicados del mismo libro.
