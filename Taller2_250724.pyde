#1 Inicialización
#1.1 Configurar la ventana de Processing
size(1000,800) #Se crea una ventana con un tamaño determinado
background("#00477") #Se colorea el fondo
textSize(20) # Se define el tamaño del texto de la pantalla

#2 Entrada de usuario
nombre= "Manzana" #Se define una variable para guardar un string
text(nombre, 200, 200) #Se imprime en la pantalla la variable

#3 Manipulaciones de la cadena
text(nombre.upper(), 200, 300) #Se asigna todo en mayúscula
text(len(nombre), 200, 400)#se cuenta el número de caracteres
text(nombre[0:3], 200, 500) # Se cuentan los primeros tres caracteres

#4 Visualización
