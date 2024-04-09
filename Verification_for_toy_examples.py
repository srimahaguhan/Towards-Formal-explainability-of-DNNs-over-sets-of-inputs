from z3 import *

# Defining the inputs and weights 

x1, x2, x3 = Reals('x1 x2 x3')
b1, b2, b3 = Reals('b1 b2 b3')
h1, h2, h3 = Reals('h1 h2 h3')
w11, w12, w13, w21, w22, w23, w31, w32, w33 = Reals('w11 w12 w13 w21 w22 w23 w31 w32 w33') 
w1, w2, w3 = Reals('w1 w2 w3')
w4, w5, w6 = Reals('w4 w5 w6')
output1, output2 = Reals('output1 output2')



def Relu(x):
    return If(x>0, x, 0)

# defining the hidden layer 


# defining the output layer 

#


constraints = [
    Or(x1==0,x1==1) ,Or(x2==0,x2==1), Or(x3==0,x3==1),
    w11 == 2, w12 == 3, w13 == 5, 
    w21 == 2, w22 == 3, w23 == 7,
    w31 == 2, w32 == 3, w33 == 6,
    w1 == 1, w2 == 1, w3 == 0,
    w4 == -1, w5 == -1, w6 == 1,
    b1 == -4 , b2 == -3 , b3 == 0,
]

s=Solver()
s.add(constraints)
s.add(h1 == Relu(w11 * x1 + w12 * x2 + w13 * x3 + b1 ))
s.add(h2 == Relu(w21 * x1 + w22 * x2 + w23 * x3 + b2))
s.add(h3 == Relu(w31 * x1 + w32 * x2 + w33 * x3 + b3))
s.add(output1 == (w1 * h1 + w2 * h2 + w3 * h3))
s.add(output2 == (w4 * h1 + w5 * h2 + w6 * h3))

s.add(output1==15)

print(s)
print(s.check())
print(s.model())





