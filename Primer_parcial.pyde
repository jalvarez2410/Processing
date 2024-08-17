size(600, 600)
background('#004477')
noFill()

columna = 0
fila = 0

for i in range(1, 300):    
    stroke('#FFFFFF')
    strokeWeight(2)
    
    if int(random(2)):
        line(columna, fila+25, columna+25, fila)
        line(columna+25, fila+50, columna+50, fila+25)
    else:
        line(columna+25, fila, columna+50, fila+25)
        line(columna, fila+25, columna+25, fila+50)

    columna= columna + 50

    if i % 14 == 0:
        fila= fila + 50
        columna = 0
