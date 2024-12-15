import turtle

turtle.Screen().bgcolor("Blue")

sc=turtle.Screen()
sc.setup(500, 400)

turtle.title("You are on the Turtle Window")

n=3
angle=360/n

board = turtle.Turtle()

for i in range(n):
    board.forward(50)
    board.left(angle)