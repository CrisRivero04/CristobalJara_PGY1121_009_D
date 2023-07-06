import funciones as fn

fn.ver_menu_concierto()
while True:
    opcion = fn.validar_opcion()
    if opcion==1:
        fn.comprar()
    elif opcion==2:
        fn.ver_asiento()
    elif opcion==3:
        fn.ver_asistentes()
    elif opcion==4:
        fn.ganancias()
    else:
        print("Cristobal Jara, 06/07/2023")
        

