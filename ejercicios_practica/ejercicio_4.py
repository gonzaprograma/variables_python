# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese tres palabras y arme un acrónimo con ellas
# Si desea puede modificar el código para ingresar más palabras
print('Ingrese palabra 1:', 'ASOCIACION del')
palabra_1 = str(input())

print('Ingrese palabra 2:', 'FUTBOL')
palabra_2 = str(input())

print('Ingrese palabra 3:', 'ARGENTINO')
palabra_3 = str(input())

# De cada palabra debe tomar la primera letra y armar el acrónimo
# Ejemplo: Alumbrado, barrido y limpieza --> ABL

PRIMER_LETRA1 = palabra_1 [0] 
PRIMER_LETRA2= palabra_2 [0]
PRIMER_LETRA3 = palabra_3 [0]

ACRONIMO = PRIMER_LETRA1 + '.' + PRIMER_LETRA2 + '.' + PRIMER_LETRA3


# Imprimir el resultado en pantalla

print('el acronimo de ASOCIACION DEL FUTBOL ARGENTINO es:', ACRONIMO)