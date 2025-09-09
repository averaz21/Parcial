#Ejercicio Cuatro
def main():
    while True:
        try:
            num1 = int(input("Ingrese el primer número entero: "))
            num2 = int(input("Ingrese el segundo número entero: "))
            
            resultado = num1 / num2
            print(f"La división de {num1} entre {num2} es: {resultado}")
        
        except ValueError:
            print("Error: Debe ingresar números enteros.")
        
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
        
        continuar = input("¿Desea realizar otra división? (s/n): ").strip().lower()
        if continuar != 's':
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()