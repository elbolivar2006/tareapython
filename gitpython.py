quintil=int(input("ingrese su quintil"))
condicionlaboral=input(" ingrese su condicon laboral")
edad=int(input(" ingrese su edad"))
if quintil in [1, 2] and condicionlaboral == "desempleado":
    subsidio = 10000
elif quintil in [1, 2] and condicionlaboral == "empleado":
    subsidio = 8000
elif quintil == 3 and condicionlaboral == "desempleado":
    subsidio = 6000
elif quintil == 3 and condicionlaboral == "empleado":
    subsidio = 4000
elif quintil in [4, 5]:
    subsidio = 1500
else:
    print("datos no validos")
if quintil in [1, 2]:
    subsidio += 2000
if edad >=65:
    subsidio += 3000
resultado=subsidio
print("segun su quintil que es", quintil , "y su condicion laboral que actualmente es", condicionlaboral,"a obtenido un subsidio de gas por el valor de", resultado)