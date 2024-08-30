'''y=1

def setup():
    y=0
    print(y)
    frameRate(1)
def draw():
    global y
    y+=1
    print(y)
    '''
    
y=0

def setup():
    size(500,500)
    background("#004477")
    noFill()
    stroke('#FFFFFF')
    strokeWeight(3)
def draw():
    global y 
    y +=1
    background("#004477")
    circle(width/2, y, 50)
    if frameCount == 200:
        saveFrame("captura.png")
