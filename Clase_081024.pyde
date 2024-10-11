'''
wait= 5000

def printAnswer():
    print("La respuesta es 42")

print("6 * 7 = ?")
delay(wait)
printAnswer()
'''

size(561,768)
art= loadImage("Van_Eyck_-_Arnolfini_Portrait.jpg")
image(art, 0, 0, width, height)

def mayusculas(txt):
    return txt.upper()

def cuadroDialogo(x, y, txt, type="Hablar"):
    #x= 190
    #y=150
    #txt= "Mira mi sombrero"
    
    txt= mayusculas(txt) #Mira mi sombrero!!!
    noStroke()
    pushMatrix()
    translate(x,y)
    fill("#FFFFFF")
    
    if type == "hablar":
    #Hacer la cola de la nube
        beginShape()
        vertex(0, 0)
        vertex(15, -40)
        vertex(35, -40)
        endShape(CLOSE)
    elif type == "pensar":
        circle(0,0,8)
        circle(10,-20,16)        

    
    
    #Realizando la burbuja
    textSize(15)
    by = -85
    bw= textWidth(txt)
    pad= 20
    rect(0, by, bw+pad*2, 45, 10)
    fill("#000000")
    textAlign(LEFT, CENTER)
    text(txt, pad, by+pad)
    
    popMatrix()
    
cuadroDialogo(190, 150, "Mira mi sombrero!!!", "hablar") #Hombre
cuadroDialogo(315, 650, "Uuufale", "pensar") #Perro
cuadroDialogo(445, 125, "Meh", "pensar") #Mujer
#cuadroDialogo(190, 150, "Guau")
