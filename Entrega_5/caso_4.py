from matplotlib.pylab import *
from matplotlib import cm
import numpy as np

#Geometria
a = 1.         
b = 0.5         
Nx = 15     
Ny = 30     

dx = b/Nx
dy = a/Ny

h = dx

if dx != dy:
    print("ERROR! dy != dy")
    exit(-1)      


def coords(i,j):
    return(dx*i,dy*j)
x,y = coords(4,2)

print(f"x = {x}")
print(f"y = {y}")

def imshowbien(u):
    imshow(u.T[Ny::-1,:],cmap=cm.coolwarm,interpolation='bilinear')
    cbar = colorbar(extend = 'both', cmap= cm.coolwarm)
    ticks = np.arange(0,35,5)
    ticks_Text = ["{}°".format(deg) for deg in ticks]
    cbar.set_ticks(ticks)
    cbar.set_ticklabels(ticks_Text)
    clim(0,30)
    
    xlabel('b')
    ylabel('a')
    xTicks_N= np.arange(0,Nx+1,3)
    yTicks_N= np.arange(0,Ny+1,3)
    xTicks= [coords(i,0)[0] for i in xTicks_N]
    yTicks= [coords(0,i)[1] for i in yTicks_N]
    xTicks_Text = ["{0:.2f}".format(tick) for tick in xTicks]
    yTicks_Text = ["{0:.2f}".format(tick) for tick in yTicks]
    xticks(xTicks_N,xTicks_Text, rotation='vertical')
    yticks(yTicks_N,yTicks_Text)
    margins(0.2)
    subplots_adjust(bottom=0.15)
    
u_k = np.zeros((Nx+1, Ny+1), dtype = np.double) 
u_km1 = np.zeros((Nx+1, Ny+1),dtype = np.double) 

#condicion de borde inicial
u_k[:,:] = 10              

#parametros problema Hierro
dt = 0.01 #s
K = 79.5 #m^2/s
c = 450. #J/Kg*C
rho = 7800. #Kg/m^3                  
α = K*dt/(c*rho*dx**2)

#informar cosas interesantes
print(f"dt = {dt}")
print(f"K = {K}")
print(f"c = {c}")
print(f"rho = {rho}")
print(f"α = {α}")

#loop en el tiempo
minuto = 60. #[s]
hora = 3600. #[s]
dia = 24 * hora

dt = 1 * minuto
dnext_t = 0.5 * hora      #guardar imagen cada 30 min

next_t = 0
framenum = 0


T = 1*dia
Days= 1 *T                # Cantidad de Dias a Simular

# Vectores con temperatura acumulada
u_0 = np.zeros(np.int32(Days/dt))
u_N4 = np.zeros(np.int32(Days/dt))
u_2N4 = np.zeros(np.int32(Days/dt))
u_3N4 = np.zeros(np.int32(Days/dt))
P1 = np.zeros(np.int32(Days/dt))
P2 = np.zeros(np.int32(Days/dt))
P3 = np.zeros(np.int32(Days/dt))

def truncate(n,decimales=0):
    multiplier= 10**decimales
    return int(n*multiplier)/multiplier


for k in range(np.int32(Days/dt)):
    t = dt*(k+1)
    dias = truncate(t/dia, 0)
    horas = truncate((t-dias*dia)/hora, 0)
    minutos = truncate((t-dias*dia-horas*hora)/minuto, 0)
    titulo = "k = {0:05.0f} ".format(
        k) + " t = {0:02.0f}d {1:02.0f}h {2:02.0f}m".format(dias, horas, minutos)



    print(titulo)
    
    #CB esenciales, se repite en cada iteracion
    u_k[0 , :] = 20.            #Borde izquierdo
    u_k[: , 0] = 20.            #borde inferior
    u_k[: ,-1] = 0.             

    u_k[-1,:] = u_k[-2,:]-0*dx         #Borde Derecho, con gradiente 0             
    
    # Loop en el espacio desde i = 1, hasta i = n-1
    for i in range(1,Nx):
        for j in range(1,Ny):
            #Algortimo de diferencias finitas en 2-D para difusion
            
            #Laplaciano
            nabla_u_k = (u_k[i-1, j]+u_k[i+1,j]+u_k[i,j-1]+u_k[i,j+1]-4*u_k[i,j])/h**2
            
            #Forard Euler
            u_km1[i,j] = u_k[i,j]+α*nabla_u_k
            
    #Avanzar la solucion a k + 1
    u_k = u_km1
    
    u_k[0 , :] = 20.            #Borde izquierdo
    u_k[: , 0] = 20.            #borde inferior
    u_k[: ,-1] = 0.            

    u_k[-1,:] = u_k[-2,:]- 0*dx            
    
    
   
    u_0[k] = u_k[int(Nx/2),-1]                    
    u_N4[k] = u_k[int(Nx/2),int(Ny/4)]           
    u_2N4[k] = u_k[int(Nx/2),int(2*Ny/4)]         
    u_3N4[k] = u_k[int(Nx/2),int(3*Ny/4)]         


    P1[k] = u_k[int(Nx / 2), int(Ny / 4)]
    P2[k] = u_k[int(Nx / 2), int(3* Ny / 4)]
    P3[k] = u_k[int(3*Nx / 4), int(3 * Ny / 4)]

    
    #Graicando en d_next
    if t >= next_t:
        figure(1)
        imshowbien(u_k)
        title(titulo)
        savefig("Caso4/frame_{0:04.0f}.png".format(framenum))
        framenum += 1
        next_t += dnext_t
        close(1)
        
        
#Ploteo puntos interesantes
figure(2)
plot(range(int32(Days / dt)), u_0, label='Superficie')
plot(range(int32(Days / dt)), u_N4, label='N/4')
plot(range(int32(Days / dt)), u_2N4, label='2N/4')
plot(range(int32(Days / dt)), u_3N4, label='3N/4')
title("Evolución de temperatura")
legend()
savefig("Caso_4.png", dpi=320)
show()

figure(3)
plot(range(int32(Days / dt)), u_0, label='Superficie')
plot(range(int32(Days / dt)), P1, label='P1')
plot(range(int32(Days / dt)), P2, label='P2')
plot(range(int32(Days / dt)), P3, label='P3')
title("Evolución de temperatura")
legend()
savefig("Caso_4_puntos.png", dpi=320)
show()