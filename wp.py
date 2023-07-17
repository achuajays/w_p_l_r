import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,2,3,4,5])
y = np.array([5,6,7,8,9])
print(x)
print(y)
print(x.shape)
plt.scatter(x,y,marker='x', c='b')
plt.title('wieght')
plt.xlabel('age')
plt.ylabel('wieght')
w = 1 
b = 4
def c(x,w,b):
    m = x.shape[0]
    f = np.zeros(m)
    for i in range(m):
        f[i] = w* x[i]+ b
    
    return f
t = c(x,w,b)
plt.plot(x,t,label="my predication on wieghht", c='g')
plt.scatter(x,y,marker='x', c='b')
plt.title('wieght')
plt.xlabel('age')
plt.ylabel('wieght')
plt.show()
x= 4
value =   w * x + b
print(value)