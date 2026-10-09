class RecursoDigital:
    def __init__(self, codigo, titulo, categoria, autor, anio, disponible):
        self.codigo = codigo
        self.titulo = titulo
        self.categoria = categoria
        self.autor = autor
        self.anio = anio
        self.disponible = disponible

    def mostrar_resumen(self):
        print(f"Codigo: {self.codigo}")
        print(f"Titulo: {self.titulo}")
        print(f"Categoria: {self.categoria}")
        print(f"Autor: {self.autor}")
        print(f"Anio: {self.anio}")

        if self.disponible:
            print("Disponibilidad: Disponible")
        else:
            print("Disponibilidad: No disponible")

        print("-" * 40)


# Lista de 20 libros
biblioteca = [
    # Dexter
    RecursoDigital(1, "El oscuro pasajero", "Libro digital", "Jeff Lindsay", 2004, True),
    RecursoDigital(2, "Querido y devoto Dexter", "Libro digital", "Jeff Lindsay", 2005, False),
    RecursoDigital(3, "Dexter en la oscuridad", "Libro digital", "Jeff Lindsay", 2007, True),
    RecursoDigital(4, "Dexter by Design", "Libro digital", "Jeff Lindsay", 2008, True),
    RecursoDigital(5, "Dexter es delicioso", "Libro digital", "Jeff Lindsay", 2010, False),
    RecursoDigital(6, "Double Dexter", "Libro digital", "Jeff Lindsay", 2011, True),
    RecursoDigital(7, "Dexter's Final Cut", "Libro digital", "Jeff Lindsay", 2013, False),
    RecursoDigital(8, "Dexter Is Dead", "Libro digital", "Jeff Lindsay", 2015, True),
    # Supernatural
    RecursoDigital(9, "John Winchester's Journal", "Guia de lore", "Alex Irvine", 2011, True),
    RecursoDigital(10, "Bobby Singer's Guide to Hunting", "Manual", "David Reed", 2011, False),
    RecursoDigital(11, "The Book of Monsters, Spirits, Demons, and Ghouls", "Guia de lore", "Autores varios", 2007, True),
    RecursoDigital(12, "The Men of Letters Bestiary", "Manual", "Tim Waggoner", 2017, True),
    RecursoDigital(13, "The Mythology of Supernatural", "Libro de referencia", "Autores varios", 2009, False),
    # Coleccion Holly Jackson
    RecursoDigital(14, "A Good Girl's Guide to Murder", "Libro digital", "Holly Jackson", 2019, True),
    RecursoDigital(15, "Good Girl, Bad Blood", "Libro digital", "Holly Jackson", 2020, False),
    RecursoDigital(16, "As Good as Dead", "Libro digital", "Holly Jackson", 2021, True),
    # Smallville
    RecursoDigital(17, "Strange Visitors", "Libro digital", "Roger Stern", 2002, True),
    RecursoDigital(18, "Dragon", "Libro digital", "Alan Grant", 2004, False),
    RecursoDigital(19, "Hauntings", "Libro digital", "Nancy Holder", 2002, True),
    RecursoDigital(20, "Whodunnit", "Libro digital", "Dean Wesley Smith", 2003, False)
]


# Solicitar una palabra, autor o anio
busqueda = input("Ingrese un titulo, autor o anio para buscar: ").strip().lower()

total_coincidencias = 0
total_disponibles = 0

print("\n--- RESULTADOS DE LA BUSQUEDA ---")

if busqueda == "":
    print("Debe ingresar un dato para buscar.")
else:
    for recurso in biblioteca:

        # Buscar en el titulo, autor o anio
        if (
            busqueda in recurso.titulo.lower()
            or busqueda in recurso.autor.lower()
            or busqueda in str(recurso.anio)
        ):
            recurso.mostrar_resumen()

            total_coincidencias += 1

            if recurso.disponible:
                total_disponibles += 1

    if total_coincidencias == 0:
        print("No se encontraron recursos que coincidan con la busqueda.")
    else:
        print(f"Cantidad total de coincidencias: {total_coincidencias}")
        print(f"Cantidad de recursos disponibles: {total_disponibles}")