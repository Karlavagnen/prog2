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
	f.set(47)
	start=pc()
#	print(f.get())
	print(f.fib())
#	print(fib_py(5))
	end=pc()
	#print(f'Tiden det tog att räkna ut fibonnaci 47 var {round(end-start,2)} sekunder')
#Det tog 51.72 sekunder att beräkna fibonnaci 47!
#Viktigt att veta är att fibonacci 47 är större än det största tillåtna talet
#Detta betyder att vi inte kommer att få fram rätt tal då det överskrider minnet (overflow errro)
def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1)+fib_py(n-2))

if __name__ == '__main__':

#	n=np.arange(30,45)#Skapar en lista från 30 till 45
#	tid_cpp=[] #Skapar en tom lista med tiden för cpp
#	tid_py=[] #Skapar en tom lista med tiden för python
#	for i in range(30,45):#En for loop som går från 30 till 45
#		start = pc() #Startar tidtagning
#		fib_py(i) #Python fibonnaci
#		end = pc() #Stoppar tidtagning
#		tid_py.append(round(end-start,2)) #Stoppar in tiden det tog i listan för python 
#		f=Integer(i)
#		start_cpp=pc()# Startar tidtagning för cpp
#		f.fib() # Beräknar fib för cpp
#		end_cpp=pc() #Stoppar tidtagning
#		tid_cpp.append(round(end_cpp-start_cpp,2))#stoppar in tiden det tog i listan för cpp
#	print(tid_cpp)
#	print()
#	print(tid_py)
#	Plottning av tiden det tog!
#	plt.plot(n,tid_py,'bo')
#	plt.plot(n,tid_cpp,'ro')
#	plt.legend(['Py','Cpp'])
#	plt.title('Plottning av Fibonnaci med Python och C++')
#	plt.savefig('MA4_Py_Cpp_plot.png')
	main()
