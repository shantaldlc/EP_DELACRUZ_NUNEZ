# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:04:16 2024

@author: SHANTAL
"""


def leer_login():
    try:
        with open('login.txt', 'r') as f:
            login = f.read().strip()
        return login
    except FileNotFoundError:
        print("NO HAY NINGÚN USUARIO REGISTRADO CON ESTE NOMBRE")
        return


def verificar_clave():
    try:
        with open('clave.txt', 'r') as f:
            clave = f.read().strip()
        return clave
    except FileNotFoundError:
        print("NO EXISTE LA CLAVE")
        return 


def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Listar personas")
    print("2. Agregar personas")
    print("3. Salir")


def listar_personas():
    try:
     
        with open('dni.txt', 'r') as dni_file, \
             open('nombre.txt', 'r') as nombre_file, \
             open('apellido.txt', 'r') as apellido_file:
            
         
            dni_list = dni_file.read().splitlines()
            nombre_list = nombre_file.read().splitlines()
            apellido_list = apellido_file.read().splitlines()
            
          
            print("\n\tDNI\t\t\tNombre\t\tApellido")
            print("\t" + "-"*40)
            
     
            for dni, nombre, apellido in zip(dni_list, nombre_list, apellido_list):
                print(f"\t{dni}\t{nombre}\t\t{apellido}")
    except FileNotFoundError:
        print("Uno o más archivos no existen.")


def agregar_persona():
    try:

        nuevo_nombre = input("Ingrese el nombre: ").strip()
        nuevo_apellido = input("Ingrese el apellido: ").strip()
        nuevo_dni = input("Ingrese el DNI: ").strip()
        
        
        if len(nuevo_dni) != 8 or not nuevo_dni.isdigit():
            print("Error: El DNI debe tener 8 dígitos.")
            return
    
        with open('dni.txt', 'a') as dni_file, \
             open('nombre.txt', 'a') as nombre_file, \
             open('apellido.txt', 'a') as apellido_file:
            
            dni_file.write(nuevo_dni + "\n")
            nombre_file.write(nuevo_nombre + "\n")
            apellido_file.write(nuevo_apellido + "\n")
        
        print("Nueva persona agregada correctamente.")
    
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")


def login():
    user = leer_login()
    password = verificar_clave()
    
    if user is None or password is None:
        return

    intentos = 0
    while intentos < 2:
        nuevo_user = input("Ingrese su usuario: ").strip()
        nueva_password = input("Ingrese su clave: ").strip()

        if nuevo_user == user and nueva_password == password:
            print("\nUsuario y clave correctos.")
            print("Ingresando a la app...")
            
            while True:
                mostrar_menu()
                opcion = input("Seleccione una opción: ")
                
                if opcion == "1":
                    listar_personas()
                elif opcion == "2":
                    agregar_persona()
                elif opcion == "3":
                    print("Saliendo del programa...")
                    break
                else:
                    print("Opción no válida, por favor intente de nuevo.")
            return
        else:
            print(" Usuario o clave incorrectos.")
            print("Inténtelo de nuevo")
            intentos += 1

    print("Se ha alcanzado el número máximo de intentos, la app se va a cerrar...")

if __name__ == "__main__":
    login()
