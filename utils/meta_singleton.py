#Metraclase y singleton
# MetaSingleton hereda de type.
# Así como type() permite crear clases dinámicamente, esta metaclase
# controla cómo se crean las instancias de las clases que la utilizan.
class MetaSingleton(type):
    # Diccionario donde se guardan las instancias creadas
    _instancias = {}
# Se ejecuta cada vez que se intenta crear una instancia  de una clase que utiliza esta metaclase.
    def __call__(cls, *args, **kwargs):
        # Si la clase todavía no tiene una instancia, la crea
        if cls not in cls._instancias:
            cls._instancias[cls] = super().__call__(*args, **kwargs)
        # Devuelve siempre la misma instancia
        return cls._instancias[cls]