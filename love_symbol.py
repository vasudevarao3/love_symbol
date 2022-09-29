#Love

from turtle import*

#background
bgcolor('black')

#love symbol
color('red')
pencolor('red')
pensize(5)
begin_fill()
left(50)
forward(200)
circle(75,200)
right(140)
circle(75,200)
forward(200)
end_fill()

#middle line
penup()
goto(-100,50)
color('red')
pendown()
begin_fill()
left(90)
forward(340)
right(90)
forward(5)
right(90)
forward(340)
end_fill()

#arrow at top of the middle line
penup()
goto(152,270)
color('red')
pendown()
begin_fill()
left(95)
forward(20)
left(120)
forward(20)
left(120)
forward(20)
end_fill()

# bottom shape at the bottom of arrow
penup()
goto(-80,63)
color('red')
pendown()
left(30)
begin_fill()
forward(20)
left(60)
forward(20)
end_fill()

# top shape at the bottom of arrow
penup()
goto(-115,57)
color('red')
pendown()
left(60)
begin_fill()
forward(20)
left(60)
forward(20)
end_fill()

#first name
penup()
goto(-200,-30)
pendown()
write('Name',font=('times new roman',45,'italic'))

#second name
penup()
goto(200,270)
pendown()
write('Crush',font=('times new roman',45,'italic'))

#For left I
penup()
goto(-350,-50)
pendown()
pencolor('red')
write('I ',font=('stencil std',200,'italic'))

#weds in middle of love symbol
penup()
goto(-50,120)
pencolor('white')
write('Love ',font=('times new roman',40,'italic'))

#For left U
penup()
goto(250,-50)
pendown()
pencolor('red')
write('U',font=('stencil std',200,'italic'))

#I love you
penup()
goto(-300,-200)
pendown()
pencolor('red')
write('I  LOVE  YOU...',font=('times new roman',80,'bold'))

#message
penup()
goto(-400,-300)
write('I want to live with you forever...',font=('times new roman',60,'italic'))

done()
