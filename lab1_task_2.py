'''
Постройте график функции
y(x) = x*x - x - 6
и по графику найдите найдите корни уравнения y(x) = 0. (Не нужно применять численных методов — просто приблизьте график
к корням функции настолько, чтобы было удобно их найти.)
'''
import numpy
import matplotlib.pyplot as plt


x = numpy.arange(-10, 10, 0.01)
plt.figure(figsize=(10, 5))
plt.plot(x, x*x-x-6, label=r'$f(x)=x*x-x-6$')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=14)
plt.show()

#Корни уравнения y(x) = 0 равны 0 и -3