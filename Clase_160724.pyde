#Ventana
size(1200,1200);
background('#FFFFFF')
stroke('#0099FF')
strokeWeight(20)
textSize(20)

#teorema_pitagoras
pitagoras='c^2=a^2+b^2'
fill('#000000')
strokeWeight(10)
text(pitagoras, 50, 700)


ladOp='4'  #numeros opuesto
areaOp='16'
text(ladOp,950,225)
text(ladOp,1100,220)
text(areaOp,850,350)

ladAd='3'  #numeros opuesto
areaOp='9'
text(ladAd,395,800)

literala='a'
text(literala,600,625)

literalc='c'
text(literalc,610,495)

literalb='b'
text(literalb,725,450)


fill('#00BAFF') #cuadro_adyacente
stroke('#000000')
strokeWeight(3)
rect(450,650,300,300)
line(550,650,550,950) #lineas
line(650,650,650,950)
line(450,750,750,750)
line(450,850,750,850)

fill('#FFF200')   #Cuadro_opuesto
stroke('#000000')
strokeWeight(3)
rect(750,250,400,400)
#lineas_horizontales
line(750,350,1150,350)
line(750,450,1150,450)
line(750,550,1150,550)
#lineas_verticales
line(850,250,850,650)
line(950,250,950,650)
line(1050,250,1050,650)


#cuadro_hipotenusa
fill('#FF0000')
stroke('#000000')
strokeWeight(3)
quad(350,15,750,250,450,650,50,350)
