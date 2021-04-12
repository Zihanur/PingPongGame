import turtle

window = turtle.Screen()
window.setup(800,600)
window.bgcolor("yellow")
window.title("Ping Pong Game")
window.tracer(0)

madrab1 = turtle.Turtle()
madrab1.shape("square")
madrab1.shapesize(5,1)
madrab1.color("black")
madrab1.penup()
madrab1.goto(-350,0)

madrab2 = turtle.Turtle()
madrab2.shape("square")
madrab2.shapesize(5,1)
madrab2.color("black")
madrab2.penup()
madrab2.goto(350,0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

def madrab1_up():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)

def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)

window.listen()
window.onkeypress(madrab1_up,"s")
window.onkeypress(madrab1_down,"z")
window.onkeypress(madrab2_up,"Up")
window.onkeypress(madrab2_down,"Down")


while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1


    if ((ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40)):
        ball.setx(340)
        ball.dx *= -1

    if ((ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() -40)):
        ball.setx(-340)
        ball.dx *= -1