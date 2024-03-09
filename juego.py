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
        self.goto(self.xcor(),self.ycor()+self.step)
    def mover_abajo(self):
        self.goto(self.xcor(),self.ycor()-self.step)
    def mover_derecha(self):
        self.goto(self.xcor()+self.step,self.ycor())
    def mover_izquierda(self):
        self.goto(self.xcor()-self.step,self.ycor())

    def hay_contacto(self,sprite1):
        distancia = self.distance(sprite1.xcor(),sprite1.ycor())
        if distancia < 30:
            return True
        else:
            return False


player = Sprite(0,-100,10,"circle","orange")
enemigo1 =Sprite(-200,0,10,"square","red")
enemigo2 =Sprite(200,20,10,"square","red")
meta=Sprite(0,120,10,"triangle","green")

pantalla = player.getscreen()
pantalla.listen()

pantalla.onkey(player.mover_arriba,"Up")
pantalla.onkey(player.mover_abajo,"Down")
pantalla.onkey(player.mover_derecha,"Right")
pantalla.onkey(player.mover_izquierda,"Left")


total_score =0

while total_score< 3:
    if player.hay_contacto(meta):
        player.goto(0,-100)
        total_score+=1
    if player.hay_contacto(enemigo1) or player.hay_contacto(enemigo2):
        meta.hideturtle()

enemigo1.hideturtle()
enemigo2.hideturtle()


exitonclick()
