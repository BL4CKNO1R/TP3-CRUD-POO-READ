class TicketSoporte:
    def __init__(self, numero, usuario, sector, problema, prioridad, estado):
        self.numero = numero
        self.usuario = usuario
        self.sector = sector
        self.problema = problema
        self.prioridad = prioridad
        self.estado = estado

    def mostrar_datos(self):
        print(f"Numero: {self.numero}")
        print(f"Usuario: {self.usuario}")
        print(f"Sector: {self.sector}")
        print(f"Problema: {self.problema}")
        print(f"Prioridad: {self.prioridad}")
        print(f"Estado: {self.estado}")

# Lista de objetos TicketSoporte.
tickets = [
    TicketSoporte(101, "Ana", "Administracion", "No imprime", "Media", "Pendiente"),
    TicketSoporte(102, "Bruno", "Informatica", "PC no enciende", "Alta", "En proceso"),
    TicketSoporte(103, "Carla", "Biblioteca", "Problema de internet", "Alta", "Pendiente"),
    TicketSoporte(104, "Diego", "Preceptoria", "Teclado danado", "Baja", "Resuelto"),
    TicketSoporte(105, "Elena", "Laboratorio", "Falla del proyector", "Media", "Pendiente"),
    TicketSoporte(106, "Fabian", "Administracion", "No puede iniciar sesion", "Media", "En proceso"),
    TicketSoporte(107, "Gina", "Biblioteca", "Impresora sin tinta", "Baja", "Resuelto"),
    TicketSoporte(108, "Hugo", "Laboratorio", "PC lenta", "Media", "Pendiente"),
]

def buscar_ticket(numero):
    for ticket in tickets:
        if ticket.numero == numero:
            return ticket
    return None

try:
    numero_buscado = int(input("Ingrese el numero de ticket que desea consultar: "))
    resultado = buscar_ticket(numero_buscado)

    # El mensaje de error se muestra una sola vez, despues de la busqueda.
    if resultado is not None:
        print("\nTICKET ENCONTRADO")
        resultado.mostrar_datos()
    else:
        print("Ticket no encontrado")
except ValueError:
    print("Debe ingresar un numero entero valido.")

print("\nTICKETS PENDIENTES")
cantidad_pendientes = 0
for ticket in tickets:
    if ticket.estado.lower() == "pendiente":
        ticket.mostrar_datos()
        print("--------------------")
        cantidad_pendientes += 1

print(f"Cantidad de tickets pendientes: {cantidad_pendientes}")
