# esto es una prueba del uso de la terminal
# otra prueba mas


nombre = raw_input("¿Cual es tu nombre?")
mision = raw_input("¿cual es tu mision en la vida?")
Color = raw_input("¿Cual es tu color favorito?")

print "Entonces tu nombre es %s, tu mision en la vida es %s y tu color favorito es %s." % (nombre, mision,Color)

fl = open('prueba.ods','w')
for i in range(1000):
    fl.write(nombre+"\t"+mision+"\t"+Color+"\n")
fl.close()
#test

