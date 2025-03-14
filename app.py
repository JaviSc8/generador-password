import generador_password as gen
import streamlit as st

def genera_password(palabra, sustituir, alternar, caracteres_extra=2):
    if sustituir:
        palabra = gen.sustituir_caracteres(palabra)

    if alternar:
        palabra = gen.alternar_mayusculas(palabra)

    caracteres_impares = caracteres_extra % 2
    
    if caracteres_extra > 1:
        parte_extra = gen.generar_caracteres_adicionales(caracteres_extra) + gen.generar_caracteres_adicionales(caracteres_impares)
    else:
        parte_extra = gen.generar_caracteres_adicionales(caracteres_extra)

    final_password = palabra + parte_extra

    return final_password

st.title("🔐 Generador de Contraseñas")

palabra1 = st.text_input("Ingrese la primera palabra:", "").strip().lower()
palabra2 = st.text_input("Ingrese la segunda palabra:", "").strip().lower()

mezclar = st.radio("¿Mezclar caracteres?", ["No", "Sí"]) == "Sí"
sustituir = st.radio("¿Sustituir caracteres (a -> @, i -> 1, etc.)?", ["No", "Sí"]) == "Sí"
alternar = st.radio("¿Alternar mayúsculas y minúsculas?", ["Sí", "No"]) == "Sí"

caracteres_extra = st.number_input("Número de caracteres adicionales:", min_value=0, max_value=10, value=2, step=2)

if st.button("Generar Contraseña"):
    if palabra1 and palabra2:
        if mezclar:
            palabra_mezclada = gen.mezclar_caracteres(palabra1, palabra2)
            password = genera_password(palabra_mezclada, sustituir, alternar, caracteres_extra)
        else:
            password1 = genera_password(palabra1, sustituir, alternar, caracteres_extra // 2)
            password2 = genera_password(palabra2, sustituir, alternar, caracteres_extra - caracteres_extra // 2)
            password = password1 + password2

        st.success(f"🔑 Contraseña generada: `{password}`")
    else:
        st.error("Por favor, ingrese ambas palabras para generar la contraseña.")

