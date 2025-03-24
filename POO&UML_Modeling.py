# %%
# ====================================================================================
# Ejercicios de Programación Orientada a Objetos
# 1. Crear una Clase Básica
# Descripción: Crea una clase llamada Persona con atributos como nombre, 
# edad y género. 
# Añade un método para mostrar la información de la persona.
# ====================================================================================

class Persona:

    def __init__(self,name ="",age = 0, genre =""):
        self.name =name
        self.age  =age
        self.genre=genre

    def show(self):
        print(f"Nombre = {self.name}\nEdad = {self.age}\nGenero: {self.genre}")


Joel = Persona()
Joel.name = "Joel"
Joel.age = 26
Joel.genre = "Male"
Joel.show()

# %%
# ====================================================================================
# Descripción: Crea una clase Estudiante que herede de la clase Persona.
# Añade atributos como carrera y promedio.
# ====================================================================================

class Person:
    
    def __init__(self,name = "",age = 0, genre = ""):
        self.name = name
        self.age = age
        self.genre = genre
    
    def show(self):
        return f"Name = {self.name} Age = {self.age} Genre = {self.genre}"

class Student(Person):
    
    def __init__(self, name="", age=0, genre="",career = "" , avg = float(0)):
        super().__init__(name, age, genre)
        self.career = career
        self.avg = avg

    def show(self):
        print(super().show())
        print(f"Career: {self.career} Average:{self.avg}")


a = Person("Joel",26,"Male")
b = Student("Joel",26,"Male","ING Biom",4.52)

b.show()
# %%
# ====================================================================================
# 3. Encapsulamiento
# Descripción: Crea una clase CuentaBancaria con atributos privados como saldo y 
# métodos públicos para depositar y retirar dinero.
# ====================================================================================

class Bank_Account:

    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,x):
        if x > 0:
            self.__balance+=x
            print (f"Cantidad depositada, Nuevo Saldo: {self.__balance}")
        else:
            print("Cantidad Invalida")
    def withdraw (self,x):
        if (x <= self.__balance):
            self.__balance-=x
            print (f"Cantidad retirada, Nuevo Saldo: {self.__balance}")
        else:
            print (f"Saldo insuficiente")


a = Bank_Account(1240)
# %%
# ====================================================================================
# 4. Polimorfismo
# Descripción: Crea una clase base Animal con un método sonido(). Luego, crea clases 
# derivadas como Perro y Gato que sobrescriban el método sonido().
# ====================================================================================
"""
Definir una interfaz común:
La clase Animal actúa como una plantilla para otras clases (subclases).
Indica que todas las subclases de Animal deben tener un método sonido,
pero no proporciona una implementación específica.
Enforzar la implementación en subclases:
Las subclases están obligadas a implementar el método sonido.
Si no lo hacen, se generará un error.
Abstracción:
Permite trabajar con objetos de diferentes subclases de manera uniforme, 
sin preocuparse por los detalles específicos de cada una.
"""
class Animal:

    def sonido(self):
        pass
    

class Perro(Animal):

    def sonido(self):
        return "guau"
    

class Gato(Animal):

    def sonido(self):
        return "miau"
    
b = Perro()
c = Gato()

print(b.sonido())
print(c.sonido())

# %%
# ====================================================================================
# 5. Relaciones entre Clases (Asociación)
# Descripción: Crea una clase Biblioteca que contenga una lista de objetos Libro.
# La clase Libro debe tener atributos como titulo y autor.
# ====================================================================================

class Libro:
    def __init__(self,title,author):
        self.title = title
        self.author = author


class Biblioteca:
    def __init__(self):
        self.books = []


    def add_books(self,book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(f"{book.title} from {book.author}")

library = Biblioteca()
library.add_books(Libro("Harry Potter", "J K Rowlings"))
library.show_books()
        



