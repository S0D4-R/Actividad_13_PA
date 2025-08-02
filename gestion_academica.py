students = {}
key = True
try:
    while key:
        print("------------Bienvenido al programa---------")
        ops = input("1.Agregar estudiante\n"
                    "2.Agregar curso con nota\n"
                    "3.Consultar estudiante\n"
                    "4. Calcular promedio de estudiante\n"
                    "5. Verificar si aprueba\n"
                    "6. Mostrar todos los estudiantes\n"
                    "7. Salir del programa\n\n"
                    "Escoja una opción: ")
        match ops:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass

except ValueError:
    print("Eso no es un número")