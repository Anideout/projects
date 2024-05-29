def Usuario():
    try:

        Tarjeta = input("Ingrese los 8 digitos de su tarjeta uwu \n")
        password = int(input("Ingrese su contraseña uwu \n"))
        if (Tarjeta == "11111111" and password == "1234"):
            print("************************************")
            print("        ENTER THE VOIDDD            ")
            print("************************************")
            opc =1 
            while opc !=2:
                print('''\t***********MENU DE OPERACIONES VOID.... CLIENTE VOID *****************''')
                print("Selecione la opcion que deseas ")
                print("1.- Realizar un deposito! " )
                print("2.- Salir \n")
                print("**************************************************************************")

                opc2 = int(input("Selecione la opcion que deseas ! \n"))
                if opc2 == 1:
                    print("\t-------REALIZA UN DEPOSITO----------")
    except:
        print("opcion no valida! ")