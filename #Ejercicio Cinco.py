#Ejercicio Cinco
def promedio_notas(estudiantes):

    if not estudiantes:
        return 0
    total = sum(estudiante["nota"] for estudiante in estudiantes)
    return total / len(estudiantes)

def mejor_estudiante(estudiantes):

    if not estudiantes:
        return None, None
    mejor = estudiantes[0]
    for estudiante in estudiantes:
        if estudiante["nota"] > mejor["nota"]:
            mejor = estudiante
    return mejor["nombre"], mejor["nota"]

def peor_estudiante(estudiantes):

    if not estudiantes:
        return None, None
    peor = estudiantes[0]
    for estudiante in estudiantes:
        if estudiante["nota"] < peor["nota"]:
            peor = estudiante
    return peor["nombre"], peor["nota"]

def main():
    estudiantes = []
    
    print("SISTEMA DE GESTIÓN DE ESTUDIANTES")
    print("Ingrese 'fin' como nombre para terminar\n")
    
    while True:
        nombre = input("Nombre del estudiante: ").strip()
        
        if nombre.lower() == 'fin':
            if len(estudiantes) == 0:
                print("Debe ingresar al menos un estudiante")
                continue
            break
        
        try:
            nota = float(input(f"Nota de {nombre} (0-5): "))
            if nota < 0 or nota > 5:
                print("La nota debe estar entre 0 y 5")
                continue
        except ValueError:
            print("Ingrese un número válido")
            continue
        
        estudiantes.append({"nombre": nombre, "nota": nota})
        print(f"Estudiante {nombre} agregado con nota {nota}\n")
    
    # Calcular resultados
    promedio = promedio_notas(estudiantes)
    mejor_nombre, mejor_nota = mejor_estudiante(estudiantes)
    peor_nombre, peor_nota = peor_estudiante(estudiantes)
    
    # Mostrar reporte
    print("\n" + "="*50)
    print("REPORTE FINAL")
    print("="*50)
    print(f"Número de estudiantes: {len(estudiantes)}")
    print(f"Promedio de notas: {promedio:.2f}")
    print(f"Mejor estudiante: {mejor_nombre} - Nota: {mejor_nota}")
    print(f"Peor estudiante: {peor_nombre} - Nota: {peor_nota}")
    print("="*50)

# Ejecutar el programa
if __name__ == "__main__":
    main()