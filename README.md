
# 📚 Sistema de Biblioteca

## 📌 Descripción

Sistema de gestión de biblioteca desarrollado en Python utilizando Programación Orientada a Objetos.

Permite administrar libros, usuarios y préstamos mediante operaciones de alta, baja, modificación y consulta.

Se aplican patrones de diseño y conceptos de POO.

---

## 👥 Integrantes

- Marcelo Albarenque  
- Cristian Matías Torres  
- María Florencia Iñiguez Trejo  
- Lucas Juarez  

---

## 🚀 Ejecución del proyecto

### Requisitos
- Python 3.10 o superior

### Ejecutar

```bash
python main.py
---
### 📦 Funcionalidades
### 📚 Libros
Agregar libros
Listar libros
Buscar por ISBN
Modificar libros
Eliminar libros
Libros iniciales precargados
---
### 👤 Usuarios
Crear socio
Crear bibliotecario
Listar usuarios (con reporte de tipo y límite de préstamos)
Modificar usuarios
Eliminar usuarios
---
### 🔄 Préstamos
Registrar préstamo
Registrar devolución
Control de disponibilidad
Límite de préstamos por tipo de usuario
---
### 🏗️ Conceptos aplicados
Programación Orientada a Objetos (POO)
Herencia (Socio y Bibliotecario heredan de Usuario)
Polimorfismo (mostrar_info_usuario, cantidad_maxima_prestamos)
Patrón Singleton (Biblioteca)
Factory Method (creación de usuarios)
Decorador (validación de ISBN)
🧠 Notas
Sistema por consola
Libros y usuarios precargados para pruebas
