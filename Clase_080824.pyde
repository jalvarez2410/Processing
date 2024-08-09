size(600, 600)
background("#004477")
stroke("#FFFFFF")
strokeWeight(1)


#print(int(random(5,11)))
'''randomSeed(500)
for i in range(500):
    point(random(width), random(height))
   ''' 

col=0
row=0
for i in range(1,145):
    aleatorio=int(random(4))
    if aleatorio==1:
        triangle(0+col,50+row, 50+col,0+row, 50+col,50+row)
    elif aleatorio==2:
        triangle(0+col,0+row, 50+col,0+row, 0+col,50+row)
    elif aleatorio==3:
        triangle(0+col,0+row, 50+col,0+row, 50+col,50+row)
    else:
        triangle(0+col,50+row, 0+col,0+row, 50+col,50+row)
    col+=50
    if i %12==0:
        row +=50
        col=0
        
