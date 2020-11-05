# Casos replicados

## Caso 1
Las condiciones de borde para el primer caso fueron las siguientes:
  + 20º Inicial
  + Borde Superior: 0º
  + Borde Izquierdo: 20º
  + Borde Inferior: 20º
  + Borde Derecho: 0º

Esto se traduce en los siguientes términos del codigo :
  + u_k[:, :] = 20.   #Inicial
  + u_k[:, -1] = 0.   #Borde Superior
  + u_k[0, :] = 20.   #Borde Izquierdo
  + u_k[:, 0] = 20.   #Borde Inferior
  + u_k[-1, :] = 0.   #Borde Derecho
  
![](Entrega_5/Caso_1.png)

### Evolución de la temperatura en el tiempo en los puntos
![](Entrega_5/Caso_1_puntos.png)

### Distribución de temperatura en los tiempos
### 0h
![](Entrega_5/Caso1/frame_0000.png)
### 2h
![](Entrega_5/Caso1/frame_0004.png)
### 6h
![](Entrega_5/Caso1/frame_0012.png)
### 12h
![](Entrega_5/Caso1/frame_0024.png)
### 14h
![](Entrega_5/Caso1/frame_0028.png)
### Gif
![](Entrega_5/caso_1.gif)


## Caso 2
Las condiciones de borde para el segundo caso fueron las siguientes:
  + 20º Inicial
  + Borde Superior: 0º
  + Borde Izquierdo: 20º
  + Borde Inferior: 20º
  + Borde Derecho: Gradiente 0º

Esto se traduce en los siguientes términos del codigo :
  + u_k[:, :] = 20.                     #Inicial
  + u_k[:, -1] = 0.                     #Borde Superior
  + u_k[0, :] = 20.                     #Borde Izquierdo
  + u_k[:, 0] = 20.                     #Borde Inferior
  + u_k[-1, :] = u_k[-2, :] - 0. * dx   #Borde Derecho
  
![](Entrega_5/Caso_2.png)

### Evolución de la temperatura en el tiempo en los puntos
![](Entrega_5/Caso_2_puntos.png)

### Distribución de temperatura en los tiempos
### 0h
![](Entrega_5/Caso2/frame_0000.png)
### 2h
![](Entrega_5/Caso2/frame_0004.png)
### 6h
![](Entrega_5/Caso2/frame_0012.png)
### 12h
![](Entrega_5/Caso2/frame_0024.png)
### 14h
![](Entrega_5/Caso2/frame_0028.png)
### Gif
![](Entrega_5/caso_2.gif)


## Caso 3
Las condiciones de borde para el tercer caso fueron las siguientes:
  + 10º Inicial
  + Borde Superior: 0º
  + Borde Izquierdo: 20º
  + Borde Inferior: 20º
  + Borde Derecho: 20º

Esto se traduce en los siguientes términos del codigo :
  + u_k[:, :] = 10.   #Inicial
  + u_k[:, -1] = 0.   #Borde Superior
  + u_k[0, :] = 20.   #Borde Izquierdo
  + u_k[:, 0] = 20.   #Borde Inferior
  + u_k[-1, :] = 20.  #Borde Derecho

![](Entrega_5/Caso_3.png)

### Evolución de la temperatura en el tiempo en los puntos
![](Entrega_5/Caso_3_puntos.png)

### Distribución de temperatura en los tiempos
### 0h
![](Entrega_5/Caso3/frame_0000.png)
### 2h
![](Entrega_5/Caso3/frame_0004.png)
### 6h
![](Entrega_5/Caso3/frame_0012.png)
### 12h
![](Entrega_5/Caso3/frame_0024.png)
### 14h
![](Entrega_5/Caso3/frame_0028.png)
### Gif
![](Entrega_5/caso_3.gif)


## Caso 4
Las condiciones de borde para el cuarto caso fueron las siguientes:
  + 10º Inicial
  + Borde Superior: 0º
  + Borde Izquierdo: 20º
  + Borde Inferior: 20º
  + Borde Derecho: Gradiente 0º

Esto se traduce en los siguientes términos del codigo :
  + u_k[:, :] = 10.               #Inicial
  + u_k[:, -1] = 0.               #Borde Superior
  + u_k[0, :] = 20.               #Borde Izquierdo
  + u_k[:, 0] = 20.               #Borde Inferior
  + u_k[-1,:] = u_k[-2,:]- 0*dx   #Borde Derecho

![](Entrega_5/Caso_4.png)

### Evolución de la temperatura en el tiempo en los puntos 
![](Entrega_5/Caso_4_puntos.png)

### Distribución de temperatura en los tiempos
### 0h
![](Entrega_5/Caso4/frame_0000.png)
### 2h
![](Entrega_5/Caso4/frame_0004.png)
### 6h
![](Entrega_5/Caso4/frame_0012.png)
### 12h
![](Entrega_5/Caso4/frame_0024.png)
### 14h
![](Entrega_5/Caso4/frame_0028.png)
### Gif
![](Entrega_5/caso_4.gif)


## Caso 5
Las condiciones de borde para el quinto caso fueron las siguientes:
  + 5º Inicial
  + Borde Superior: Gradiente 0º
  + Borde Izquierdo: 25º
  + Borde Inferior: Gradiente 0º
  + Borde Derecho: 25º

Esto se traduce en los siguientes términos del codigo :
  + u_k[:, :] = 5.                    #Inicial
  + u_k[:, -1] = u_k[:, -2] -0 * dy   #Borde Superior
  + u_k[0, :] = 25.                   #Borde Izquierdo
  + u_k[:, 0] = u_k[:, -1] - 0. * dy  #Borde Inferior
  + u_k[-1,:] = 25                    #Borde Derecho

![](Entrega_5/Caso_5.png)

### Evolución de la temperatura en el tiempo en los puntos
![](Entrega_5/Caso_5_puntos.png)

### Distribución de temperatura en los tiempos
### 0h
![](Entrega_5/Caso5/frame_0000.png)
### 2h
![](Entrega_5/Caso5/frame_0004.png)
### 6h
![](Entrega_5/Caso5/frame_0012.png)
### 12h
![](Entrega_5/Caso5/frame_0024.png)
### 14h
![](Entrega_5/Caso5/frame_0028.png)
### Gif
![](Entrega_5/caso_5.gif)


## Caso 6
Las condiciones de borde para el sexto caso fueron las siguientes:
  + 30º Inicial
  + Borde Superior: Gradiente 0º
  + Borde Izquierdo: 10º
  + Borde Inferior: Gradiente 0º
  + Borde Derecho: Gradiente 0º

Esto se traduce en los siguientes términos del codigo :
  + u_k[:, :] = 30.                    #Inicial
  + u_k[:, -1] = u_k[:, -2] -0 * dy    #Borde Superior
  + u_k[0, :] = u_k[:, -1] - 0. * dy   #Borde Izquierdo
  + u_k[:, 0] = u_k[:, -1] - 0. * dy   #Borde Inferior
  + u_k[-1,:] = u_k[-2, :] - 0. * dx   #Borde Derecho
  
![](Entrega_5/Caso_6.png)

### Evolución de la temperatura en el tiempo en los puntos
![](Entrega_5/Caso_6_puntos.png)

### Distribución de temperatura en los tiempos
### 0h
![](Entrega_5/Caso6/frame_0000.png)
### 2h
![](Entrega_5/Caso6/frame_0004.png)
### 6h
![](Entrega_5/Caso6/frame_0012.png)
### 12h
![](Entrega_5/Caso6/frame_0024.png)
### 14h
![](Entrega_5/Caso6/frame_0028.png)
### Gif
![](Entrega_5/caso_6.gif)


## Caso 7
Las condiciones de borde para el séptimo caso fueron las siguientes:
  + 20º Inicial
  + Borde Superior: Temperatura ambiental (sinusoide con variación de 10º, periodo de 1 día)
  + Borde Izquierdo: Gradiente 0º
  + Borde Inferior: Gradiente 0º
  + Borde Derecho: Gradiente 0º

Esto se traduce en los siguientes términos del codigo :
  + u_k[:, :] = 20.                                       #Inicial
  + u_k[:, -1] = Tambiental = 20. + 10.*sin((2*pi/T)*t)   #Borde Superior
  + u_k[0, :] = u_k[-2, :] - 0 * dx                       #Borde Izquierdo
  + u_k[:, 0] = u_k[:, -1] - 0. * dy                      #Borde Inferior
  + u_k[-1,:] = u_k[-2, :] - 0. * dx                       #Borde Derecho
  
![](Entrega_5/Caso_7.png)

### Evolución de la temperatura en el tiempo en los puntos
![](Entrega_5/Caso_7_puntos.png)

### Distribución de temperatura en los tiempos
### 0h
![](Entrega_5/Caso7/frame_0000.png)
### 2h
![](Entrega_5/Caso7/frame_0004.png)
### 6h
![](Entrega_5/Caso7/frame_0012.png)
### 12h
![](Entrega_5/Caso7/frame_0024.png)
### 14h
![](Entrega_5/Caso7/frame_0028.png)
### Gif
![](Entrega_5/caso_7.gif)


