size(800,800)
noFill()
noStroke()
grid= loadImage("grid.png")
image(grid,0,0)
grido= loadImage("grid-overlay.png")
translate(150,100)
'''rotate(QUARTER_PI)
scale(0.4)
shearY(QUARTER_PI)
shearY(QUARTER_PI)



image(grido,0,0)
fill("#FF0000")
square(0,0,100)
fill("#FFFF00")
square(100,0,100)
translate(100,0)'''

pushMatrix()
shearY(QUARTER_PI)
image(grido,0,0)
fill("#FF0000")
square(0,0,100)
popMatrix()

pushMatrix()
translate(100,0)
image(grido,0,0)
fill("#FFFF00")
square(0,0,100)
popMatrix()
