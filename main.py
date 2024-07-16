from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=600, height=400)
screen.bgpic(
    "empty-racing-track-top-view-background-vector-illustration_530733-1647-ezgif.com-avif-to-gif-converter.gif")
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a Color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def create_turtle(body_color, x, y):
    turtle_obj = Turtle(shape="turtle")
    turtle_obj.color(body_color)
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    return turtle_obj


turtle_y_pos = -100
all_turtles = []
for color in colors:
    new_turtle = create_turtle(body_color=color, x=-230, y=turtle_y_pos)
    all_turtles.append(new_turtle)
    turtle_y_pos += 30

is_race_on = True if user_bet else False
while is_race_on:
    for t in all_turtles:
        distance = random.randint(1, 10)
        t.forward(distance)
        if t.xcor() > 230:
            win_color = t.fillcolor()
            if win_color == user_bet:
                print(
                    f"You won the bet! {win_color.capitalize()} is the winner. ")
            else:
                print(
                    f"You lost the bet! {win_color.capitalize()} is the winner. ")
            is_race_on = False


screen.exitonclick()
