def setup ():
    size(600,600)
    frameRate(1)
    noFill()
    stroke('#FFFFFF')
    
def draw():
    background("#004477")
    h= hour()
    m= minute()
    s= second()
    print("{}:{}:{}".format(h,m,s))
    translate(width/2, height/2)
    strokeWeight(3)
    circle(0,0,350)
    rotate(-HALF_PI)

#Manecillas hora
    pushMatrix()
    rotate(TAU/12 * h)
    strokeWeight(10)
    line(0,0,100,0)
    popMatrix()

#Manecillas minuto
    pushMatrix()
    rotate(TAU/60 * m)
    strokeWeight(5)
    line(0,0,125,0)
    popMatrix()

#Manecillas segundo
    pushMatrix()
    rotate(TAU/60 * s)
    strokeWeight(1)
    line(0,0,145,0)
    popMatrix()
    
