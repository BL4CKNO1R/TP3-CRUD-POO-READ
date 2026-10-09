class Reparacion:
    def __init__(self, orden, cliente, equipo, falla, estado, tecnico, costo_estimado):
        self.orden = orden
        self.cliente = cliente
        self.equipo = equipo
        self.falla = falla
        self.estado = estado
        self.tecnico = tecnico
        self.costo_estimado = costo_estimado

    def mostrar_datos(self):
        print(f"Orden: {self.orden}")
        print(f"Cliente: {self.cliente}")
        print(f"Equipo: {self.equipo}")
        print(f"Falla: {self.falla}")
        print(f"Estado: {self.estado}")
        print(f"Tecnico: {self.tecnico}")
        print(f"Costo estimado: ${self.costo_estimado:.2f}")

reparaciones = [
    Reparacion(1001, "Ana Gomez", "Notebook", "No enciende", "Pendiente", "Lucas", 35000),
    Reparacion(1002, "Bruno Diaz", "PC de escritorio", "Falla de disco", "En proceso", "Micaela", 48000),
    Reparacion(1003, "Carla Ruiz", "Tablet", "Pantalla rota", "Finalizada", "Lucas", 62000),
    Reparacion(1004, "Diego Paz", "Notebook", "Teclado danado", "Pendiente", "Sofia", 22000),
    Reparacion(1005, "Elena Gil", "Monitor", "Sin imagen", "En proceso", "Micaela", 30000),
    Reparacion(1006, "Fabian Soto", "PC de escritorio", "Sobrecalentamiento", "Finalizada", "Lucas", 18000),
    Reparacion(1007, "Gina Vera", "Notebook", "Bateria defectuosa", "Pendiente", "Sofia", 27000),
    Reparacion(1008, "Hugo Leon", "Impresora", "No toma papel", "En proceso", "Micaela", 15000),
    Reparacion(1009, "Ines Mora", "Tablet", "No carga", "Finalizada", "Sofia", 12000),
    Reparacion(1010, "Juan Rey", "Monitor", "Colores incorrectos", "Pendiente", "Lucas", 25000),
]

def buscar_por_orden(numero):
    for reparacion in reparaciones:
        if reparacion.orden == numero:
            return reparacion
    return None

def filtrar_por_estado(estado):
    cantidad = 0
    for reparacion in reparaciones:
        if reparacion.estado.lower() == estado.lower():
            reparacion.mostrar_datos()
            print("--------------------")
            cantidad += 1
    if cantidad == 0:
        print("No se encontraron reparaciones con ese estado.")

def filtrar_por_tecnico(tecnico):
    cantidad = 0
    for reparacion in reparaciones:
        if reparacion.tecnico.lower() == tecnico.lower():
            reparacion.mostrar_datos()
            print("--------------------")
            cantidad += 1
    if cantidad == 0:
        print("No se encontraron reparaciones asignadas a ese tecnico.")


def filtrar_por_costo(limite):
    cantidad = 0
    for reparacion in reparaciones:
        if reparacion.costo_estimado <= limite:
            reparacion.mostrar_datos()
            print("--------------------")
            cantidad += 1
    if cantidad == 0:
        print("No hay reparaciones con un costo igual o inferior al limite.")


def mostrar_todas():
    for reparacion in reparaciones:
        reparacion.mostrar_datos()
        print("--------------------")


while True:
    print("\nMENU DE CONSULTAS DE REPARACIONES")
    print("1. Mostrar todas las reparaciones")
    print("2. Buscar por orden")
    print("3. Filtrar por estado")
    print("4. Filtrar por tecnico")
    print("5. Filtrar por costo maximo")
    print("6. Salir")

    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "1":
        mostrar_todas()
    elif opcion == "2":
        try:
            numero = int(input("Ingrese el numero de orden: "))
            resultado = buscar_por_orden(numero)
            if resultado is not None:
                resultado.mostrar_datos()
            else:
                print("Reparacion no encontrada.")
        except ValueError:
            print("La orden debe ser un numero entero.")
    elif opcion == "3":
        estado = input("Ingrese el estado (Pendiente, En proceso o Finalizada): ").strip()
        filtrar_por_estado(estado)
    elif opcion == "4":
        tecnico = input("Ingrese el nombre del tecnico: ").strip()
        filtrar_por_tecnico(tecnico)
    elif opcion == "5":
        try:
            limite = float(input("Ingrese el costo maximo: "))
            filtrar_por_costo(limite)
        except ValueError:
            print("El costo debe ser numerico.")
    elif opcion == "6":
        print("Fin del programa. No se modificaron los registros.")
        break
    else:
        print("Opcion invalida. Seleccione un numero del 1 al 6.")
