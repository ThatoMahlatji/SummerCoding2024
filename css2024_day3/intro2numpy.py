# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:07:42 2024

@author: tjmah
"""


import numpy as np
import matplotlib.pyplot as plt

# Conventional python - for loop
for i in range(1,11):
    print("i = ", i)
print("-------end--------")
    
# numpy - arange (can handle float increment )
for j in np.arange(1,6,.5):
    print ("j = ", j)

print("-------end--------")

# squaring - conventional
squares = []
for i in range(1,6):
    squares.append(i**2)
print("squares = ", squares)

print("-------end--------")

# using numpy
squaresNp = np.arange(1,6)**2
print("squaresNp = ", squaresNp)

print("-------end--------")

# option 2
x = np.arange(1,6)
y = x**2

#plt.plot(x,y,"*r")
#plt.show()

print("x shape = ", x.shape)
print("y shape = ", y.shape)
print("x + y = ", x+y)
print("x * y = ", x*y)
print("dot product = ", x.dot(y))
print("cross product = ", np.multiply(x,y))


alist = [1,2,5,6,15,22]
data = np.array(alist)
print("data = ", data)
data2 = data.reshape([2,3])
data3 = np.reshape(data, [2,3])
print("data2 =", data2)
print("data3 = ", data3)
print("data2 + data3 = ", data2 + data3)


data4 = np.matmul(data2.T,data3)
data5 = np.multiply(data2,data3)
print("data4 = ", data4)
print("data5 = ", data5)

print("Cross product")
print("data2[0,:] = ", data2[0,:].T)
print("data3[0,:]",data3[0,:])
cross_data = np.cross(data2[0,:].T,data3[0,:])
print("cross data = ", cross_data)
cross_data2 = np.cross(data2[0,:].T,data3[1,:])
print("cross data_row2 = ", cross_data2)


# Matrices
# Solve a system of linear equations
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,-9]])
b = np.array([3,-4,2])
d = np.linalg.det(a)
if (d>0):
    print(f"d = {d}, so this matric is solvable")
# solve for x,y,z
sol = np.linalg.solve(a,b)
    

# Load csv file
import numpy as np

data = np.loadtxt("css2024_day3/noisydata.csv", skiprows=1,delimiter=",")
data_avg = np.mean(data,0)
print("average of columns =  ", data_avg)


print(data)
pressure = data[:,0]
flowrate = data[:,1]

# coefficient of a polynomial
fit = np.polyfit(pressure,flowrate,2) #2 = order
# a, b ,c
print(fit)

flowfit = np.polyval(fit,pressure)

plt.plot(pressure, flowrate, "go")
plt.plot(pressure, flowfit, "k-")
plt.xlabel("Pressure (Pa)")
plt.ylabel("Flowrate ($m^3/s$)")
plt.legend(["Original","Fit"])
plt.title("Flow rate and pressure data")
plt.show()

# trick
print(pressure[pressure<4])


# Moter carlo
n = 3000
x = np.random.uniform(size=n)
y = np.random.uniform(size=n)
print(sum(x*x+y*y<=1)/n*4)
plt.plot(x[x*x+y*y*1<=1],y[x*x+y*y<=1],"bo")
plt.plot(x[x*x+y*y*1>1],y[x*x+y*y>1],"ro")
plt.savefig("pi.png")
plt.show()






