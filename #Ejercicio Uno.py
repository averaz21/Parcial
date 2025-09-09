
#Ejercicio Uno
def main():
    while True:
        try:
            n = int(input("Ingrese un número: "))
            if n <= 0:
                print("Debe ser positivo")
                continue
            
            primos = []
            for num in range(2, n + 1):
                es_primo = True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        es_primo = False
                        break
                if es_primo:
                    primos.append(num)
            
            print("Primos:", primos)
            print("Total:", len(primos))
            
            otra = input("¿Desea ingresar otro número? (s/n): ")
            if otra.lower() != 's':
                print("Programa finalizado.")
            break
                
                
        except:
            print("Error: ingrese número válido")

if __name__ == "__main__":
    main()