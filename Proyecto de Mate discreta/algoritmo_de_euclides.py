print("Algoritmo de EUCLIDES")
print("Si tenemos dos numeros enteros positivos, a y b, tales que a=b>=0:")
print("a=b*q+r")
print("Ejemplo: \n")
print("Encontrar el m.c.d de 101-13\n")
print("101=13*7+10")
print("13=10*1+3")
print("10=3*3+1")
print("3=1*3+0")
print("El m.c.d de 101 y 13 es: 1\n")
#variable para tomar los numeros
def AlgoritmoDeEuclides(numero1, numero2):
    #el bucle se ejecutaran hasta que la division de los numeros sea igual a 0
    while numero2 != 0:
        numero1, numero2 = numero2, numero1 % numero2
    return numero1
print("Este es un progrma que le ayudara a encontrar el MCD de dos numeros por medio del algoritmo de EUCLIDES")

#inputs para pedir valores
numero1 = int(input("Infrese el primer numero: ")) 
numero2 = int(input("Ingrese el segundo numero: ")) 

resultados = AlgoritmoDeEuclides(numero1, numero2)
#imprimimos los resultados
print("Se toma el valor del dividiendo: ", numero1, "Se toma el resto de: ", numero1 )
print("El MCD de", numero1, "y", numero2, "es: ", resultados)
