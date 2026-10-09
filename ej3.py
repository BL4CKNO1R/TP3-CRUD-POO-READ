class Componente:
    def __init__(self, codigo, nombre, tipo, marca, stock, ubicacion):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.stock = stock
        self.ubicacion = ubicacion

    def hay_stock(self):
        return self.stock > 0

    def mostrar_datos(self):
        print(f"Codigo: {self.codigo} | Nombre: {self.nombre} | Tipo: {self.tipo}")
        print(f"Marca: {self.marca} | Stock: {self.stock} | Ubicacion: {self.ubicacion}")

componentes = [
    Componente(1, "Resistencia 220 ohm", "Resistencia", "Genérica", 120, "Caja A1"),
    Componente(2, "LED rojo", "LED", "Lumex", 80, "Caja A2"),
    Componente(3, "Capacitor 100 uF", "Capacitor", "ElectroMax", 35, "Caja B1"),
    Componente(4, "Resistencia 1 kohm", "Resistencia", "Genérica", 200, "Caja A1"),
    Componente(5, "Arduino Uno", "Placa", "Arduino", 12, "Estante C1"),
    Componente(6, "LED verde", "LED", "Lumex", 0, "Caja A2"),
    Componente(7, "Transistor BC547", "Transistor", "MicroTech", 45, "Caja B2"),
    Componente(8, "Capacitor 10 uF", "Capacitor", "ElectroMax", 60, "Caja B1"),
    Componente(9, "Protoboard", "Placa", "Maker", 18, "Estante C2"),
    Componente(10, "Transistor 2N2222", "Transistor", "MicroTech", 25, "Caja B2"),
]

tipo_buscado = input("Ingrese el tipo de componente: ").strip().lower()
try:
    stock_minimo = int(input("Ingrese el stock minimo requerido: "))
    if stock_minimo < 0:
        print("El stock minimo no puede ser negativo.")
    else:
        cantidad_resultados = 0
        componente_mayor_stock = None

        print("\nCOMPONENTES QUE CUMPLEN LAS CONDICIONES")
        # Se recorre la lista original: no se crea una segunda lista de resultados.
        for componente in componentes:
            if componente.tipo.lower() == tipo_buscado and componente.stock >= stock_minimo:
                componente.mostrar_datos()
                print("--------------------")
                cantidad_resultados += 1

                # Comparacion manual para encontrar el mayor stock, sin max().
                if componente_mayor_stock is None or componente.stock > componente_mayor_stock.stock:
                    componente_mayor_stock = componente

        print(f"Cantidad de componentes que cumplen ambas condiciones: {cantidad_resultados}")
        if cantidad_resultados == 0:
            print("No hay componentes que cumplan las condiciones ingresadas.")
        else:
            print("\nComponente con mayor stock entre los resultados:")
            componente_mayor_stock.mostrar_datos()
except ValueError:
    print("El stock minimo debe ser un numero entero.")
