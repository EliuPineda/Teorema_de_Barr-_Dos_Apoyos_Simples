# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 05:31:30 2020

@author: ELIU
"""

# Por favor introduzca los datos teniendo como referencia laprimera carga izquierda a derecha
l = 15                    #Longitud de viga (m)
p = [200, 300, 300, 100]  #Cargas respecto a la primera carga derecha(kN)
x = [0, 1, 3, 5]          #Posicion global de las cargas respecto al la primera carga izquierda (m)
#----------------------------------------------------------------------------------------------



if len(p)!=len(x):
    print("Revise sus datos")
#Inizialisaciones#############################################################
div = 0
#Viga simplemente apoyada

#_1_Hallar la resultante___# -Sumatoria de momento en p1 = 0
resultante = sum(p) 
for i in range(0, len(x), 1):
    div = div + p[i]*x[i]
    
Xbarra = div/resultante

#_2_Calculo de distancias para Equidistar la resultante a una carga central
for i in range(0, len(x), 1):
    if x[i]>Xbarra:
        a_distancia_carga_cercana_uno = (Xbarra - x[i-1]) 
        a_distancia_carga_cercana_dos = (x[i]-Xbarra) 
        indice_xi_mayor_xbarra = i
        break

print("")
print("La resultante tiene un valor de ",resultante,"kN y está entre las cargas P",i-1," y P",i," a una distancia de", a_distancia_carga_cercana_uno, "m y ", a_distancia_carga_cercana_dos,"m respectivamente")
print("");print("")

#_3_Momentos
        
#Para M1-1 a la izquierda maximo
a = (l/2)+a_distancia_carga_cercana_uno/2 
b = l-a
Ra = resultante*b/l #Resultanrte apoyo
Rb = resultante*a/l #Resultanrte apoyo
#M1-1 Se espera que este sea mayor
m_cargas = 0
d_acargai = 0
for z in range(i-1, -1, -1):
    d_acargai = d_acargai+(x[z+1]-x[z])
    if z==i:d_acargai=0
    m_cargas = m_cargas+(p[z]*(d_acargai))
    #print(z,"-", d_acargai, "-", m_cargas)
M11 = Ra*(a-a_distancia_carga_cercana_uno)-m_cargas

#M1-2  
m_cargas = 0
d_acargai = 0
for z in range(i, -1, -1):
    d_acargai = d_acargai+(x[z+1]-x[z])
    if z==i:d_acargai=0
    m_cargas = m_cargas+(p[z]*(d_acargai))
    #print(z,"-", d_acargai, "-", m_cargas)
M12 = Ra*(a+a_distancia_carga_cercana_dos)-m_cargas

#if a_distancia_carga_cercana_uno < a_distancia_carga_cercana_dos: #Para M1-1 a la izquierda
#    print("Se espera un momento maximo cuando la resultante equidista de la carga P",i-1,"=",p[i-1],"kN la cual está ubicada a ",a-a_distancia_carga_cercana_uno,"m del apoyo izquierdo y a la izquierda de la resultante")
#else:
print("Momentos cuando la resultante equidista de la carga P",i-1,"=",p[i-1],"kN la cual está ubicada a ",a-a_distancia_carga_cercana_uno,"m del apoyo izquierdo y a la izquierda de la resultante")

print("El momento para un corte en la carga P",i-1,"=",p[i-1],"kN es ",M12,"kN-m")    
print("El momento para un corte en la carga P",i,"=",p[i],"kN es ",M11, "kN-m")

#------------------
print("");print("Además");print("")
#------------------    
        

#Para M1-1 a la derecha maximo
a = (l/2)-a_distancia_carga_cercana_dos/2
b = l-a
Ra = resultante*b/l #Resultanrte apoyo
Rb = resultante*a/l #Resultanrte apoyo    
#M1-1 Se espera que este sea mayor 
m_cargas = 0
d_acargai = 0
for z in range(i, -1, -1):
    d_acargai = d_acargai+(x[z+1]-x[z])
    if z==i:d_acargai=0
    m_cargas = m_cargas+(p[z]*(d_acargai))
    #print(z,"-", d_acargai, "-", m_cargas)
M11 = Ra*(a+a_distancia_carga_cercana_dos)-m_cargas 
#M1-2
m_cargas = 0
d_acargai = 0
for z in range(i-1, -1, -1):
    d_acargai = d_acargai+(x[z+1]-x[z])
    if z==i:d_acargai=0
    m_cargas = m_cargas+(p[z]*(d_acargai))
    #print(z,"-", d_acargai, "-", m_cargas)
M12 = Ra*(a-a_distancia_carga_cercana_uno)-m_cargas

#if a_distancia_carga_cercana_dos < a_distancia_carga_cercana_uno: #Para M1-1 a la derecha
#    print("Se espera un momento maximo cuando la resultante equidista de la carga P",i,"=",p[i],"kN la cual está ubicada a ",a+a_distancia_carga_cercana_dos,"m del apoyo izquierdo y a la derecha de la resultante")
#else:
print("Momentos cuando la resultante equidista de la carga P",i,"=",p[i],"kN la cual está ubicada a ",a+a_distancia_carga_cercana_dos,"m del apoyo izquierdo y a la derecha de la resultante")

print("El momento para un corte en la carga P",i-1,"=",p[i-1],"kN es ",M12,"kN-m")    
print("El momento para un corte en la carga P",i,"=",p[i],"kN es ",M11, "kN-m")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
