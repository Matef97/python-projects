#importing the graphics module turtle
import turtle
#Enter the players name
player1 = input("Enter player one name : ")
player2 = input("Enter player two name : ")

#setup the window and its specifications
window = turtle.Screen()
window.title("Ping Pong Game By Mostafa Atef")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)
#set up the first paddle
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape('square')
paddle1.color('blue')
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.penup()
paddle1.goto(-350,0)
#set up the first paddle
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape('square')
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.color('red')
paddle2.penup()
paddle2.goto(350,0)
#set up the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy =0.3

#functions
def pd1_up():
    y = paddle1.ycor()
    y+=10
    paddle1.sety(y)
def pd1_down():
    y = paddle1.ycor()
    y-=10
    paddle1.sety(y)  
def pd2_up():
    y = paddle2.ycor()
    y+=10
    paddle2.sety(y) 
def pd2_down():
    y = paddle2.ycor()
    y-=10
    paddle2.sety(y) 
 #score
score1=0
score2=0 
score = turtle.Turtle() 
score.speed()
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,270)
score.write(f"{player1} : {score1} {player2} : {score2}",align="center",font=("Times",24,"bold"))
#keyboard connection
window.listen()
window.onkeypress(pd1_up,'w')
window.onkeypress(pd1_down,'x')             
window.onkeypress(pd2_up,'l')             
window.onkeypress(pd2_down,'Down')             

while True :
    window.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if(ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle2.ycor()+40 and ball.ycor()>paddle2.ycor()-40)    :
     ball.setx(340)
     ball.dx*=-1
    if(ball.xcor()<-340 and ball.xcor()>-350 and ball.ycor()<paddle1.ycor()+40 and ball.ycor()>paddle1.ycor()-40)    :
     ball.setx(-340)
     ball.dx*=-1
    if ball.xcor()>390 :
        ball.goto(0,0)
        ball.dx*= -1
        score1+=1
        score.clear()
        score.write(f"{player1} : {score1} {player2} : {score2}",align="center",font=("Times",24,"bold"))
    if ball.ycor()>290 :
        ball.sety(290)
        ball.dy*=-1
    if ball.xcor()<-390 :
        ball.goto(0,0)
        ball.dx*= -1
        score2+=1
        score.clear()
        score.write(f"{player1} : {score1} {player2} : {score2}",align="center",font=("Times",24,"bold"))
    if ball.ycor()<-290 :
        ball.sety(-290)
        ball.dy*=-1    
    
