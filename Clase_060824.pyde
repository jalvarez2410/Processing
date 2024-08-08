size(1000, 1000)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(2)

linea=0
espacio=5

for linea in range(13):
    line(width/10, height/5+(linea+linea)*12, width/3, height/10+(linea+linea)*12)
    
       
for linea in range(13):
    if linea % 2 > 0:
        line(width/1.5, height/5+28*linea, width/1.2, height/8+28*linea)
    else:
        line(width/1.2, height/5.3+28*linea, width/1.03, height/4.3+28*linea)
        
        
for linea in range(1,9):
    line(width/2.5, height/11+espacio, width/1.6, height/5+espacio)
    espacio *= 1.63
