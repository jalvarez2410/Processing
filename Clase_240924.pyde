'''
# diferencia con lsitas: Usamos llaves
estudiante ={"nombre": "Marvin", "edad":25, "peso (lbs)": 300, "altura (cm)": 200}

#print(estudiante["nombre"])

#if "edad" in estudiante:
    #print(estudiante["edad"])
    
estudiante["edadd"]= "19/12"
#print(estudiante)

del estudiante["edadd"]
#del estudiante
print(estudiante)


estudiantes= {
        "nombres": ["Marvin", "Ronaldo", "Pedro"],
        "carnets": ["2352", "2654", "7894"],
        "edad": [25,27,20]
              }

print(estudiantes["edad"][0])
'''

estudiantes= [{"nombre": "Marvin", "edad":25},
              {"nombre": "Ronaldo", "edad":30}
              ]

print(estudiantes[0] ["nombre"])
