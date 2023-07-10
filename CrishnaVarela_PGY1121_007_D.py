from os import system
system("cls")

valor=0
plat=120000
gold=80000
silv=50000

ubicacion=[]
for ubi in range (1,101):
    ubicacion.append(ubi)
asis=[None]*100

def ubicaciones():
    cantidad=0
    for i in range(100):
        print(ubicacion[i], end="\t")
        cantidad+=1
        if cantidad%10==0:
            print()

def ocupado(rut:str,ubi:int):
    if ubicacion[int(ubi)-1]!="X":
        ubicacion[int(ubi)-1]="X"
        asis[int(ubi)-1]=rut
        return True
    else:
        return False

def pausa():
    input("Presiona una tecla para continuar...")
    system("cls")

def ingreso_rut():
    if len(rut)<=8:
        print("El rut se ha ingresado correctamente")
    else: 
        print("El rut ingresado no es válido. Intentelo nuevamente")
        return ingreso_rut()
    
def verasistentes():
    for i in range(100):
        if ubicacion[i]=="X":
            print(f"{i+1}-{asis[i]}")

    
while True:
    print("""
        ***** CREATIVOS *****
    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir""")
    opc=input("Ingrese la opción que desea llevar a cabo: ")

    match opc:
        
        case "1":
            canti=0
            cant=int(input("Ingrese la cantidad de entradas que desea obtener: "))
            if cant<=3 and cant>=1:
                print("Cantidad de entradas correctas")
            else:
                print("Error. El máximo de entradas por persona es 3")
            if canti <= cant:
                canti+=1
                ubicaciones()
                print(f"""Platinum (1 al 20): ${plat}
Gold (21 al 50): ${gold}
Silver (51 al 100): ${silv}""")
                ubi=(input("Ingrese la o las ubicaciones que desea obtener: "))
                rut=input("Ingrese su rut sin puntos ni dígito verficador: ")
                ingreso_rut()
                if ocupado(rut,ubi):
                    print("Ubicaciones reservadas")
                    pausa()
                else:
                    print("No se ha podido reservar")
                    pausa()

        case "2":
            ubicaciones()

        case "3":
            verasistentes()
        case "4":
            if ubi>=1 and ubi<=20:
                print(f"""
        Tipo de Entrada: Platinum ${plat}
        Catidad: {cant}
        Total {plat*cant}""")
            elif ubi>=21 and ubi<=50:
                print(f"""
        Tipo de Entrada: Gold ${gold}
        Catidad: {cant}
        Total {gold*cant}""")
            else:
                print(f"""
        Tipo de Entrada: Silver ${silv}
        Catidad: {cant}
        Total {silv*cant}""")

        case "5":
            print("Saliendo del programa...")
            break
        case "other":
            pass