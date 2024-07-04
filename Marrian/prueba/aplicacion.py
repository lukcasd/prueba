import Ma_funciones

listado_A = []

while True:
    opcion = Ma_funciones.menu_menu()

    if opcion == 1:
        Ma_funciones.registro_pedido(listado_A)

    elif opcion == 2:
        Ma_funciones.lista_cliente(listado_A)

    elif opcion == 3:
        print()