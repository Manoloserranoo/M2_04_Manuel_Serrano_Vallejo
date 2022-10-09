#Apartado:a
diccionario_persona={
  'Nombre' : 'Manuel',
  'Edad' : 18,
  'Género' : 'Masculino'
}

set_vehículos={"coche","camión","moto"}
#Apartado:b
print(diccionario_persona)
print(set_vehículos)
#Apartado:c
contador=1
enumeracion=1

for palabra in set_vehículos:
  if contador==2:
    print(palabra)
  contador= contador+1
#No se pueden mostrar el clave-valor de el diccionario

#Apartado:e
contador=0
for palabra in set_vehículos:
  contador= contador+1

print(contador)

enumeracion=0
for frase in diccionario_persona:
  enumeracion=enumeracion+1

print(enumeracion)
#Apartado:g
diccionario_persona['Estado']='soltero'
print(diccionario_persona)
set_vehículos.add('bicicleta')
print(set_vehículos)
#Apartado:h
del(diccionario_persona['Edad'])
print(diccionario_persona)
set_vehículos.remove('coche')
print(set_vehículos)