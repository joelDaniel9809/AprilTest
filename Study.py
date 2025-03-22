import random

# ==========================  
# Ejercicio 1: Número Mayor o Menor
# Descripción: Escribe un programa que solicite al usuario dos números y determine 
# cuál es el mayor o si son iguales. 
# Usa estructuras de decisión (if-else).
# ==========================  

def comparar_numeros():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if num1 > num2:
        print(f"{num1} es mayor que {num2}.")
    elif num2 > num1:
        print(f"{num2} es mayor que {num1}.")
    else:
        print("Ambos números son iguales.")

# # Llamada a la función
# comparar_numeros()

# ==========================  
# Ejercicio 2: Suma de Números Pares
# Descripción: Escribe un programa que sume todos los números 
# pares en un rango dado por el usuario. Usa estructuras de repetición (for o while).
# ==========================  

# define sum_par function
def sum_par():
    #asking for value range to the user
    start = int(input("Defina el inicio de los valores: "))
    end = int(input("Defina el final de los valores: "))

    #checking for start value not being a odd value
    if start % 2 != 0:
        #move start value to an even one
        start+=1
    #initialize Sum variable to collect even values
    Sum = 0
    
    #going from start to end values with step 2 to check only for even values
    for i in range (start , end , 2):
        #adding even value to Sum
        Sum+=i
    #print results to user
    print("La suma de los valores pares es: ",Sum)

# sum_par()


# ==========================  
# Ejercicio 3: Factorial de un Número
# Descripción: Escribe un programa que calcule el factorial de un 
# número dado por el usuario. Usa una función para modularizar el código.
# ==========================  
def fact_calc(x):
    if x == 0 or x ==1:
        return 1
    return x*fact_calc(x - 1)
     
def fact():
    value = int(input("Ingresa un numero para calcular su factorial: "))
    factorial = fact_calc(value);
    print(f"El valor factorial para {value} es: {factorial}")

# fact()


# ==========================  
# Ejercicio 4: Adivina el Número
# Descripción: Escribe un programa que genere un número aleatorio entre 1 y 100, y permita al usuario adivinarlo. 
# El programa debe dar pistas ("muy alto" o "muy bajo") hasta que el usuario adivine el número.
# ==========================  

def rand_guess():
    rNumber = random.randint(1,100);
    guess = rNumber+1
    guessings=0
    while (guess != rNumber):
        guess = int(input("Ingrese el numero generado aleatoriamente: "))
        if(guess < rNumber):
            guessings+=1
            print("Su numero es menor que el generado.")
        elif(guess > rNumber):
            guessings+=1
            print("Su numero es mayor que el generado.")
        else:
            print(f"Felicidades, ha adivinado en {guessings} intentos.")

rand_guess()


# ==========================  
# Ejercicio 5: Tabla de Multiplicar
# Descripción: Escribe un programa que muestre la tabla de multiplicar de un 
# número dado por el usuario. Usa una función para modularizar el código.
# ==========================

def mult(x):
    for i in range (1 , 11):
        print (f"{x} x {i} = {x*i}\n")


def graph():
    valor = int (input("Introdzca el valor del cual se mostrara la tabla: "))
    mult(valor)

# graph()




# Arreglos y estructuras de datos

# ======================================================================================================
# Ejercicio 1: Suma de Elementos de un Arreglo
# Descripción: Escribe un programa que sume todos los elementos de un arreglo (lista) de números enteros.
# ======================================================================================================
# Function to calculate the sum of elements in an array
def arr_sum(x):
    sum = 0  # Initialize a variable to store the sum
    for i in x:  # Iterate through each element in the array
        sum += i  # Add the current element to the sum
    return sum  # Return the total sum

# Function to create an array and calculate the sum of its elements
def value():
    # Ask the user for the length of the array
    lenght = int(input("Enter the number of elements in the array: "))
    
    # Create an array (list) of zeros with the specified length
    arr = [0] * lenght
    
    # Loop to fill the array with user-provided values
    for i in range(0, lenght):
        arr[i] = int(input(f"Enter the value for position {i}: "))  # Store the value in the array
    
    # Print the sum of the elements in the array by calling the `arr_sum` function
    print(f"The sum of the elements is {arr_sum(arr)}")

# Call the `value` function to execute the program
# value()

# ====================================================================================
# Ejercicio 2: Encontrar el Máximo y Mínimo en un Arreglo
# Escribe un programa que encuentre el valor máximo y mínimo en un arreglo de números.
# ====================================================================================

def min_max(x):
    min_val = x[0]
    max_val = x[0]
    for i in x:
        if i< min_val:
            min_val = i
        if i> max_val:
            max_val = i
    return min_val,max_val
def val():
    # Ask the user for the length of the array
    lenght = int(input("Enter the number of elements in the array: "))
    
    # Create an array (list) of zeros with the specified length
    arr = [0] * lenght
    
    # Loop to fill the array with user-provided values
    for i in range(0, lenght):
        arr[i] = int(input(f"Enter the value for position {i}: "))  # Store the value in the array

        # Call min_max function to look for min and max values
        minimo,maximo = min_max(arr)
    # print min and max values to user
    print(f"El valor maximo para el arreglo dado es {maximo} y el valor minimo es {minimo}")
# call for val function to excecute script
val()

# %%
"""
# ====================================================================================
# Ejercicio 3: Invertir un Arreglo
# Descripción: Escribe un programa que invierta el orden de los elementos en un arreglo.
# ===================================================================================="""

# Function that inverts the original function's elements order
def invert(x):

    return x[::-1]
    """secuencia[inicio:fin:paso]
    inicio: Índice desde donde comienza el segmento (incluido). Si se omite, por defecto es 0.
    fin: Índice donde termina el segmento (no incluido). Si se omite, por defecto es el final de la secuencia.
    paso: Define el incremento entre los índices. Si es negativo, la secuencia se recorre en orden inverso."""

    # storing the size of the array
    size = len(x)
    # creating an array with equal size
    y =[0]*size

    # going through original array and assigning values to the second array 
    # using inverse order
    for i in range(0,size):
        y[size - i-1] = x[i]
    # return inverted array
    return y

# function to execute the script
def ex_3():

    # Ask the user for the length of the array
    lenght = int(input("Enter the number of elements in the array: "))

    # Create an array (list) of zeros with the specified length
    arr = [0] * lenght
    
    # Loop to fill the array with user-provided values
    for i in range(0, lenght):
        arr[i] = int(input(f"Enter the value for position {i}: "))  # Store the value in the array
    print (f"El arreglo invertido quedaria {invert(arr)}")

# call for ex_3 function
ex_3()

