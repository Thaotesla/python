#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Nhập toạ độ của 1 tứ giác. Lập biểu thức để kiểm tra tứ giác đó là một tứ giác lồi hay tứ giác lõm. 
#Vẽ tứ giác đó với màu bất kỳ nhập từ bàn ph
# Kiểm tra các góc của tứ giác đó phải đều nhỏ hơn 180 độ

xa=int(input('Nhập hoành độ của điểm A: '))
ya=int(input('Nhập tung độ của điểm A: '))
xb=int(input('Nhập hoành độ của điểm B: '))
yb=int(input('Nhập tung độ của điểm B: '))
xc=int(input('Nhập hoành độ của điểm C: '))
yc=int(input('Nhập tung độ của điểm C: '))
xd=int(input('Nhập hoành độ của điểm D: '))
yd=int(input('Nhập tung độ của điểm D: '))

import math

AB=math.sqrt((xb-xa)**2+(yb-ya)**2)
AD=math.sqrt((xd-xa)**2+(yd-ya)**2)
DC=math.sqrt((xc-xd)**2+(yc-yd)**2)
BC=math.sqrt((xc-xb)**2+(yc-yb)**2)
AC=math.sqrt((xc-xa)**2+(yc-ya)**2)
BD=math.sqrt((xd-xb)**2+(yd-yb)**2)

cosA=(AB**2+AD**2-BD**2)/(2*AB*AD)
cosB=(AB**2+BC**2-AC**2)/(2*BC*AB)
cosC=(BC**2+DC**2-BD**2)/(2*BC*DC)
cosD=(AD**2+DC**2-AC**2)/(2*AD*DC)

tugiacloi=(cosA<1 and cosA>-1) and (cosB<1 and cosB>-1) and (cosC<1 and cosC>-1) and (cosD<1 and cosD>-1)
print('tứ giác lồi: ',tugiacloi)
# Vẽ tứ giác 
import turtle
t=turtle.Turtle()
t.shape('turtle')
t.hideturtle()
t.fillcolor('red')
t.begin_fill()
t.goto(xa,ya)
t.goto(xd,yd)
t.goto(xb,yb)
t.goto(xc,yc)
t.goto(xa,ya)
t.end_fill()
turtle.done()


# In[ ]:





# In[ ]:





# In[ ]:




