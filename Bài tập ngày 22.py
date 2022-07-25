#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Yêu cầu: Nhập vào toạ độ của 3 điểm A, B, C. Xác định 3 điểm A, B, C có phải là 3 điểm của tam giác hay không? ##Vẽ tam giác
# Tính độ dài của các đường cao từ các đỉnh, tính độ dài của các trung tuyến từ các đỉnh, xác định toạ độ của trọng tâm
#và trực tâm của ABC. Visualize các kết quả lên turtle!

xa=int(input('Nhập hoành độ điểm A: '))
ya=int(input('Nhập tung độ điểm A: '))
xb=int(input('Nhập hoành độ điểm B: '))
yb=int(input('Nhập tung độ điểm B: '))
xc=int(input('Nhập hoành độ điểm C: '))
yc=int(input('Nhập tung độ điểm C: '))
import math
AB=math.sqrt((xa-xb)**2+(ya-yb)**2)
AC=math.sqrt((xa-xc)**2+(ya-yc)**2)
BC=math.sqrt((xb-xc)**2+(yb-yc)**2)
cosA=(AC**2+AB**2-BC**2)/(2*AC*AB)
cosB=(BC**2+AB**2-AC**2)/(2*BC*AB)
cosC=(BC**2+AC**2-AB**2)/(2*BC*AC)
A = math.degrees(math.acos(cosA))
B = math.degrees(math.acos(cosB))
C = math.degrees(math.acos(cosC))


tamgiac=(AB+AC)>BC and (AB+BC)>AC and (AC+BC)>AB
print('tam giác:',tamgiac)

#Tính độ dài các đường cao từ đỉnh của tam giác
duongcaoCH=CH=math.sin(B)*BC
duongcaoAK=AK=math.sin(C)*AC
duongcaoBS=BS=math.sin(A)*AB
print(CH)
print(AK)
print(BS)

# Tính độ dài đường trung tuyến từ các đỉnh 
duongtrungtuyenAI=AI=math.sqrt(2*(AB**2+AC**2)-BC**2)/2
duongtrungtuyenCJ=CJ=math.sqrt(2*(BC**2+AC**2)-AB**2)/2
duongtrungtuyenBO=BO=math.sqrt(2*(BC**2+AB**2)-AC**2)/2
print(AI)
print(CJ)
print(BO)


# Xác định tọa độ trọng tâm của tam giác 
xg=(xa+xb+xc)/3
yg=(ya+yb+yc)/3
print('G',xg,yg)
# Xác định tọa độ trực tâm của tam giác 
#Gọi M là trực tâm của tam giác ABC
xm=int(input('Nhập hoành độ điểm M: '))
ym=int(input('Nhập tung độ điểm M: '))
2*xm+ym==400
xm+2*ym==400
print(xm,ym)

    
# Vẽ
import turtle
t=turtle.Turtle()
t.shape('turtle')
t.goto(xa,ya)
t.goto(xb,yb)
t.goto(xc,yc)
t.goto(xa,ya)
turtle.done()



# In[ ]:





# In[ ]:





# In[ ]:




