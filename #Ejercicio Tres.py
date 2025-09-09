#Ejercicio Tres
def analizar_texto(*args, **kwargs):


    texto_completo = " ".join(args)
    

    contar_vocales = kwargs.get('contar_vocales', False)
    contar_palabras = kwargs.get('contar_palabras', False)
    

    if not contar_vocales and not contar_palabras:
        contar_vocales = True
        contar_palabras = True
    

    if contar_vocales:
        vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
        total_vocales = 0
        for letra in texto_completo:
            if letra in vocales:
                total_vocales += 1
        print(f"Cantidad de vocales: {total_vocales}")
    

    if contar_palabras:
        palabras = texto_completo.split()
        print(f"Cantidad de palabras: {len(palabras)}")


print("Ejemplo 1:")
analizar_texto("Hola mundo", "Python es genial", contar_vocales=True)

print("\nEjemplo 2:")
analizar_texto("la calma serena del día", "un suspiro de viento me guía", contar_palabras=True)

print("\nEjemplo 3:")
analizar_texto("Texto sin opciones especificadas")

print("\nEjemplo 4:")
analizar_texto("Y si solo quiero contar las vocales", contar_vocales=True, contar_palabras=False)

print("\nEjemplo 5:")
analizar_texto("Análisis", "completo", "de un", "texto", contar_vocales=True, contar_palabras=True)