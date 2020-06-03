import turtle
import time
import random
delay=0.1
#set up the screen
wn=turtle.Screen()
wn.title("Snake Game by vythik")
wn.bgcolor("light blue")
wn.setup(width=600 , height=600)
wn.tracer(0)
#Snake head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"
#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
segments =[]


#Functions
def up():
    if head.direction!="down":
        head.direction="up"
def down():
    if head.direction!="up":
        head.direction="down"
def left():
    if head.direction!="rigth":
        head.direction="left"
def right():
    if head.direction!="left":
        head.direction="right"
def move():
    
    if(head.direction=="up"):
        y=head.ycor()
        head.sety(y+20)
    if(head.direction=="down"):
        y=head.ycor()
        head.sety(y-20)
    if(head.direction=="left"):
        x=head.xcor()
        head.setx(x-20)
    if(head.direction=="right"):
        x=head.xcor()
        head.setx(x+20)
# keybord bindings
wn.listen()
wn.onkeypress(up,"w")
wn.onkeypress(down,"s")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")
#Main game loop
while True:
    wn.update()
    #Check for a collision with the border
    if(head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290):
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        #hide the segments
        for segment in segments:
            segment.goto(1000,10000)
        # Clear segmentslist
        segments.clear()
    #Check for a collision with the food
    if (head.distance(food)<20):
        #Move the food to a random place
        x= random.randint(-290,290)
        y= random.randint(-290,290)
        food.goto(x,y)

        #Add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)
    
    #Move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #Move segment 0 to where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    



    move()

    #Check fro head collision with the body segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
              #hide the segments
            for segment in segments:
                segment.goto(1000,10000)
            # Clear segmentslist
            segments.clear()




    time.sleep(delay)

wn.mainloop()