saludo= "What's up?"
#print(saludo)
nombre= "Marvin"
tiempo= "Buenas noches"

#Funciones: len, count, find, strings
#text= escribir en la pantalla

#print(6/3)

#print("Hola"/3)

#saludo2= saludo +' '+ nombre
#print(saludo2)

#saludo2='Bienvenido {}'.format(nombre)
#print(saludo2)

#print(len(saludo))

#sitio= "https://miumg.edu.gt"
#print(len(sitio))
#print(sitio[-6:])
#print(sitio.count("g"))

#print(sitio.find("umg"))


size(900,400)
background("#004477")
fill("#FFFFFF")
stroke("#0099FF")
strokeWeight(3)
textSize(20)
#print(PFont.list())
fuente= createFont("Arial", 20)
textFont(fuente)
textAlign(CENTER) #LEFT, RIGHT, CENTER

#nombre="Marvin"
#text(nombre, 100,100)


nombre="Marvin Ronaldo Palma Rojas"
longitud= len(nombre)
conteo= nombre.count("a")
texto="{} tiene una extención de {} caracteres".format(nombre, longitud)
texto2="Tambien posee {} letras \'a\' dentro del nombre".format(conteo)
text(texto, 300, 100)
text(texto2, 300,200)
