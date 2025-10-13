import os
from time import sleep

# EJERCIO FINAL MODULO 1 - CRUD EMPRESAS
# NOMBRE : YELTSIN SOLANO DIAZ

dic_empresas = {
    '20454545':{
        'razon_social': 'EMPRESA SAC',
        'direccion':'CALLE EL SOL 123',
    }
}

ANCHO = 50

while True:
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("=" * ANCHO)
    try:
        opcion = int(input("INGRESE OPCION : "))
        if opcion < 1 or opcion > 5:
            print("Opción inválida. Ingrese un número del 1 al 5.")
            input("Presione ENTER para continuar...")
            continue
    except ValueError:
        print("Opción inválida. Ingrese un número del 1 al 5.")
        input("Presione ENTER para continuar...")
        continue
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("=" * ANCHO)

        ruc = input("Ingrese RUC: ")
        razon_social = input("Ingrese Razón Social: ")
        direccion = input("Ingrese Dirección: ")

        dic_nueva_empresa = {
            'razon_social': razon_social,
            'direccion': direccion
        }
        dic_empresas[ruc] = dic_nueva_empresa
        print("Empresa registrada exitosamente.")

    if opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESAS")
        print("=" * ANCHO)

        if not dic_empresas:
            print("No hay empresas registradas.")
        else:
            for ruc, info in dic_empresas.items():
                print(f"RUC        : {ruc}")
                print(f"Razón Social: {info['razon_social']}")
                print(f"Dirección  : {info['direccion']}")
                print("*" * ANCHO)

    if opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR EMPRESA")
        print("=" * ANCHO)

        ruc = input("Ingrese RUC de la empresa a actualizar: ")
        if ruc in dic_empresas:
            print(f"Empresa encontrada: {dic_empresas[ruc]['razon_social']}")
            nuevo_razon = input("Ingrese nueva Razón Social (dejar en blanco para no cambiar): ")
            nueva_direccion = input("Ingrese nueva Dirección (dejar en blanco para no cambiar): ")

            if nuevo_razon:
                dic_empresas[ruc]['razon_social'] = nuevo_razon
            if nueva_direccion:
                dic_empresas[ruc]['direccion'] = nueva_direccion

            print("Empresa actualizada exitosamente.")
        else:
            print("Empresa no encontrada.")

    if opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR EMPRESA")
        print("=" * ANCHO)

        ruc = input("Ingrese RUC de la empresa a eliminar: ")
        if ruc in dic_empresas:
            del dic_empresas[ruc]
            print("Empresa eliminada exitosamente.")
        else:
            print("Empresa no encontrada.")

    if opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL SISTEMA...")
        print("=" * ANCHO)
        sleep(2)
        break

    input("Presione ENTER para continuar...")
