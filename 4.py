import turtle

win=turtle.Screen()
turtle.color('white')
win.bgcolor('black')

screen = turtle.Screen()
screen.setup(600,600)
turtle.speed(6)

turtle.up()
turtle.goto(-100,-60)
turtle.down()
turtle.seth(-45)
turtle.circle(200,90)
turtle.circle(100,90)
turtle.circle(200,90)
turtle.circle(100,90)

win.mainloop()