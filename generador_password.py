import random

DICCIONARIO_SUSTITUCION = {
    'a': '@',
    'i': '1',
    'e': '3',
    'o': '0',
    's': '$',
    'g': '9',
    'b': '8',
    't': '7'
}

CARACTERES_1 = '.!#-'
CARACTERES_2 = '2456$'

def sustituir_caracteres(palabra):
    return ''.join(DICCIONARIO_SUSTITUCION.get(char, char) for char in palabra)

def mezclar_caracteres(palabra1, palabra2):
    combinacion = []

    for p1, p2 in zip(palabra1, palabra2):
        combinacion.append(p1)
        combinacion.append(p2)
    combinacion.extend(palabra1[len(palabra2):])
    combinacion.extend(palabra2[len(palabra1):])

    return ''.join(combinacion)

def alternar_mayusculas(palabra):
    return ''.join(
    char.upper() if index % 2 == 0 else char.lower()
    for index, char in enumerate(palabra)
    )

def generar_caracteres_adicionales(caracteres_extra):
    parte_extra = ''.join(random.choices(CARACTERES_1, k=caracteres_extra))

    if caracteres_extra > 1:
        caracteres_extra = caracteres_extra // 2
        parte_extra1 = parte_extra
        parte_extra2 = ''.join(random.choices(CARACTERES_2, k=caracteres_extra))
        parte_extra = ''.join([char for pair in zip(parte_extra1, parte_extra2) for char in pair])

    return parte_extra

def solicitar_entrada(prompt, opciones, default):
    while True:
        entrada = input(prompt).strip().lower()
        if entrada in opciones:
            return entrada
        elif entrada == '':
            return default
        print(f"Entrada inválida. Por favor ingrese {' o '.join(opciones)}")

def genera_password(palabra, sustituir, alternar, caracteres_extra=2):
    if sustituir == "s":
        palabra = sustituir_caracteres(palabra)

    if alternar == "s":
        palabra = alternar_mayusculas(palabra)

    caracteres_impares = caracteres_extra % 2
    
    if caracteres_extra > 1:
        parte_extra = generar_caracteres_adicionales(caracteres_extra) + generar_caracteres_adicionales(caracteres_impares)
    else:
        parte_extra = generar_caracteres_adicionales(caracteres_extra)

    final_password = palabra + parte_extra

    return final_password

def main():
    print("Generador de Password a partir de dos palabras")
    palabra1 = input("Introduzca la primera palabra: ").strip().lower()
    palabra2 = input("Introduzca la segunda palabra: ").strip().lower()
    print(f"En total tiene {str(len(palabra1)+len(palabra2))} caracteres")
    mezclar = solicitar_entrada("¿Desea mezclar caracteres (s/n)? Esto hace que la password sea menos fácil de recordar (por defecto no): ", ['s','n'], 'n')     
    sustituir = solicitar_entrada("¿Desea sustituir caracteres (s/n)? Por ejemplo: a -> @, i -> 1 ... (por defecto no): ", ['s','n'], 'n') 
    alternar = solicitar_entrada("¿Desea alternar entre mayusculas y minusculas (s/n)? Por ejemplo: PaLaBrA ... (por defecto si): ", ['s','n'], 's')

    try:
        caracteres_extra = int(input("¿Desea añadir caracteres adicionales? Introduzca un número par en caso afirmativo (por defecto 2): ") or 2)
    except ValueError:
        print("Error: Número de caracteres adicionales tiene que ser un número. Utilizando valor por defecto (2)")
        caracteres_extra = 2

    print(f"Caracteres adicionales seleccionados: {str(caracteres_extra)}")

    if mezclar == "n":
        password = genera_password(palabra1, sustituir, alternar, caracteres_extra // 2) + genera_password(palabra2, sustituir, alternar, caracteres_extra - caracteres_extra // 2)
    else:
        palabra = mezclar_caracteres(palabra1, palabra2)
        password = genera_password(palabra, sustituir, alternar, caracteres_extra)

    print(f"Password generada: {password}")
    print("Guardela en lugar seguro. Cuando lo desee, presione Enter para salir")
    input()

if __name__ == "__main__":
    main()