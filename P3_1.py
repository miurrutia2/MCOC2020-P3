from matplotlib.pylab import *

L = 1.
n = 100
dx = L / n

x = linspace(0, L, n+1)


dt = 2.
Nt = 50000
u = zeros((Nt, n+1))

u[:,0] = 0.		#Borde Izquierdo
u[:,-1] = 0.	#Borde Derecho

#Condicion Inicial
u[0, :] = 20

K = 79.5
c = 450
rho = 7800


u = zeros((Nt, n+1))

#u[:,0] = 0.		#Borde Izquierdo
u[:,-1] = 20.	#Borde Derecho

#Condicion Inicial
u[0, :] = 20

alpha = K*dt/(c*rho*dx**2)
for k in range(Nt-1):
	t = dt*k
	#print (f"k = {k} t = {t}")
	u[k, 0] = -5 * dx + u[k, 1]
	for i in range(1,n):
		u[k+1, i] = u[k,i] + alpha*(u[k, i+1] - 2*u[k, i] + u[k, i-1])
	#print (x, u[k, :])

	if k % 200 == 0:
		plot(x, u[k, :])

title("k = {}  t = {} s".format(k, k*dt))

show()