from matplotlib.pylab import *

L = 1.04
n = 20
dx = L / n

x = linspace(0, L, n+1)


dt = 1.
Nt = 5000
u = zeros((Nt, n+1))

u[:,0] = 0.		#Borde Izquierdo
u[:,-1] = 0.	#Borde Derecho

#Condicion Inicial
u[0, :] = 20

K = 79.5
c = 450
rho = 7800


dts = [1,5,10,50]
for dt in dts:
	eje_x=[] 
	eje_y=[]
	Nt = 9000
	Nt = Nt//dt

	u = zeros((Nt, n+1))

	u[:,0] = 0.		#Borde Izquierdo
	u[:,-1] = 0.	#Borde Derecho

	#Condicion Inicial
	u[0, :] = 20

	alpha = K*dt/(c*rho*dx**2)
	for k in range(Nt-1):
		t = dt*k
		#print (f"k = {k} t = {t}")
		#u[k, n] = 10 * dx + u[k, n-1]
		for i in range(1,n):
			u[k+1, i] = u[k,i] + alpha*(u[k, i+1] - 2*u[k, i] + u[k, i-1])
		#print (x, u[k, :])

		eje_x.append(t*10/3600)
		eje_y.append(u[k, 2])

	subplot(3,1,1)
	plot(eje_x, eje_y, label=f"{dt}")
	grid(True)
	legend()

title("x = {}".format(x[2]))

for dt in dts:
	eje_x=[] 
	eje_y=[]
	Nt = 9000
	Nt = Nt//dt

	u = zeros((Nt, n+1))

	u[:,0] = 0.		#Borde Izquierdo
	u[:,-1] = 0.	#Borde Derecho

	#Condicion Inicial
	u[0, :] = 20

	alpha = K*dt/(c*rho*dx**2)
	for k in range(Nt-1):
		t = dt*k
		#print (f"k = {k} t = {t}")
		#u[k, n] = 10 * dx + u[k, n-1]
		for i in range(1,n):
			u[k+1, i] = u[k,i] + alpha*(u[k, i+1] - 2*u[k, i] + u[k, i-1])
		#print (x, u[k, :])

		eje_x.append(t*10/3600)
		eje_y.append(u[k, 4])

	subplot(3,1,2)
	plot(eje_x, eje_y, label=f"{dt}")
	grid(True)
	legend()
title("x = {}".format(x[4]))
for dt in dts:
	eje_x=[] 
	eje_y=[]
	Nt = 9000
	Nt = Nt//dt

	u = zeros((Nt, n+1))

	u[:,0] = 0.		#Borde Izquierdo
	u[:,-1] = 0.	#Borde Derecho

	#Condicion Inicial
	u[0, :] = 20

	alpha = K*dt/(c*rho*dx**2)
	for k in range(Nt-1):
		t = dt*k
		#print (f"k = {k} t = {t}")
		#u[k, n] = 10 * dx + u[k, n-1]
		for i in range(1,n):
			u[k+1, i] = u[k,i] + alpha*(u[k, i+1] - 2*u[k, i] + u[k, i-1])
		#print (x, u[k, :])

		eje_x.append(t*10/3600)
		eje_y.append(u[k, 8])

	subplot(3,1,3)
	plot(eje_x, eje_y, label=f"{dt}")
	grid(True)
	legend()

title("x = {}".format(x[8]))

show()
