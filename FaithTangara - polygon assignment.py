import matplotlib.pyplot as plt

#create empty list for coordinate
x=[]
y=[]

#ask user how many point that he want
n=int(input("How many points do you want? "))
for i in range(n):
    inputx = int(input(f"enter x of point {i+1}: "))
    inputy = int(input(f"enter y of point {i+1}: "))
    x.append(inputx)
    y.append(inputy)

#print coordinates
for i in range(n):
    print(f"Point {i+1}: {x[i]},{y[i]}")

print(n)
print(x)
print(y)
#cross sectional area
A=0 
for i in range(len(x)):
    A+=1/2*(x[i]+x[i-1])*(y[i]-y[i-1])
print(f"the area is: {A}")

#static moments of cross section
Sx=0
Sy=0
for i in range(len(x)):
    Sx+=-1/6*(x[i]-x[i-1])*(y[i]**2+y[i]*y[i-1]+y[i-1]**2)
    Sy+=1/6*(y[i]-y[i-1])*(x[i]**2+x[i]*x[i-1]+x[i-1]**2)
print(f"Sx= {Sx}")
print(f"Sy= {Sy}")

#axial moments of inertia
Ix=0 
Iy=0
Ixy=0
for i in range(len(x)):
    Ix+=-1/12*(x[i]-x[i-1])*(y[i]**3+y[i]**2*y[i-1]+y[i]*y[i-1]**2+y[i-1]**3)
    Iy+=1/12*(y[i]-y[i-1])*(x[i]**3+x[i]**2*x[i-1]+x[i]*x[i-1]**2+x[i-1]**3)
    a=y[i]*(3*x[i]**2+2*x[i]*x[i-1]+x[i-1]**2)
    b=y[i-1]*(3*x[i-1]**2+2*x[i]*x[i-1]+x[i]**2)
    Ixy+=-1/24*(y[i]-y[i-1])*(a+b)
print(f"Ix= {Ix}")
print(f"Iy= {Iy}")
print(f"Ixy= {Ixy}")
#coordinate of centroid cross section
XT=Sy/A
YT=Sx/A
print(f"XT= {XT}")
print(f"YT= {YT}")
#moments of inertia
ITX=Ix-YT**2*A
ITY=Iy-XT**2*A
ITXY=Ixy+XT*YT*A
print(f"ITX= {ITX}")
print(f"ITY= {ITY}")
print(f"ITXY= {ITXY}")


print(f"A = {A:.2f}")
print(f"Sx = {Sx:.2f}")
print(f"Sy = {Sy:.2f}")
print(f"Ix = {Ix:.2f}")
print(f"Iy = {Iy:.2f}")
print(f"Ixy = {Ixy:.2f}")
print(f"XT = {XT:.2f}")
print(f"YT = {YT:.2f}")
print(f"ITX = {ITX:.2f}")
print(f"ITY = {ITY:.2f}")
print(f"ITXY = {ITXY:.2f}")