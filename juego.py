from turtle import *
class Sprite(Turtle):
    def __init__(self,x,y,step=10,shape='circle',color ="black"):
        super().__init__()
        self.penup()
        self.speed(0)   
        self.goto(x,y)
        self.color(color)
        self.shape(shape)
        self.step=step
    def mover_arriba(self):
        print("arriba")
    def mover_abajo(self):
        print("abajo")
    def mover_derecha(self):
        print("derecha")
    def mover_izquierda(self):
        print("izquierda")


player = Sprite(0,-100,10,"circle","orange")
pantalla = player.getscreen()
pantalla.listen()

pantalla.onkey(player.mover_arriba,"Up")
pantalla.onkey(player.mover_abajo,"Down")
pantalla.onkey(player.mover_derecha,"Right")
pantalla.onkey(player.mover_izquierda,"Left")

exitonclick()
