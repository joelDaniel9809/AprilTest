# ==========================  
# Ejercicio 1
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

# Llamada a la función
comparar_numeros()