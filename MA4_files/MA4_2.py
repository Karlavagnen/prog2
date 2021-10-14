#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc
from time import sleep as pause
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
	f = Integer(5)
	print(f.get())
	print(f.fib())
	f.set(7)
	print(f.get())
	print(f.fib())
	print(fib_py(5))

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1)+fib_py(n-2))

if __name__ == '__main__':

	n=np.arange(35,40)
	tid_cpp=[]
	tid_py=[]
	for i in range(35,40):
		start = pc()
		fib_py(i)
		end = pc()
		tid_py.append(round(end-start,2))
	for i in range(35,40):
		f=Integer(i)
		start_cpp=pc()
		f.fib()
		end_cpp=pc()
		tid_cpp.append(round(end_cpp-start_cpp,2))
	print(tid_cpp)
	print()
	print(tid_py)
	plt.plot(n,tid_py,'bo')
	plt.plot(n,tid_cpp,'ro')
	plt.legend(['Py','Cpp'])
	plt.title('Plottning av Fibonnaci med Python och C++')
	plt.savefig('MA4_testplot.png')
	main()
