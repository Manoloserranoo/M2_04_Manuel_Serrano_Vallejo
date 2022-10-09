#Apartado:a
equipos=["real madrid","fc barcelona","atlético","sevilla"]
frutas=("manzanas","peras","naranjas","plátanos")
#Apartado:b
print(equipos)
print(frutas)

#Apartado:c
contador=1
enumeracion=1

for palabra in equipos:
  if contador==2:
    print(palabra)
  contador= contador+1

for frase in frutas:
  if enumeracion==3:
    print(frase)
  enumeracion= enumeracion+1

#Apartado:e
contador=0
for palabra in equipos:
  contador= contador+1

print(contador)

enumeracion=0
for frase in frutas:
  enumeracion=enumeracion+1

print(enumeracion)
#Apartado:f
print(f"Quiero buscar:",equipos[2])
print(f"Quiero buscar:",frutas[3])
#Apartado:g
equipos.append("levante")
print(equipos)
#Apartado:h
equipos.pop(2)
print(equipos)
#En las tuplas no se pueden ni añadir ni eleminar elementos al contrario q en las listas ya que son estáticas.