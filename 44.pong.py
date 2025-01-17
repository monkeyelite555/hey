import turtle
scoretracker=turtle.Turtle()
scoretracker.speed(0)
scoretracker.pu()
scoretracker.goto(0,260)
scoretracker.ht()
lpaddlescore=0
rpaddlescore=0
def update_score(player):
    if player=='l':
        global lpaddlescore
        lpaddlescore+=1
    else:
        global rpaddlescore
        rpaddlescore+=1
    scoretracker.clear()
    scoretracker.write('Red: {} -- Blue: {}'.format(lpaddlescore, rpaddlescore),align='center',font=("Arial",24,'normal'))

def pong():
    screen=turtle.Screen()
    screen.setup(width=1000,height=600)

    ball=turtle.Turtle()
    ball.speed(40)
    ball.shape("circle")
    ball.color("red")
    ball.pu()
    ball.goto(0,0)
    ball.dx=5
    ball.dy=-5

    lpaddle=turtle.Turtle()
    lpaddle.speed(0)
    lpaddle.shape("square")
    lpaddle.color("red")
    lpaddle.shapesize(6,2)
    lpaddle.pu()
    lpaddle.goto(-400,0)
    lpaddlescore=0

    rpaddle=turtle.Turtle()
    rpaddle.shape("square")
    rpaddle.color("blue")
    rpaddle.shapesize(6,2)
    rpaddle.speed(0)
    rpaddle.pu()
    rpaddle.goto(400,0)
    rpaddlescore=0

    

    def lpaddleup():
        lpaddle.goto(-400,((lpaddle.ycor())+20))

    def lpaddledown():
        lpaddle.goto(-400,((lpaddle.ycor())-20))

    def rpaddleup():
        rpaddle.goto(400,((rpaddle.ycor())+20))

    def rpaddledown():
        rpaddle.goto(400,((rpaddle.ycor())-20))

    screen.listen()
    screen.onkeypress(lpaddleup,'w')
    screen.onkeypress(lpaddledown,'s')
    screen.onkeypress(rpaddleup,'Up')
    screen.onkeypress(rpaddledown,'Down')

    while True:
        screen.update()
        ball.setx(ball.xcor()+ball.dx)
        ball.sety(ball.ycor()+ball.dy)

        #bouncing
        if ball.ycor()>280:
            ball.sety(280)
            ball.dy *= -1
        
        if ball.ycor()<-280:
            ball.sety(-280)
            ball.dy *= -1

        if ball.xcor()>500:
            ball.goto(0,0)
            ball.dy *= -1
            update_score('l')
            continue
        elif ball.xcor()<-500:
            ball.goto(0,0)
            ball.dy *= -1
            update_score('r')
            continue

        #paddle collision
        if ((ball.xcor()>360) and 
            (ball.xcor()<370) and 
            (ball.ycor()<rpaddle.ycor()+60) and 
            (ball.ycor()>rpaddle.ycor()-60)):
            ball.setx(360)
            ball.dx *= -1

        if ((ball.xcor()<-360) and 
            (ball.xcor()>-370) and 
            (ball.ycor()<lpaddle.ycor()+60) and 
            (ball.ycor()>lpaddle.ycor()-60)):
            ball.setx(-360)
            ball.dx *= -1

pong()