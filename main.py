import turtle
import random

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle")
turtle_screen.setup(600,600)
#Keeping the score
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0,260)
score_display.color("black")
score_display.write(f"Score: {score}",align="center",font=("Arial",24,"normal"))
#Score update
def score_update():
    score_display.clear()
    score_display.write(f"Score: {score}",align="center",font=("Arial",24,"normal"))
#Screen timer countdown
time_turtle = turtle.Turtle()
time_turtle.hideturtle()
time_turtle.color("black")
time_turtle.penup()
time_turtle.goto(0,234)
time_turtle.write("Time 10",align="center",font=("Arial",24,"normal"))

countdown = 10
#Timer Update
def timer():
    global countdown
    if countdown > 0:
        countdown -= 1
        time_turtle.clear()
        time_turtle.write(f"Time: {countdown}",align="center",font=("Arial",24,"normal"))
        turtle_screen.ontimer(timer,1000)
    else:
        time_turtle.clear()
        time_turtle.write("Game over!",align="center",font=("Arial",24,"normal"))
        stop_game()
#Function to stop the game
def stop_game():
    for t in turtles:
        t.hideturtle()
    turtles.clear()
#Creating a turtle to catch
turtles = []
def random_turtle():
    if countdown > 0:
        turtle_instance = turtle.Turtle("turtle")
        turtle_instance.color("green")
        turtle_instance.penup()
        x = random.randint(-turtle_screen.window_width()//2, turtle_screen.window_width()//2)
        y = random.randint(-turtle_screen.window_height()//2, turtle_screen.window_height()//2)
        turtle_instance.goto(x,y)
        turtles.append(turtle_instance)
        turtle_instance.onclick(lambda x, y:click_turtle(turtle_instance))
        turtle_screen.ontimer(lambda: delete_turtle(turtle_instance),1000)
#Code for clicking the turtles randomly created
def click_turtle(r):
    global score
    if r.isvisible():
        r.hideturtle()
        r.clear()
        turtles.remove(r)
        score += 1
        score_update()
        random_turtle()
#Code for deleting turtles that randomly created
def delete_turtle(r):
    if r.isvisible():
        r.hideturtle()
        r.clear()
        turtles.remove(r)
        random_turtle()

random_turtle()
#Turtle that controlled by mouse
mouse = turtle.Turtle()
mouse.hideturtle()
def mouse_function(x,y):
    mouse.ondrag(None)
    mouse.setheading(mouse.towards(x,y))
    mouse.goto(x,y)
    mouse.ondrag(mouse_function)
    mouse.penup()

mouse.speed("fastest")
mouse.ondrag(mouse_function)
#end codes
timer()
turtle.mainloop()