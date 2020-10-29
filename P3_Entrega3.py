from matplotlib.pylab import *

L = 1
n = 19
dx = L / n

x = linspace(0, L, n+1)


dt = 2.
Nt = 90000
u = zeros((Nt, n+1))

u[:,0] = 0.		#Borde Izquierdo
u[:,-1] = 0.	#Borde Derecho

#Condicion Inicial
u[0, :] = 20

K = 79.5
c = 450
rho = 7800
alpha = K*dt/(c*rho*dx**2)

eje_x=[] 
eje_y=[]

for k in range(Nt-1):
	t = dt*k
	print (f"k = {k} t = {t}")
	u[k, n] = 10 * dx + u[k, n-1]
	for i in range(1,n):
		u[k+1, i] = u[k,i] + alpha*(u[k, i+1] - 2*u[k, i] + u[k, i-1])
	print (x, u[k, :])

	eje_x.append(t/(dt*3600))
	eje_y.append(u[k, 2])

	if k % 500 == 0: 
		plot(eje_x, eje_y)


title("x = {}".format(x[2]))

show()
