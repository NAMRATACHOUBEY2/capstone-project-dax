import random
import turtle

turtle.speed(0)

turtle.Screen().bgcolor("black")

def pen(colour):
    turtle.color(colour)  

pen('red')
    
def firework1(size):
    for num in range(20):
        turtle.forward(size)
        turtle.right(180-(360/20))
        
firework1(150)

def move():
    turtle.penup()
    x=random.randint(-150,150)
    y=random.randint(-150,150)
    turtle.goto(x,y)
    turtle.pendown()

move()
pen('yellow')
firework1(30)
move()
pen('blue')
firework1(57)
move()
pen('purple')
firework1(80)
move()
pen('lightblue')
firework1(120)
move()
pen('pink')
firework1(100)
move()
pen('orange')
firework1(54)
move()
pen('violet')
firework1(33)
move()
pen('green')
firework1(68)

move()
pen('light green')
firework1(29)
move()
pen('magenta')
firework1(104)
move()
pen('pink')
firework1(79)
move()
pen('lime')
firework1(160)
move()
pen('orange')
firework1(68)
move()
pen('indigo')
firework1(39)
move()
pen('neon pink')
firework1(56)
move()
pen('dark blue')
firework1(46)

move()
pen('white')
firework1(30)
move()
pen('neon pink')
firework1(57)
move()
pen('brown')
firework1(80)
move()
pen('gold')
firework1(120)
move()
pen('silver')
firework1(100)
move()
pen('pink')
firework1(54)
move()
pen('light green')
firework1(33)
move()
pen('indigo')
firework1(68)