import menu,random, csv

def menu_menu():
    num1_opcion = 1
    for opk in menu.pyme_menu:
        print (f"{num1_opcion} . {opk}")
        num1_opcion = +1
        while True:
            try:
                seleccion_A = int(input("seleccione una opcion: "))
                break
            except:
                print("el valor ingresado debe ser numerico")
                return seleccion_A

def generar_IDpedido():
    variable_A = random.randint(100000,999999)
    return variable_A


def registro_pedido(lista_pedido):
    codigo_pedido = generar_IDpedido()
    while True:
         nombre_cliente = input("ingrese su nombre: ").strip()
         if len(nombre_cliente)>3 and nombre_cliente.isalpha():
              break
         else:
              print("nombre no valido, porfavor intentelo nuevamente")

    while True:
         apellido_cliente = input("ingrese su apellido: ").strip()
         if len(apellido_cliente)>3 and apellido_cliente.isalpha():
              break
         else: 
              print("apellido no valido, porfavor intentelo nuevamente")
    while True:        
         direccion_cliente = input("ingrese la direccion de su domicilio: ").strip()
         if len(direccion_cliente)>3 and direccion_cliente.isalpha():
              break
         else:
              print("direccion no valido, porfavor intentelo nuevamente")

    comuna_cliente = input("ingrese la comuna en la que recide: ")

    dispensadores = input("ingrese la cantidad de litros del dispensador que desea comprar: ").isnumeric()

    cantidad_dispensadores = input("ingrese la cantidad de dispensadores que desea comprar: ").isnumeric()

    lista_pedido.append([codigo_pedido, nombre_cliente, apellido_cliente, direccion_cliente, comuna_cliente, dispensadores, cantidad_dispensadores])

def lista_cliente(lista_pedido):
        print("codigo pedido\tNombre\tApellido\tdireccion\tcomuna\tDispensador 6litros\tdispensador 10litros\tdispensador 20litros")
        for clien in lista_pedido:
             print(f"{clien[0]}\t{clien[1]}\t{clien[2]}\t{clien[3]}\t{clien[4]}\t{clien[5]}")

def planilla(lista_pedido, dispensadores, cantidad_dispensadores):
     try:
          with open("dato.csv", "w", newline="") as archivo:
               escritor = csv.writer(archivo)
               escritor.writerow(["codigo del pedido", "nombre cliente", "apellido cliente", "direccion cliente", "direccion comuna", "dispensadores", "cantidad de dispensadores"])
               if lista_pedido and dispensadores and cantidad_dispensadores == "todos":
                    escritor.writerows(lista_pedido, dispensadores, cantidad_dispensadores)
                else:
                    for clien in lista_pedido, dispensadores, cantidad_dispensadores:
                         if clien[3] == dispensadores
                         escritor.writerow(lista_cliente)
                    print("planilla fue creada con exito")






