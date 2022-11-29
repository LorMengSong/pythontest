import turtle
mengsong = turtle.Turtle();
mengsong.speed(10)
turtle.bgcolor("red");
for i in range(180):
    mengsong.forward(100)
    mengsong.right(30)
    mengsong.forward(20)
    mengsong.left(60)
    mengsong.forward(50)
    mengsong.right(30)

    mengsong.penup();
    mengsong.setposition(0,0)
    mengsong.pendown()
    mengsong.right(2)
    turtle.down()