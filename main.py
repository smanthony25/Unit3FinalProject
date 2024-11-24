# Sean A
# Recurisve tree
# Using our knowledge of turtle and recursion, make a fractal tree!

import turtle
import random as r

TURTLE_SPEED = 0
HIDE_TURTLE = True

# Tree
TREE_SIZE = 100
TREE_ANGLE = range(10, 30)
TREE_COLOR = '#4d2600'

# Leaves
LEAF_SIZE = range(10, 15)
LEAF_COLORS = ["#ff6699", "#ff99ff", "#ffb3ff", "lightpink"]

t = turtle.Turtle()


def makeTree(size):
    if size == 0:
        return
    else:
        if size == 10:
            t.pencolor(r.choice(LEAF_COLORS))
            t.pensize(r.choice(LEAF_SIZE))
        else:
            t.pencolor(TREE_COLOR)
            t.pensize(size / 10)
        t.forward(size)
        angle = r.choice(TREE_ANGLE)
        t.left(angle)
        makeTree(size - 10)
        t.pensize(size / 10)
        t.right(angle * 2)
        if size > 10:
            makeTree(size - 10)
        t.left(angle)
        t.penup()
        t.backward(size)
        t.pendown()


def main():
    screen = turtle.Screen()
    screen.setup()
    screen.bgcolor('black')
    t.color('tomato4')
    t.speed(TURTLE_SPEED)
    t.right(90)
    t.forward(50)
    t.left(180)
    if HIDE_TURTLE:
        t.ht()
    print("Generating a tree!")
    makeTree(TREE_SIZE)
    turtle.exitonclick()


if __name__ == "__main__":
    main()
