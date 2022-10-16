import math
import py

class punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def string(self):
        return "({}, {})".format(self.x, self.y)

    def cuadrante(self):
        if self.x >0 and self.y >0:
            print("en el primer cuadrante")
        elif self.x<0 and self.y>0:
            print("en el segundo cuadrante")
        elif self.x>0 and self.y<0:
            print("en el tercer cuadrante")
        elif self.x<0 and self.y<0:
            print("en el cuarto cuadrante")
        else:
            print("en el origen")

    def vector(self, punto_2):
        punto_2 = punto_2.x - self.x, punto_2.y - self.y
        print(punto_2)

    def distancia(self, punto_3):
        distancia = math.sqrt((punto_3.x - self.x)**2 + (punto_3.y - self.y)**2)
        print(distancia)


A = (2, 3)
B = (5,5)
C = (-3, -1)
D = (0,0)

print("El punto A es", A)
print("El punto B es",B)
print("El punto C es",C)
print("El punto D es",D)

A = punto(2, 3)
B = punto(5,5)
C = punto(-3, -1)
D = punto(0,0)
    
print("El punto A se encuentra:")    
A.cuadrante()
print("El punto C se encuentra") 
C.cuadrante()
print("El punto D se encuentra") 
D.cuadrante()

print("El vector de punto AB es:")
A.vector(B)
print("El vector de punto BA es:")
B.vector(A)

print("La distancia entre A y B es:")
A.distancia(B)
print("La distancia entre B y A es:")
B.distancia(A)