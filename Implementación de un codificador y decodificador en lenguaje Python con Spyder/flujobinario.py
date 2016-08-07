# -*- coding: utf-8 -*-
"""
Created on Thu Nov 06 23:27:19 2014

@author: Jorge Ulises Useche Cuellar
@código: 20091005082
@institución: Universidad Distrital Francisco José de Caldas
"""

#Generador de tren de pulsos
def flujobinario(tamano,p1):
    c=[]    
    for x in range(0, tamano):
        a = random()
        if(a <= p1):
            b=True
        else:
            b=False
        c.append(b)
    return c

#Convertir el arreglo de 1 y 0 a valores booleanos    
def tobool(arreglo):
    c=[]    
    for x in range(0, len(arreglo)):
        if(arreglo[x]==1):
            c.append(True)
        else:
            c.append(False)
    return c
 
#Convertir el arreglo de valores booleanos a 1 y 0
def tonum(arreglo):
    c=[]    
    for x in range(0, len(arreglo)):
        if(arreglo[x]==True):
            c.append(1)
        else:
            c.append(0)
    return c

#Genera un pulso de reloj en 0 y 1 alternados   
def reloj(tamano):
    tamano=int(tamano)
    c=[]
    p1=True;#porque el primer valor comienza en not True = False
    for x in range(0, tamano):
        p1 = not p1
        c.append(p1)
    return c

#Transforma los arreglos para graficar    
def tograph(arreglo):
    arreglo = arreglo[:]
    arreglo.insert(0,arreglo[0])
    arreglo.pop()
    return arreglo

#Trasforma un nivel lógico a una señal entre +V o +1 para True y -V o -1 para False
def tovoltage(arreglo):
    c=[]    
    for x in range(0, len(arreglo)):
        if(arreglo[x]==True):
            c.append(1)
        else:
            c.append(-1)
    return c
    
    

#ak1=flujobinario(100,0.5)
#ak1=tobool([1,0,0,1,1,0,0,1,0,1])
ak1=[False, True, True, True, True, True, True, False, True, False, True, False, False, True, True, True, False, False, True, True, True, False, False, False, False, True, False, True, False, True, False, False, True, True, True, True, False, False, False, True, False, False, False, False, False, False, True, False, True, False, True, False, False, True, True, False, False, False, False, False, True, True, True, False, True, False, True, True, False, True, False, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True, True, True, False, True, False, True, True, False, True, True, False, False]
#reset s0
ek1=[]
ek1.append(True);
bk1=ak1;
for i in range(1, len(ak1)):
    ek1.append(( ak1[i] and (not ek1[i-1]) ) or
        ( (not ak1[i]) and (ak1[i-1] == ek1[i-1]) ))
#Generación de los pulsos de reloj
#t es división de tiempo y s es valor en dicho tiempo
clkt = range(0,len(ak1)*100,100)
clks = tonum(reloj(len(ak1)))
clk2t = range(0,len(ak1)*100,int(100/2))
clk2s = tonum(reloj(len(ak1)*2))

#Generación del pulso de codificación miller
millert = range(0,len(ak1)*100,int(100/2))
millers = []
#+v = +1, -v = -1
for i in range(0, len(ak1)):
    # Nos muestra el valor de bk1 y ek1 para
    # rectificar si está en el estado correcto
    texto = " "+str(bk1[i])+","+str(ek1[i])
    if   bk1[i] == False and ek1[i] == False:
        millers.append(1)
        millers.append(1)
        print "S3 Sc(t)"+texto
    elif bk1[i] == False and ek1[i] == True:
        millers.append(-1)
        millers.append(-1)
        print "S2 Sd(t)"+texto
    elif bk1[i] == True  and ek1[i] == False:
        millers.append(-1)
        millers.append(1)
        print "S1 Sb(t)"+texto
    elif bk1[i] == True  and ek1[i] == True:
        millers.append(1)
        millers.append(-1)
        print "S0 Sa(t)"+texto
        
#Se grafican las señales por medio de step
#Algunas veces hay que hacer modificaciones breves al arreglo
#para su correcta visualización
#clk1
figure(1)
subplot(3,1,1)
step(clkt,tograph(clks))
xlim([clkt[0]-10, clkt[len(clkt)-1]-10])
ylim([-0.5, 1.5])
legend(["CLK"])
'''
#clk2
#figure(2)
subplot(2,1,1)
step(clk2t,clk2s,'--')
xlim([clk2t[0]-10, clk2t[len(clk2t)-1]-10])
ylim([-0.5, 1.5])
'''

#figure(2)#ak+1
subplot(3,1,2)
step(clkt,tograph(ak1))
xlim([clk2t[0]-10, clk2t[len(clk2t)-1]-10])
ylim([-0.5, 1.5])
legend(["a_{k+1}"])
#figure(3)
subplot(3,1,3)
step(millert,tograph(millers))
xlim([millert[0]-10, millert[len(millert)-1]-10])
ylim([-1.5, 1.5])
legend(["Miller"])

show()

#Recuperar ak1
ak1rec=[]
for i in range(0, int(len(millers)/2)):
    if(millers[2*i]==millers[2*i+1]):
        ak1rec.append(False)
    else:
        ak1rec.append(True)

if ak1 == ak1rec:
    print "El mensaje fue recuperado exitosamente."      
else:
    print "El mensaje no fue recuperado con éxito."


figure(2) 
subplot(3,1,1)
step(clkt,tograph(clks))
xlim([clkt[0]-10, clkt[len(clkt)-1]-10])
ylim([-0.5, 1.5])
legend(["CLK"])
#clk2
subplot(3,1,2)
step(clk2t,tograph(clk2s))
xlim([clk2t[0]-10, clk2t[len(clk2t)-1]-10])
ylim([-0.5, 1.5])
legend(["CLK2"])
#Decodificador MILLER  
subplot(3,1,3)
step(clkt,tograph(tonum(ak1rec)))
xlim([clkt[0]-10, clkt[len(clkt)-1]-10])
ylim([-0.5, 1.5])
legend(["Recuperado del Miller"])

show()










