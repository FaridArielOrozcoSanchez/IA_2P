# Hechos iniciales en un formato diferente
# Simulamos una base de hechos utilizando una lista
hechos_iniciales = [
    "mascota(gato)",
    "mascota(perro)",
    "consume(gato, pescado)",
    "existe(z, perro(z) ∧ consume(gato, z))"  # Existencia de un perro que consume gato
]

# Función para transformar a forma Skolem
def transformar_a_skolem(hechos):
    hechos_skolem = []  # Lista para almacenar los hechos en forma Skolem
    contador_skolem = 1  # Contador para las funciones Skolem

    for hecho in hechos:
        # Detectamos una expresión de existencia
        if "existe" in hecho:
            # Generamos un identificador para la función Skolem
            funcion_skolem = f"funcion_skolem_{contador_skolem}()"
            contador_skolem += 1  # Incrementamos el contador
            
            # Sustituimos el hecho existencial
            nuevo_hecho_skolem = hecho.replace("existe(z", f"{funcion_skolem}")
            hechos_skolem.append(nuevo_hecho_skolem)
        else:
            # Agregamos los hechos no existenciales sin cambios
            hechos_skolem.append(hecho)

    return hechos_skolem

# Ejemplo de uso
print("Hechos originales:")
for hecho in hechos_iniciales:
    print(hecho)

# Convertimos los hechos a forma Skolem
resultado_skolem = transformar_a_skolem(hechos_iniciales)

print("\nHechos transformados a forma Skolem:")
for resultado in resultado_skolem:
    print(resultado)
