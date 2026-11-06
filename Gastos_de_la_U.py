"""ESTE ARCHIVO SE UTILIZARÁ PARA COMENZAR EL PROYECTO"""
def saludo():
    print("BIENVENIDO A TU HOJA DE GASTOS, DONDE PODRAS MANEJAR TU DINERO COMO UNIVERSITARIO")
    

"""Estructura de diccionario   
movimientos = [
    {"tipo": "ingreso", "mes": 11, "categoria": "Mesada", "descripcion": "Mesada de noviembre", "monto": 120.00},
    {"tipo": "gasto", "mes": 11, "categoria": "Comida", "descripcion": "Salida con amigos", "monto": 12.00}
]
"""
movimientos = []
Menu = ["1", "2", "3","4", "5"]
Tipos = ["gasto", "ingreso"]
Categorias_gasto = ["alimentación", "transporte", "educacion", "entretenimiento", "otros"]
Categorias_ingreso = ["mesada", "trabajo", "beca", "otros"]
Meses = list(range(1, 12))
tipos = ("ingreso", "gasto")
#Definiremos las funciones a utilizar

def pedir_tipo():
    while True:
        tipo = input("Ingresa el tipo (ingreso/gasto: )")
        if tipo in tipos:
            return tipo
        print("Dato inválido")
        
def pedir_mes():
    while True:
        mes = input("Ingresa el número del mes (1-12): ")
        if mes not in Meses:
            print("Error ingrese un mes correcto (1-12)")
        else:
            return mes
        
def pedir_categoria(tipo):
    if tipo == "gasto":
        categorias = Categorias_gasto
    else:
        categorias = Categorias_ingreso
    print("CATEGORÍAS:")
    for i in categorias:
        print(f"- {categorias}")
    while True:
        categoria = input("Escriba su categoría de las de la lista").strip().lower()
        if categoria in categorias:
            return categoria
        else:
            print("Esa categoría no esta en la lista")
            
def pedir_monto():
    while True:
        monto = float(input("Escriba en número el monto: $"))
        if monto <0:
            print("Error ese monto no es aceptable")
        else:
            return monto

def calcular_disponible(movimientos):
    disponible = 0
    for movimiento in movimientos:
        if movimiento["tipo"] == "ingreso":
            disponible += movimiento["monto"]
        else:
            disponible -= movimiento["monto"]
    return disponible

def mostrar_movimientos(lista):
    for movimiento in lista:
        print(f"Tipo de movimiento: {movimiento["tipo"]}")
        print(f"Categoría: {movimiento["categoría"].title()}")
        print(f"Descripción: {movimiento["descripcion"]}")
        print(f"Mes: {movimiento["mes"]}")
        print(f"Monto: ${movimiento["monto"]}")
        
def registrar_movimiento(movimientos):
    print("Registrar movimiento")
    tipo = pedir_tipo()
    mes = pedir_mes()
    categoria = pedir_categoria()
    descripcion = input("Descripción: ")
    monto = pedir_monto()
    
    movimiento = {
        "tipo": tipo,
        "mes": mes,
        "categoria": categoria,
        "descripcion": descripcion,
        "monto": monto,
    }
    
    movimientos.append(movimiento)
    print(f"\n{tipo.title()} registrado")
    
    print(f"\n Movimientos del mes {mes}")
    for movimiento in movimientos:
        if movimiento["mes"] == mes:
            mostrar_movimientos([movimiento])
    print(f"Dinero disponible: ${round(calcular_disponible(movimientos), 2)}")
    
    
def consultar_gastos(movimientos):
    print("\n Consultar gastos")
    mes = pedir_mes()
    filtrar = input("¿Filtrar categoria? (s/n): ").lower()
    categoria = ""
    if filtrar =="s":
        categoria = pedir_categoria("gasto")
        
    encontrados = []
    for movimiento in movimientos:
        if movimiento["tipo"] == "gasto" and movimiento["mes"] == mes:
            if categoria == "" or movimiento["categoria"] == categoria:
                encontrados.append(movimiento)
                
    if encontrados:
        mostrar_movimientos(encontrados)
        total = 0
        for movimiento in encontrados:
            total += movimiento["monto"]
        print(f"Total: ${round(total, 2)}")
    else:
        print("No has registrado nada para este mes")
        
        
def resumen_del_mes(movimientos):
    print("\n Resumen del mes")
    mes = pedir_mes()
    total_ingresos = 0
    total_gastos = 0
    gastos_cat = {}
    hubo_movimientos = False
    
    for movimiento in movimientos:
        if movimientos["mes"] == mes:
            hubo_movimientos = True
            if movimiento["tipo"] == "ingreso":
                total_ingresos += movimiento["monto"]
            else:
                total_gastos += movimiento["monto"]
                categoria = movimiento["categoria"]
                gastos_cat[categoria] = gastos_cat.get(categoria, 0) + movimiento["monto"]
    if hubo_movimientos:
        disponible = total_ingresos - total_gastos
        print(f"Ingresos: ${round(total_ingresos, 2)}")
        print(f"Gastos: $ {round(total_gastos, 2)}")
        print(f"Disponible: ${round(disponible, 2)}")
        
        print("\n Gastos por categoria: ")
        for categoria, monto in gastos_cat.items():
            porcentaje = round(monto / total_gastos * 100, 1)
            print(f"{categoria.tittle()}: ${round(monto, 2)} ({porcentaje}%)")
            
        if disponible < 0:
         print("\n Gastaste más de lo que ingresaste")   
    else:
        print("No has registrado nada para este mes")
        
        
def saludo():
    print("BIENVENIDO A TU HOJA DE GASTOS, DONDE PODRÁS MANEJAR TU DINERO COMO UNIVERSITARIO")
    
    
def mostrar_menu():
    print("\n=== MENÚ ===")
    print("1. Registrar movimiento")
    print("2. Consultar gastos")
    print("3. Resumen del mes")
    print("4. Guardar") 
    print("5. Salir")
    
def main():
    saludo()
    pass
    pass
    if movimientos:
        print("\nMovimientos orevios:")
        mostrar_movimientos(movimientos)
        print(f"Dinero disponible: ${round(calcular_disponible(movimientos), 2)}")
        
    activo = True
    while activo:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion not in Menu:
            print("Esa opcion del menú no existe")
        elif opcion == "1":
            registrar_movimiento(movimientos)
        elif opcion == "2":
            consultar_gastos(movimientos)
        elif opcion == "3":
            resumen_del_mes(movimientos)
        elif opcion == "4":
            pass
        else:
            pass
            print("Se ha cerrado el sistema.")
            activo = False   
main()                                     
            
                 
    