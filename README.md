# Generador de Passwords

Este proyecto realizado para practicar con lenguaje Python, es un generador de Passwords a partir de dos palabras ingresadas por el usuario. 

Permite varias opciones de personalización para fortalecer la password generada, incluyendo la sustitución de caracteres, la alternancia entre mayúsculas y minúsculas, y la adición de caracteres adicionales.

## Características

- **Sustitución de caracteres**: Sustituye ciertos caracteres por otros para hacer la password más segura (e.g., 'a' por '@', 'i' por '1').
- **Alternancia de mayúsculas y minúsculas**: Alterna entre mayúsculas y minúsculas en la password generada.
- **Mezcla de caracteres**: Mezcla los caracteres de dos palabras ingresadas.
- **Adición de caracteres adicionales**: Agrega caracteres adicionales seleccionados aleatoriamente de dos conjuntos predefinidos.

## Uso

Para usar este generador de passwords, simplemente ejecuta el script `cli.py` o ejecuta `start_windows.bat` o `start_bash.sh` según tu sistema operativo y sigue las instrucciones en la consola.

Si prefieres usarlo directamente desde web puedes hacerlo en https://generador-password-javisc8.streamlit.app

### Ejecución (CLI)

1. Clona este repositorio:
    ```bash
    git clone https://github.com/JaviSc8/generador-password.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd generador-password
    ```
3. Ejecuta el script:
    Windows, ejecuta start_windows.bat o introduce en una consola:
    ```bash
    python cli.py
    ```
    Linux, ejecuta start_linux.sh o introduce en un terminal:
    ```bash
    python3 cli.py
    ```

### Instrucciones

1. Introduce la primera palabra.
2. Introduce la segunda palabra.
3. Responde si deseas mezclar los caracteres de las dos palabras (opcional).
4. Responde si deseas sustituir ciertos caracteres por otros (opcional).
5. Responde si deseas alternar entre mayúsculas y minúsculas (opcional).
6. Introduce el número de caracteres adicionales a agregar (opcional).

### Ejemplo

```shell
Generador de Password a partir de dos palabras
Introduzca la primera palabra: ejemplo
Introduzca la segunda palabra: seguro
En total tiene 13 caracteres
¿Desea mezclar caracteres (s/n)? Esto hace que la password sea menos fácil de recordar (por defecto no): s
¿Desea sustituir caracteres (s/n)? Por ejemplo: a -> @, i -> 1 ... (por defecto no): s
¿Desea alternar entre mayusculas y minusculas (s/n)? Por ejemplo: PaLaBrA ... (por defecto si): s
¿Desea añadir caracteres adicionales? Introduzca un número par en caso afirmativo (por defecto 2): 4
Caracteres adicionales seleccionados: 4
Password generada: 3$J339MuPrL00!4.5
Guardela en lugar seguro. Cuando lo desee, presione Enter para salir
