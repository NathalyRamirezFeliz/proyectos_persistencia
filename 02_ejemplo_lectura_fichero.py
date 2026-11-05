"""f=open("dias.txt","r")
linea=f.readline() #devuelve la línea completa, incluyendo el salto de línea
while linea!="": #mientras sea distinta de cadena vacía
    print(linea) #me la vuelves a imrimir
    linea=f.readline() #y garantizo que me lea todas las líneas linea a linea
f.close()
"""
with open("dias.txt","r") as f:
    linea=f.readline() #devuelve la línea completa, incluyendo el salto de línea
    while linea!="": #mientras sea distinta de cadena vacía
        print(linea) #me la vuelves a imrimir
        linea=f.readline() #y garantizo que me lea todas las líneas linea a linea
with open("dias.txt","r") as f:
    lista_dias=f.readlines() #devuelve una lista con todas las líneas del fichero
print(lista_dias)
lista_limpia=[a.strip() for a in lista_dias]
print(lista_limpia)
