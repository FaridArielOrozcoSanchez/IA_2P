def higher_order_function(func, value):
    """
    Esta función toma otra función y un valor, 
    y devuelve True si el resultado de la función es par, 
    False si es impar.
    """
    result = func(value)
    return result % 2 == 0

def example_function(x):
    """Ejemplo de función que devuelve el doble de x."""
    return x * 2

# Aplicación de la función de orden superior
value = 3
result = higher_order_function(example_function, value)

print(f"El resultado de aplicar la función a {value} es {'par' if result else 'impar'}.")
