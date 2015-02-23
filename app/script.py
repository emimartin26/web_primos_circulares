#! /usr/bin/python


import sys
import math
import random
import threading 
import time

# Declaro y inicializo variables globales.
BANDERA_THREDS = 0
CONTADOR_NUMEROS = 0
PRIMOS_CIRCULARES = []




# Recibe un numero en formato string y lo devuelve rotado en formato string
def rotar_numero(numero):
	pila = []
	numero_rotado = ""
	for digito in numero:
		pila.append(digito)

	primer_digito = pila.pop(0)
	pila.append(primer_digito)

	for digito in pila:
		numero_rotado = numero_rotado + digito

	
	return numero_rotado



#Recibo como parametro dos numeros "x" e "y".
#Obetengo como resultado el maximo comun divisor
def mcd(x,y):
	while y != 0:
		z = x % y
		x = y
		y = z
	return x


#Tengo como entrada factor, power, modulus
#Y la salida sera: factor^power % modulus 
def faster_mod(factor,power,modulus):
	result = 1
	while power > 0:
		if power % 2 == 1:
			result = (result*factor) % modulus
			power = power -1
		power = power / 2
		factor = (factor*factor)%modulus

	return result


# Toma como parametro un numero entero string y retorna
# True si es primo
def metodo_fermat_es_primo(numero):
	numero = int(numero)
	numPasos = 20
	# Repetimos hasta lograr un grado de confianza definido en la
	# variable numPasos 
	for x in range(0,numPasos):
		#Genero numero aleatorio entre 1 y numero - 1
		num_aleatorio = random.randint(1, numero-1)

		# Si el maximo comun divisor del numero aleatorio y el numero ingresado es distinto de uno,
		# el numero es compuesto, por la tanto, no es primo.
		if mcd(num_aleatorio,numero) != 1:
			return False

		# Si se cumple el teorema de fermat, numero es compuesto
		# a^(n-1) (mod n) != 1 entonces n es compuesto
		if faster_mod(num_aleatorio,numero-1, numero) != 1:
			return False

	return True




# Toma como parametro un numero y devuelve True si es primo circular
def es_primo_circular(numero):
	global PRIMOS_CIRCULARES
	if not(metodo_fermat_es_primo(numero)): # Si no es primo tampoco puede ser primo circular
		return False

	long_num = len(numero)
	aux_numero = numero
	for i in range(1,long_num):
		aux_numero = rotar_numero(aux_numero)
		if not(metodo_fermat_es_primo(aux_numero)):# Si un numero obtenido de la rotacion no es primo entonces tampoco es circular
			return False

	
	PRIMOS_CIRCULARES.append(int(numero))
	return True



# Toma como parametro dos enteros y genera numeros entre esos dos paramtros
# Para cada numero generado se verifica si es primo circular
def simular(limite_inferior, limite_superior,num_th):
	global CONTADOR_NUMEROS
	global BANDERA_THREDS
	for i in range(limite_inferior,limite_superior):
		numero = str(i)
		CONTADOR_NUMEROS = CONTADOR_NUMEROS + 1
		es_primo_circular(numero)
	
	BANDERA_THREDS = BANDERA_THREDS + 1

# Este es un hilo que esta escuchando una variable global BANDERA_THERDS
# con la finalidad de ir mostrando el progreso del procesamiento de los numeros.
def hilo_main():
	global BANDERA_THREDS
	limite = 1000000	
	while BANDERA_THREDS != 16:
		progreso = ((CONTADOR_NUMEROS * 100) / (limite))
		sys.stdout.write("\rProcesando Numeros... %d%%" % progreso)
		sys.stdout.flush()

	sys.stdout.write("\r")
	print "Los numeros primos circulares son los siguientes: "
	for n in sorted(PRIMOS_CIRCULARES):
		print ("Numero: " + str(n))

	return


# Proceso principal del script.
def main():
	# Declaro un hilo y como parametro le paso la funcion que debe ejecutar.
	t = threading.Thread(target=hilo_main)

	# Declaro 16 hilos y les paso como parametro la funcion que deben ejecutar y el rango de numero
	# que deben verificar si son primos circulares	
	t1 = threading.Thread( target=simular, args=(2, 62500, "1") )
	t2 = threading.Thread( target=simular, args=(62500, 125000, "2") )
	t3 = threading.Thread( target=simular, args=(125000, 187500, "3") )
	t4 = threading.Thread( target=simular, args=(187500, 250000, "4") )
	t5 = threading.Thread( target=simular, args=(250000, 312500, "5") )
	t6 = threading.Thread( target=simular, args=(312500, 375000, "6") )
	t7 = threading.Thread( target=simular, args=(375000, 437500, "7") )
	t8 = threading.Thread( target=simular, args=(437500, 500000, "8") )
	t9 = threading.Thread( target=simular, args=(500000, 562500, "9") )
	t10 = threading.Thread( target=simular, args=(562500, 625000, "10") )
	t11 = threading.Thread( target=simular, args=(625000, 687500, "11") )
	t12 = threading.Thread( target=simular, args=(687500, 750000, "12") )
	t13 = threading.Thread( target=simular, args=(750000, 812500, "13") )
	t14 = threading.Thread( target=simular, args=(812500, 875000, "14") )
	t15 = threading.Thread( target=simular, args=(875000, 937500, "15") )
	t16 = threading.Thread( target=simular, args=(937500, 1000000, "16") )
	
	
	# Ejecuto todos los hilos para que comiencen el procesamiento
	t.start()
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t5.start()
	t6.start()
	t7.start()
	t8.start()	
	t9.start()
	t10.start()
	t11.start()
	t12.start()
	t13.start()
	t14.start()
	t15.start()
	t16.start()


if __name__=="__main__":main()