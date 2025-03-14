import generador_password as gen

def main():
    print("Generador de Password a partir de dos palabras")
    palabra1 = input("Introduzca la primera palabra: ").strip().lower()
    palabra2 = input("Introduzca la segunda palabra: ").strip().lower()
    print(f"En total tiene {str(len(palabra1)+len(palabra2))} caracteres")
    mezclar = gen.solicitar_entrada("¿Desea mezclar caracteres (s/n)? Esto hace que la password sea menos fácil de recordar (por defecto no): ", ['s','n'], 'n')     
    sustituir = gen.solicitar_entrada("¿Desea sustituir caracteres (s/n)? Por ejemplo: a -> @, i -> 1 ... (por defecto no): ", ['s','n'], 'n') 
    alternar = gen.solicitar_entrada("¿Desea alternar entre mayusculas y minusculas (s/n)? Por ejemplo: PaLaBrA ... (por defecto si): ", ['s','n'], 's')

    try:
        caracteres_extra = int(input("¿Desea añadir caracteres adicionales? Introduzca un número par en caso afirmativo (por defecto 2): ") or 2)
    except ValueError:
        print("Error: Número de caracteres adicionales tiene que ser un número. Utilizando valor por defecto (2)")
        caracteres_extra = 2

    print(f"Caracteres adicionales seleccionados: {str(caracteres_extra)}")

    if mezclar == "n":
        password = gen.genera_password(palabra1, sustituir, alternar, caracteres_extra // 2) + gen.genera_password(palabra2, sustituir, alternar, caracteres_extra - caracteres_extra // 2)
    else:
        palabra = gen.mezclar_caracteres(palabra1, palabra2)
        password = gen.genera_password(palabra, sustituir, alternar, caracteres_extra)

    print(f"Password generada: {password}")
    print("Guardela en lugar seguro. Cuando lo desee, presione Enter para salir")
    input()

if __name__ == "__main__":
    main()