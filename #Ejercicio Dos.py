#Ejercicio Dos
def calcular_descuento(precio, descuento=10):
    """
    Calcula el precio final después de aplicar el descuento.
    """
    precio_final = precio - (precio * descuento / 100)
    return precio_final

def main():
    total_sin_descuento = 0
    total_con_descuento = 0
    for i in range(3):  # Pedir al menos 3 precios
        precio = float(input(f"Ingrese el precio del producto {i+1}: "))
        total_sin_descuento += precio
        total_con_descuento += calcular_descuento(precio)
    
    print(f"\nValor total sin descuento: {total_sin_descuento:.2f}")
    print(f"Valor total con descuento: {total_con_descuento:.2f}")

if __name__ == "__main__":
    main()