import turtle

def draw_square(a_turtle):
  for _ in range(4):
    a_turtle.forward(100)
    a_turtle.right(90)

def draw_circle(a_turtle):
  a_turtle.circle(100)

def draw_triangle(a_turtle):
  for _ in range(3):
    a_turtle.forward(100)
    a_turtle.right(120)

def draw_art():
  window = turtle.Screen()
  window.bgcolor("red")
  a_turtle = turtle.Turtle()
  a_turtle.shape("turtle")
  a_turtle.color("yellow")
  for _ in range(36):
    draw_square(a_turtle)
    a_turtle.right(10)
  window.exitonclick()

draw_art()
