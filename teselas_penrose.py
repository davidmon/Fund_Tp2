# -*- coding: utf-8 -*-
from turtle import *
import math

def lindenmayerPenrose(instante):
	lindenmayer = '[7]LL[7]LL[7]LL[7]LL[7]'
        for i in range(instante):
            aux = ""
            for l in lindenmayer: 
                if(l == '6'):
                    aux += '81LL91RRRR71[R81RRRR61]LL'
                if(l == '7'):
                    aux += 'L81RR91[RRR61RR71]L'
                if(l == '8'):
                    aux += 'R61LL71[LLL81LL91]R'
                if(l == '9'):
                    aux += 'RR81LLLL61[L91LLLL71]RR71'
                if(l == '1'):
                    aux += ''
                if(l == 'L'):
                	aux += l
            	if(l == 'R'):
                	aux += l
            	if(l == '['):
                	aux += l
            	if(l == ']'):
                	aux += l
            lindenmayer = aux
	return lindenmayer 

def calcularPuntos(cadena,angulo,lado):
	ang = 0
	pila = []
	puntos = {}
	n=0
	puntos[n] = [0,0,0,0]
	for l in cadena: 
		if(l == '1'):
			x_calc = puntos[n][1]+math.cos(math.radians(float(ang)))*lado
			x_trunc = "%.2f" % x_calc
			x = float(x_trunc)
			y_calc = puntos[n][2]+math.sin(math.radians(float(ang)))*lado
			y_trunc ="%.2f" % y_calc
			y = float(y_trunc)
			n += 1
			puntos[n]=[n,x,y,ang]
		if(l == 'R'):
			ang = ang+angulo
		if(l == 'L'):
			ang = ang-angulo
		if(l == '['):		
			apilar_x = puntos[n][1]
			apilar_y = puntos[n][2]	
			apilar_ang = ang
			pila.append(apilar_x)
			pila.append(apilar_y)
			pila.append(apilar_ang)
		if(l == ']'):
			desapilar_ang = pila.pop()
			desapilar_y = pila.pop()
			desapilar_x = pila.pop()
			n+=1
			puntos[n]=[n,desapilar_x,desapilar_y,desapilar_ang]
			ang = desapilar_ang
	return puntos	

def graficar (puntos):

	hideturtle()
	speed(5)
	wn = Screen()
	wn.bgcolor("white")
	wn.title("Trabajo Practico n 3")
	pensize(2)
	fillcolor("red")
	begin_fill()
	for punto in puntos.items():
		goto(punto[1][1],punto[1][2])		
	end_fill()
	wn.exitonclick()

cadena = lindenmayerPenrose(3)
graficar(calcularPuntos(cadena,36,40))
