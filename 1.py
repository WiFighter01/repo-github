import numpy as пр
import matplotlib.pyplot as plt


x = пр.arange(-10, 10, 0.01)
plt.figure(figsize=(10, 5))
plt.plot(x, пр.sin(x), label=r'$f_1(x)=\sin(x)$')
plt.plot(x, пр.cos(x), label=r'$f_2(x)=\cos(x)$')
plt.plot(x, -x, label=r'$f_3(x)=-x$')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel('$f(x)$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('figure_with_legend.png')
plt.show()