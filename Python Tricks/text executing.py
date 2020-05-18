from numpy import *
from matplotlib.pyplot import *
import time

code = "print('hello there how are you')"

code_with_math = '''
print('hello there! it is from a text file')
a = 12
b = 19
print('the sum of a and b is :{}'.format(a+b))
print('now lets draw some plots')
print('wait a moment...')
time.sleep(1)
print('are you still waiting?')
time.sleep(1)
print('your result in ready')
time.sleep(0.2)
x = arange(0,12,0.1)
y = sin(x)
plot(x,y)
show()
'''

exec(code_with_math)

#eval(code_with_math)

#print(code_with_math)
