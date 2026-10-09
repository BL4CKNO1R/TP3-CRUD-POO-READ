class Videojuego:
    def __init__(self, codigo, titulo, genero, plataforma, anio, horas_estimadas):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.plataforma = plataforma
        self.anio = anio
        self.horas_estimadas = horas_estimadas

    def mostrar_datos(self):
        print(f"Codigo: {self.codigo}")
        print(f"Titulo: {self.titulo}")
        print(f"Genero: {self.genero}")
        print(f"Plataforma: {self.plataforma}")
        print(f"Anio: {self.anio}")
        print(f"Horas estimadas: {self.horas_estimadas}")

    def es_del_genero(self, genero):
        return self.genero.lower() == genero.lower()

    def supera_horas(self, cantidad):
        return self.horas_estimadas > cantidad

videojuegos = [
    Videojuego(1, "Silent Hill 2", "Terror", "PC", 2024, 16),
    Videojuego(2, "Resident Evil 4", "Terror", "PC", 2023, 20),
    Videojuego(3, "Life is Strange", "Aventura", "PC", 2015, 14),
    Videojuego(4, "Minecraft", "Sandbox", "PC", 2011, 40),
    Videojuego(5, "Until Dawn", "Terror", "PlayStation", 2015, 10),
    Videojuego(6, "The Witcher 3", "RPG", "PC", 2015, 50),
    Videojuego(7, "Portal 2", "Puzzle", "PC", 2011, 8),
    Videojuego(8, "Red Dead Redemption 2", "Aventura", "PC", 2019, 45),
]

def buscar_por_codigo(codigo):
    for videojuego in videojuegos:
        if videojuego.codigo == codigo:
            return videojuego
    return None

# Consulta por genero usando el metodo de cada objeto.
genero_buscado = input("Ingrese el genero que desea consultar: ").strip()
cantidad_genero = 0
print("\n VIDEOJUEGOS DEL GENERO")
for videojuego in videojuegos:
    if videojuego.es_del_genero(genero_buscado):
        videojuego.mostrar_datos()
        print("--------------------")
        cantidad_genero += 1
if cantidad_genero == 0:
    print("No se encontraron videojuegos de ese genero.")

# Consulta por duracion usando el metodo de cada objeto.
try:
    horas_buscadas = float(input("\nMostrar juegos que superen cuantas horas: "))
    cantidad_horas = 0
    print("\nVIDEOJUEGOS QUE SUPERAN ESA DURACION")
    for videojuego in videojuegos:
        if videojuego.supera_horas(horas_buscadas):
            videojuego.mostrar_datos()
            print("--------------------")
            cantidad_horas += 1
    if cantidad_horas == 0:
        print("No hay videojuegos que superen esa cantidad de horas.")
except ValueError:
    print("Debe ingresar una cantidad numerica de horas.")

# Consulta individual por codigo.
try:
    codigo_buscado = int(input("\nIngrese el codigo del videojuego que desea consultar: "))
    resultado = buscar_por_codigo(codigo_buscado)
    if resultado is not None:
        print("\nVIDEOJUEGO ENCONTRADO")
        resultado.mostrar_datos()
    else:
        print("Videojuego no encontrado.")
except ValueError:
    print("El codigo debe ser un numero entero.")
