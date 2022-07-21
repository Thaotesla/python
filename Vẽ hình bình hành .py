#!/usr/bin/env python
# coding: utf-8

# In[1]:


xa=0
ya=0
xb=100
yb=0
xc=0
yc=200
xd=xc-xb+xa
yd=yc-yb+ya
print('d (',xd,yd,')')


# In[ ]:


import turtle
t=turtle.Turtle()

t.shape('turtle')
t.hideturtle()
t.pensize(2)
t.fillcolor('green')
t.begin_fill()
t.goto(xa,ya)
t.end_fill
t.goto(xb,yb)
t.goto(xc,yc)
t.goto(xd,yd)
t.goto(xa,ya)
t.right(180)
t.fillcolor('green')
t.begin_fill()
t.circle(5)
t.end_fill()
turtle.done()

