import turtle

def draw_square(a_turtle, size):
  for _ in range(4):
    a_turtle.forward(size)
    a_turtle.right(90)

def draw_art():
  window = turtle.Screen()
  window.bgcolor("red")
  a_turtle = turtle.Turtle()
  a_turtle.shape("turtle")
  a_turtle.color("yellow")

  for i in range(5):
    draw_square(a_turtle, (2**i)*10)

  window.exitonclick()

draw_art()
