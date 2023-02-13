import math
import numpy as np
'''
x_values =[1,2,3,4,5]
y_values = [10,11,12,13,14]
x_bar = sum(x_values)/len(x_values)
y_bar = sum(y_values)/len(y_values)

print(x_bar,y_bar)
summation = 0
for i in range(len(x_values)):
    summation += abs((x_bar - x_values[i])*(y_bar - y_values[i]))

result = math.sqrt(summation/(len(x_values)-1))
print(result)
'''
import matplotlib.pyplot as plt

def sigmoid(z):
    return (1/(1+math.exp(-z)))

def activation(k):
    k1 = sigmoid(k)
    if k1>0.5:
        return 1
    else:
        return 0

def rev_sigmoid(val):
    if val==0:
        raise ZeroDivisionError
    else:
        return (math.log(val) - math.log(1-val))



'''
values = [0.9725,0.8324,0.1139,0.6739,0.9831,0.9135,0.1314,0.0098]
new_values = []
for value in values:
    print("input:",value, "output:",'{0:.{1}f}'.format(sigmoid(value), 4))
    new_values+=[sigmoid(value)]
for value in new_values:
    print("input:",'{0:.{1}f}'.format(value, 4), "output:",'{0:.{1}f}'.format(rev_sigmoid(value), 4))

w=[0.2,0.1,-0.3]
x=[0.3,0.5,0.6]
b=[0.48]
print(sigmoid(neuron(x,w,b )))
while sigmoid(neuron(x,w,b ))>0.5:
    for i in range(len(w)):
        w[i]-=0.01
print(w, sigmoid(neuron(x,w,b )))
'''    

def neuron(x,w,b):
    val = 0
    for i in range(len(w)):
        val+=w[i]*x[i]
    return val+ b[0]


def f_z(k):
    if k>=0:
        return 1
    else:
        return -1

alpha = 0.5
t = -1

w1 = [0.05, 0.1]
w2 = [0.2, 0.2]
b1 = [0.3]
b2 = [0.15]
wy =[0.5,0.5]
wb = [0.5]
x = [1,0]

print(f_z(neuron([f_z(neuron(x,w1,b1)),f_z(neuron(x,w2,b2))],wy,wb)))

while f_z(neuron([f_z(neuron(x,w1,b1)),f_z(neuron(x,w2,b2))],wy,wb))>-1:
    for i in range(len(w1)):
        w1[i] = w1[i]+(alpha*(t-neuron(x,w1,b1))*x[i])
    for i in range(len(w2)):
        w2[i] = w2[i]+(alpha*(t-neuron(x,w2,b2))*x[i])
    for i in range(len(wy)):
        wy[i] = wy[i]+(alpha*(t-neuron([f_z(neuron(x,w1,b1)),f_z(neuron(x,w2,b2))],wy,wb))*x[i])
    b1[0] = b1[0] +(alpha*(t-neuron(x,w1,b1)))
    b2[0] = b2[0] +(alpha*(t-neuron(x,w2,b2)))
    wb[0] = wb[0] +(alpha*(t-neuron([f_z(neuron(x,w1,b1)),f_z(neuron(x,w2,b2))],wy,wb)))
    print("w1:",w1," w2:",w2," wy:",wy," b1:",b1," b2:",b2," by:",wb)

print(f_z(neuron([f_z(neuron(x,w1,b1)),f_z(neuron(x,w2,b2))],wy,wb)))