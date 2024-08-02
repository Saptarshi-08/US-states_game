import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
screen.tracer(0)

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_column = data.state.to_list()
states_mentioned = []

while len(states_mentioned) < 50:
    screen.update()
    answer_state = screen.textinput(title=f"{len(states_mentioned)}/50 States Guessed",
                                    prompt="What's your guess?").title()

    if answer_state == "Exit":
        states_missed = [states for states in state_column if states not in states_mentioned]
        for state in states_missed:
            screen.update()
            state_data = data[data.state == state]
            sappy = turtle.Turtle()
            sappy.hideturtle()
            sappy.penup()
            sappy.speed("fastest")
            sappy.color("red")
            sappy.goto(int(state_data.x), int(state_data.y))
            sappy.write(state_data.state.item())
        df = pandas.DataFrame(states_missed)
        df.to_csv("missed_states.csv")
        break

    if answer_state in state_column:
        sap = turtle.Turtle()
        sap.penup()
        sap.hideturtle()
        guessed_state = data[data.state == answer_state]
        sap.goto(int(guessed_state.x), int(guessed_state.y))
        sap.write(f"{answer_state}")
        states_mentioned.append(answer_state)

screen.exitonclick()
