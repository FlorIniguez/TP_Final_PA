#Antes de agregar libro valida el ISBN
def validar_isbn(func):

    def wrapper(self, libro):
        #isdigit primero para ver que todos los digitos sean numeros
        if not libro.isbn.isdigit():
            return "ISBN inválido"
    #Validar longiud del codigo isbn
        if len(libro.isbn) not in (10, 13):
            print("ISBN debe tener 10 o 13 dígitos")

        return func(self, libro)

    return wrapper