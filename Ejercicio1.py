class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def constructor(a=0,b=0):
        punto = [a, b]
        return punto

    def string(punto):
        print("("+str(punto[0])+", "+str(punto[1])+")")

    def cuadrante(punto):
        if punto[0]>0 and punto[1]>0:
            print("El punto esta en el primer cuadrante")
        elif punto[0]<0 and punto[1]>0:
            print("El punto esta en el segundo cuadrante")
        elif punto[0]>0 and punto[1]<0:
            print("El punto esta en el tercer cuadrante")
        elif punto[0]<0 and punto[1]<0:
            print("El punto esta en el cuarto cuadrante")
 
