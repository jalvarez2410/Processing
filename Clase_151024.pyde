radius= 200
theta=1
period= 2.1

def circlePoint(t, r):
    x= cos(t) * r
    y= sin(t) * r
    return[x,y]

def ellipsePoint(t, hr, vr):
    x= cos(t) * hr
    y= sin(t) * vr
    return [x, y]
    

def setup():
    size(800, 600)
    
def draw():
    global theta
    theta += TAU / (frameRate * period)
    background("#004477")
    noFill()
    strokeWeight(3)
    stroke("#0099FF")
    line(width/2, height, width/2, 0)
    line(0, height/2, width, height/2)
    #invertir el eje y
    scale(1,-1)
    translate(0, -height)
    translate(width/2, height/2)
    circle(0, 0, radius*2)
    stroke("#FFFFFF")
    pushMatrix()
    rotate(theta)
    line(0, 0, radius, 0)
    popMatrix()
    
    x, y = circlePoint(theta, radius)
    circle(x, y, 15)
    
    x, y = circlePoint(theta, frameCount)
    circle(x, y, 15)
    
    x, y = ellipsePoint(theta, radius*1.5, radius)
    circle(x,y,15)
