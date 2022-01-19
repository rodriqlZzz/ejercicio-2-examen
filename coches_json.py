import json
lista_coche = []
archivo = open('coches.txt','w')
while True:
    marca_coche = input("marca coche: ")
    archivo.write(marca_coche)
    archivo.write("\n")
    if marca_coche == "fin":
        break
    modelo = input("modelo: ")
    archivo.write(modelo)
    archivo.write("\n")
    combustible = input("tipo combustible: ")
    archivo.write(combustible)
    archivo.write("\n")
    cilindrada = input("cilindrada: ")
    archivo.write(cilindrada)
    archivo.write("\n")
    linea= {}
    linea["marca coche: "] = marca_coche
    linea["modelo: "] = modelo
    linea["combustible: "] = combustible
    linea["cilindrada: "] = cilindrada
    lista_coche.append(linea)
print("\tLista de coches:\n", lista_coche)
archivo.close()
with open('programacion.json','w') as f:
  json.dump(lista_coche,f,indent=4,sort_keys = True)
