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
# ====================================================================================
# Ejercicio 3: Invertir un Arreglo
# Descripción: Escribe un programa que invierta el orden de los elementos en un arreglo.
# ====================================================================================

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
# %%
# ====================================================================================
# Ejercicio 4: Implementar una Pila (Stack)
# Descripción: Implementa una pila usando una lista en Python. Debe incluir operaciones 
# para agregar (push), eliminar (pop) y ver el elemento en el tope (peek).
# ====================================================================================

# Class with all modules
class Stack:

    # class constructor
    def __init__(self):
        self.items = []
    
    # Push module with functionality for adding a value to the end of the stack
    def push(self,x):
        self.items.append(x)

    # Pop module with functionality for deleting a value from the end of the stack
    def pop(self):
        if len(self.items):
            return self.items.pop()
        return None
    
    # Peek module with functionality for returnof the value to the end of the stack
    def peek(self):
        if len(self.items):
            return self.items[-1]
        return None
    
    # returns True if there are no values on the stack and False if there is
    def is_empty(self):
        if len(self.items):
            return False
        return True

    
def ex_4():
    pila = Stack()
    pila.push(10)
    pila.push(20)
    pila.push(30)
    
    print(pila.peek()) 
    
    while pila.is_empty() != True:
        print(f"Elemento eliminado {pila.pop()}")

ex_4()
# %%
# ====================================================================================
# Ejercicio 5: Contar Frecuencia de Elementos en un Arreglo
# Descripción: Escribe un programa que cuente la frecuencia de cada elemento en un arreglo
# y almacene los resultados en un diccionario.
# ====================================================================================

def count_freq(arr):
    dicc = {}
    for i in arr:
        if i in dicc:
            dicc [i] +=1; 
        else:
            dicc[i] = 1
    return dicc

def ex_5():
    
    arr = []
    value = 1
    
    while value != "0":
        value = input()
        arr.append(value)
    
    dicc = count_freq(arr)
    print(dicc)

ex_5()
# %%
# Manejo de cadena de caracteres
# ====================================================================================
# Ejercicio 1: Contar Vocales en una Cadena
# Descripción: Escribe un programa que cuente el número de vocales (a, e, i, o, u) 
# en una cadena de texto ingresada por el usuario.recuencia de cada elemento en un 
# arreglo
# ====================================================================================
def vowel_count(chain):

    vowels = "aeiouAEIOU"
    count =0
    for a in chain:
        if a in vowels:
            count+=1
    return count

def ex_1():
    chain = "QWERTYUIOPasdfghjklzxcvbnm"
    vowels = vowel_count(chain)
    print(vowels)

ex_1()
# %%
# ====================================================================================
# Ejercicio 2: Invertir una Cadena
# Descripción: Escribe un programa que invierta una cadena 
# de texto ingresada por el usuario.
# ====================================================================================

def invert(chain):
    return chain[::-1]


def ex_2():
    chain = "JoelDaniel"
    print(invert(chain))

ex_2()
    # %%
# ====================================================================================
# Ejercicio 3: Contar Palabras en una Cadena
# Descripción: Escribe un programa que cuente el número de palabras
# en una cadena de texto ingresada por el usuario
# ====================================================================================
def count_w(chain):
    words = chain.split()
    return len(words)

def ex_3():
    chain = "Joel Daniel Matos Diaz"
    print(count_w(chain))

ex_3()

    # %%
# ====================================================================================
# Ejercicio 4: Reemplazar Caracteres en una Cadena
# Descripción: Escribe un programa que reemplace todas las ocurrencias de un carácter
# específico en una cadena de texto por otro carácter.
# ====================================================================================

def repl(chain,a):
    n_chain = chain.replace(a,"*")
    return n_chain

def ex_4():
    chain = "Joel Daniel Matos Diaz"
    print(repl(chain,"e"))

ex_4()
    # %%
# ====================================================================================
# Ejercicio 5: Verificar si una Cadena es un Palíndromo
# Descripción: Escribe un programa que verifique si una cadena de texto es 
# un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
# ====================================================================================

def pal(chain):
    chain = chain.replace(" ","").lower()

    return chain == chain[::-1]

def ex_5():
    chain = "ab Ba"
    print(pal(chain))

ex_5()
# %%
# Recursividad. 
# ====================================================================================
# Ejercicio 1: Factorial de un Número
# Descripción: Escribe una función recursiva para calcular el factorial de un número. 
# El factorial de un número n(denotado como n!) es el producto de todos los enteros positivos desde 1 hasta n
# ====================================================================================

def fact (n):
    if (n == 1 or n == 0):
        return 1
    return n*fact(n-1)

def ex_1():
    numb  = 6
    print (fact(numb))

ex_1()
# %%
# Recursividad. 
# ====================================================================================
# Ejercicio 1: Factorial de un Número
# Descripción: Escribe una función recursiva para calcular el factorial de un número. 
# El factorial de un número n(denotado como n!) es el producto de todos los enteros positivos desde 1 hasta n
# ====================================================================================

def fact (n):
    if (n == 1 or n == 0):
        return 1
    return n*fact(n-1)

def ex_2():
    numb  = 6
    print (fact(numb))

ex_2()
# %%
# ====================================================================================
#Ejercicio 3: Fibonacci Recursivo
# Descripción: Escribe una función recursiva para calcular el n-ésimo número de 
# la secuencia de Fibonacci. La secuencia de Fibonacci comienza con 0 y 1,
# y cada número subsiguiente es la suma de los dos anteriores. 
# ====================================================================================

def fibb (n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibb(n-1) + fibb (n-2)


def ex_4():
    numb  = 6
    print (fibb(numb))

ex_4()
# %%
# ====================================================================================
# Ejercicio 5: Búsqueda Binaria Recursiva
# Descripción: Implementa una función recursiva para realizar una búsqueda binaria en
# una lista ordenada. La búsqueda binaria divide repetidamente la lista en dos mitades y 
# busca el elemento en la mitad correspondiente.
# ====================================================================================

def bin_search(list,target,start,end):
    
    if start > end:
        return -1
    # Con //, obtienes un número entero, que es lo que necesitas para acceder a un elemento en una lista.
    half = (start+end)//2
    
    if list[half] == target:
        return half
    elif list[half] < target:
        return bin_search(list,target,start,half-1)
    elif list[half] < target:
        return bin_search(list,target,half+1,end)

def ex_5():
    list = [1,2,4,5,7,9,10,13,15,16]
    target = 7

    print (bin_search(list,target,0,len(list)-1))

ex_5()

# %%
# Manejo de archivos
# ====================================================================================
# Ejercicio 1: Leer un Archivo de Texto
# Descripción: Escribe un programa que lea un archivo de texto y muestre 
# su contenido en la consola.
# ====================================================================================
"""El bloque with garantiza que el recurso (en este caso, el archivo) se cierre 
automáticamente después de que se complete el bloque de código, incluso si ocurre 
una excepción."""

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:  # Abre el archivo en modo lectura
        contenido = archivo.read()  # Lee todo el contenido del archivo
        print(contenido)  # Imprime el contenido
    # El archivo se cierra automáticamente al salir del bloque 'with'
# Llamada a la función
leer_archivo("archivo.txt")

# %%
# ====================================================================================
# Ejercicio 2: Escribir en un Archivo de Texto
# Descripción: Escribe un programa que permita al usuario ingresar texto
# y lo guarde en un archivo.
# ====================================================================================

def mod_file(file_name,text_to_add):
    with open(file_name,"w") as file:
        file.write(text_to_add)
    with open(file_name,"r") as file:
        content = file.read()
        print(content)

mod_file("archivo.txt","Hello World")

# %%
# ====================================================================================
# Ejercicio 3: Contar Líneas en un Archivo
# Descripción: Escribe un programa que cuente el número de
# líneas en un archivo de texto.
# ====================================================================================
def count_lines(file_name):
    with open(file_name,"r") as file:
        lines = file.readlines()
        return len(lines)
    
print (count_lines("archivo.txt"))

# %%
# ====================================================================================
# Ejercicio 4: Copiar un Archivo
# Descripción: Escribe un programa que copie el contenido de un archivo 
# a otro archivo.
# ====================================================================================

def copy_file(file_name_1,file_name_2):
    with open (file_name_1,"r") as file_1:
        content = file_1.read()
    with open(file_name_2,"w") as file_2:
        file_2.write(content)

copy_file("file_1.txt","file_2.txt")

# %%
# ====================================================================================
# Ejercicio 5: Buscar una Palabra en un Archivo
# Descripción: Escribe un programa que busque una palabra en un archivo de texto y
# muestre las líneas donde aparece.
# ====================================================================================

def find_word(file_name,find):
    with open(file_name,"r") as file:
        content = file.readlines()
    for i in range(0 , len(content)):
        if content[i].find(find) != -1:
            print (f"Su texto se encuentra en la linea {i+1}.")
    
find_word("file_1.txt","here")

""""Solucion de la IA"""
# def buscar_palabra(nombre_archivo, palabra):
#     with open(nombre_archivo, "r") as archivo:
#         lineas = archivo.readlines()
#         for i, linea in enumerate(lineas, 1):
#             if palabra in linea:
#                 print(f"Línea {i}: {linea.strip()}")

# # Llamada a la función
# buscar_palabra("archivo.txt", "Python")