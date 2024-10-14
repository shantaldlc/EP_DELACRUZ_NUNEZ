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

def leer_clave():
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


def login():
    user = leer_login()
    password = leer_clave()

    if user  is None or password  is None:
        return

    intentos = 0
    while intentos < 2:
        nuevo_user = input("Ingrese su login: ").strip()
        nueva_password = input("Ingrese su clave: ").strip()

        if nuevo_user == user and nueva_password == password:
            print("\nLogin y clave correctos.")
            print("Ingresando al sistema...")
            mostrar_menu()
            return
        else:
            print("Login o clave incorrectos.")
            print("Inténtelo de nuevo")
            intentos += 1

    print("Se ha alcanzado el número máximo de intentos, el sistema se va cerrar...")

if __name__ == "__main__":
    login()