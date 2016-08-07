# -*- coding: utf-8 -*-
"""
Created on Sun Nov 09 10:09:49 2014

@author: Jorge
"""
def tomiller(ak1):
    #Reset s0
    ek1=[]
    ek1.append(True);
    bk1=ak1;
    for i in range(1, len(ak1)):
        ek1.append(( ak1[i] and (not ek1[i-1]) ) or
            ( (not ak1[i]) and (ak1[i-1] == ek1[i-1]) ))
    
    #Generación del pulso de codificación miller
    millers = []
    #+v = +1, -v = -1
    for i in range(0, len(ak1)):
        if   bk1[i] == False and ek1[i] == False:
            millers.append(1)
            millers.append(1)
        elif bk1[i] == False and ek1[i] == True:
            millers.append(-1)
            millers.append(-1)
        elif bk1[i] == True  and ek1[i] == False:
            millers.append(-1)
            millers.append(1)
        elif bk1[i] == True  and ek1[i] == True:
            millers.append(1)
            millers.append(-1)
    return millers
  
def prueba2 (vecesprueba,bits,probabilidad1):
    dcak1prom=0
    dcmillerprom=0
    dcak1values=[]
    dcmillervalues=[]
    for i in range(0, vecesprueba):  
        ak1=flujobinario(bits,probabilidad1)        
        miller=tomiller(ak1)
        valor1=float(sum(tovoltage(ak1)))/len(ak1)
        dcak1values.append(valor1)
        valor2=float(sum(miller))/len(miller)
        dcmillervalues.append(valor2)
    dcak1prom=float(sum(dcak1values))/len(dcak1values)
    dcmillerprom=float(sum(dcmillervalues))/len(dcmillervalues)
    print "El valor DC Promedio del mensaje: "+ str("%.12f" % dcak1prom)
    print "El valor DC Promedio del miller: "+ str("%.12f" % dcmillerprom)
    if abs(dcak1prom) < abs(dcmillerprom):
        print "El DC del miller es menor que la del mensaje"
    
def prueba (bits,probabilidad1):
    dcak1prom=0
    dcmillerprom=0
    ak1=flujobinario(bits,probabilidad1)        
    miller=tomiller(ak1)
    dcak1prom=float(sum(tovoltage(ak1)))/len(ak1)
    dcmillerprom=float(sum(miller))/len(miller)
    print "El valor DC del mensaje: "+ str("%.12f" % dcak1prom)
    print "El valor DC del miller: "+ str("%.12f" % dcmillerprom)
    if abs(dcmillerprom) < abs(dcak1prom):
        print "El DC del miller es menor que la del mensaje"    
    
    
    
    
    
    
    
    
    
    
    
    
    