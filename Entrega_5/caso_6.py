from matplotlib.pylab import *
from matplotlib import cm


#Geometría
a = 1. #Alto
b = 1. #Ancho
Nx = 30 #Intervalos en X
Ny = 30 #Intervalos en Y

dx = b / Nx #Discretizacion en X
dy = a / Ny #Discretizacion en Y


if dx != dy:
    print("Error: dx y dy no son iguales")
    exit(-1)   

h = dx

#Coordenadas del punto (i,j)
def coords(i, j): return (dx * i, dy * j)


x, y = coords(4, 2)

print("x: ",x)
print("y: ",y)


def imshowbien(u):
    imshow(u.T[Nx::-1, :], cmap=cm.coolwarm, interpolation = "bilinear")
    cbar = colorbar(extend="both", cmap=cm.coolwarm)
    ticks = arange(0, 35, 5)
    ticks_Text = ["{}".format(deg) for deg in ticks]
    cbar.set_ticks(ticks)
    cbar.set_ticklabels(ticks_Text)
    clim(0, 30)
    
    xlabel("b")
    ylabel("a")
    xTicks_N = arange(0, Nx + 1, 3)
    yTicks_N = arange(0, Ny + 1, 3)
    xTicks = [coords(i, 0)[0] for i in xTicks_N]
    yTicks = [coords(0, i)[1] for i in yTicks_N]
    xTicks_Text = ["{0:.2f}".format(tick) for tick in xTicks]
    yTicks_Text = ["{0:.2f}".format(tick) for tick in yTicks]
    xticks(xTicks_N, xTicks_Text, rotation="vertical")
    yticks(yTicks_N, yTicks_Text)
    margins(0.2)
    subplots_adjust(bottom = 0.15)
    

u_k = zeros((Nx + 1, Ny + 1), dtype=double)
u_km1 = zeros((Nx + 1, Ny + 1), dtype=double)

#Condicion de Borde Inicial
u_k[:, :] = 30. #Son 30 grados en todas partes

#Parámetros para el hierro
dt = 0.01 #s
K = 79.5 #m^2/s
c = 450. #J/Kg*C
rho = 7800. #Kg/m^3
alpha = K * dt / (c * rho * dx**2)

#Informacion interesante
print(f"dt = {dt}")
print(f"dx = {dx}")
print(f"K = {K}")
print(f"c = {c}")
print(f"rho = {rho}")
print(f"alpha = {alpha}")

#Loop en el tiempo
minuto = 60.
hora = 3600.
dia = 24 * 3600.

dt = 1 * minuto
dnext_t = 0.5 * hora

next_t = 0
framenum = 0

T = 1 * dia
Days = 1 * T #Cantidad de Dias a Simular

#Vectores con temperatura acumulada
u_0 = zeros(int32(Days / dt))
u_N4 = zeros(int32(Days / dt))
u_2N4 = zeros(int32(Days / dt))
u_3N4 = zeros(int32(Days / dt))

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n* multiplier) / multiplier


for k in range(int32(Days/dt)):
    t = dt * (k + 1)
    dias = truncate(t / dia, 0)
    horas = truncate((t - dias *dia) / hora, 0)
    minutos = truncate((t - dias * dia -horas * hora) / minuto, 0)
    titulo = "k = {0:05.0f}".format(k) + " t = {0:02.0f}d {1:02.0f}h {2:02.0f}m ".format(dias, horas, minutos)
    print(titulo)
    
    
#Condiciones de Borde Eseciales    
    u_k[0, :] = 10. #Borde Izquierdo
    u_k[:, 0] =  u_k[:, -1] - 0. * dy #Borde Inferior, con gradiente 0
    u_k[:, -1] = u_k[:, -2] - 0 * dy #Borde Superior, con gradiente 0
    u_k[-1, :] = u_k[-2, :] - 0. * dx  #Borde Derecho, con gradiente 0
    


    # Loop en el espacio desde i = 1, hasta i = n-1
    for i in range(1,Nx):
        for j in range(1,Ny):
            
            #Algortimo de diferencias finitas en 2-D para difusion
            
            #Laplaciano
            nabla_u_k = (u_k[i-1, j] + u_k[i+1, j] + u_k[i, j-1] + u_k[i, j+1] - 4 * u_k[i,j]) / h**2
            
            #Forard Euler
            u_km1[i,j] = u_k[i,j] + alpha * nabla_u_k
            
    #Avanzar la solucion a k + 1
    u_k = u_km1
    
    #Reetablecen condiciones de Borde para asegurar cumplimiento
    u_k[0, :] = 10. #Borde Izquierdo
    u_k[:, 0] =  u_k[:, -1] - 0. * dy #Borde Inferior, con gradiente 0
    u_k[:, -1] = u_k[:, -2] - 0 * dy #Borde Superior, con gradiente 0
    u_k[-1, :] = u_k[-2, :] - 0 * dx  #Borde Derecho, con gradiente 0
    
    u_0[k] = u_k[int(Nx / 2), -1]
    u_N4[k] = u_k[int(Nx / 2), int(Ny / 4)]
    u_2N4[k] = u_k[int(Nx / 2), int(2 * Ny / 4)]
    u_3N4[k] = u_k[int(Nx / 2), int(3 * Ny / 4)]
    
    #Graicando en d_next
    if t > next_t:
        figure(1)
        imshowbien(u_k)
        title(titulo)
        savefig("Caso6/frame_{0:04.0f}.png".format(framenum))
        framenum += 1
        next_t += dnext_t
        close(1)
        
        
#Ploteo puntos interesantes
figure(2)
plot(range(int32(Days / dt)), u_0, label='Superficie')
plot(range(int32(Days / dt)), u_N4, label='N/4')
plot(range(int32(Days / dt)), u_2N4, label='N/2')
plot(range(int32(Days / dt)), u_3N4, label='3N/4')
title("Evolución de temperatura")
legend()
savefig("Caso_6.png", dpi=320)
show()