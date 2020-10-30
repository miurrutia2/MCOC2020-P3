from matplotlib.pylab import *

L = 1.0
n = 100  #discretizacion de 100 int
dx = L / n

x = linspace(0, L, n+1)

# arreglo con la solucion
dt = 2.
Nt = 50000

u = zeros((Nt, n+1))

# 25	35	10
#condiciones de borde
u[:,-1] = 20. #Borde der

#Condicion inicial
u[0, 1:n] = 20


K = 79.5  # m^2 /s
c = 450.  # J /kg C
ρ = 7800. # kg / m^3 
α = K*dt/(c*ρ*dx**2)

for k in range(Nt-1):
	t = dt*k
	print(f"k = {k} t = {t}")
	u[k,0] = -5*dx+u[k,1]
	for i in range(1, n):
		u[k+1, i] = u[k,i] + α*(u[k,i+1] - 2*u[k,i] + u[k,i-1])

	if k % 1000 == 0:
		plot(x,u[k,:])

title("k = {} t={} s".format(k,k*dt))

show()

