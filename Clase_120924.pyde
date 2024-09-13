#inventario= ['llaves', 8, 45]
#arcoiris= ["azul","anaranjado","amarillo","verde","negro"]
#print(arcoiris)

#arcoiris[1]= "morado"
#print(arcoiris)

#arcoiris.append("anaranjado")
#print(arcoiris)

'''colores =["violeta","celeste"]
arcoiris.extend(colores)
print(arcoiris)

indice= arcoiris.index("negro")
print(indice) 

arcoiris.insert(2, "violeta")
print(arcoiris) 

valorEliminado= arcoiris.pop(1)
print(valorEliminado)
print(arcoiris)

arcoiris.remove("verde")
print(arcoiris)
'''

size(500,500)
noStroke()
background("#004477")

bands= [
        "#FF0000", #Rojo
        "#FF9900", #Anaranjado
        "#FFFF00", #Amarillo
        "#00FF00", #Verde
        "#0099FF", #Azul
        "#6633FF", #Violeta
        ]

'''translate(0,100)
    fill(bands[0])
    rect(0, 0, width, 50)
'''

for indice, band in enumerate(bands):
   fill(band)
   rect(0,0, width, 50) 
   fill("#FFFFFF")
   textSize(25)
   text(indice, 20, 30)
   translate(0, 50)
    
