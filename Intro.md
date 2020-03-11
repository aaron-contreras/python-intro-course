# Python
## Prof Kevin Gonzalez 21 años

Weekend project:

Hacer un programa orientado a objetos que haga lo siguiente:

1. Cree una clase matriz.
2. Cree un constructor para la clase matriz.
3. Desarrolle los metodos para sumar restar multiplicar y calcular inversa de una matriz.
4. Utilizar sobrecarga de operadores.
5. Utilizar manejo de excepciones en el programa.
6. Hacer las validaciones si se pueden realizar las funciones.
7. NO pueden usar librerias.
8. Subir su repositorio a un repositorio gitlab.

<br>

+ Dynamically allocated memory.
+ No variable declaration.
+ No curly braces -> **use indentation**.
+ Dynamically set types.
+ No pointers.
+ Indentation determines blocks and scope.

<br>

+ **Preferred editor** -> pycharm(university email vives professional license).

+ **:** tells the interpreter that a new block of code is starting.

+ Extension (.py)

+ Method examples
    + print("some string")
    + input("") --> returns string

    + Casting
        + str(thingToCast)
        + int(thingToCast)

+ ### Data types
    + **Numbers**
        + int
        + float
        + complex
            + i(the imaginary number) -> j 
    + **Strings**
        + Strings in python work as char[]
        + x = "Hola mundo"
        + x[2:5] returns "la "
        + `len()` returns the length of the String, array or list.
    + **Lists**
        + Similar to collections in java.
        + Any data type accepted.
        + Build data structures.
        + Casts
            + list(toBeCasted)
    + **Tuples**
        + Are immutable.
        + x = [] -> lists
        + x = {} -> dictionary
        + x = () -> tuples
    + **Dictionaries**
        + `name["key"]`
        + similar to a Java Hash map

+ Syntax
    + One line comments
        ```python
        #This is a comment
        ```
    + Multi-comments
        ```python
        '''
        This is a comment
        '''
        ```
    + Conditionals
        + and
        + or
        + not
        ```python
        if (condition):
            '''
            '''
        else:
            '''
            '''
        ```
        ```python
        if (condition):
            '''
            '''
        elif (condition):
            '''
            '''
        ```
    + Loops
        ```python
        while(condition):
            ''' '''
        ```
        ```python
        for i in range(start,end,step):
        ```
        ```python
        for i in listName:
        # i is not the index, i is the element of the list.
        ```
        + `break` leave the loop
        + `continue` next iteration
        + `pass` ignores the code
    + Functions
        ```python
        def functionName(parameters):
            return optional
        functionName(parameter=parameterValue)
        ```
        + Predetermined parameter values
        ```python
        def fib(n=20):
        # assigns a predetermined value to the function
        ```
    + **"Main"**

        + `if __name__ == "__main__":`
        + __ is private
        + none is public
    + When Python runs the "source file" as the main program, it sets the special variable `(__name__)` to have a value `("__main__")`.

    ```python
    def fib(n):
        result = []
        a,b = 0,1

        while (b<n):
            result.append(b)
            a,b = b,a+b
            # solves backwards to remove the necessity of using a temp variable.
        return result

Haga un programa que pregunte al usuario su edad y muestre en pantalla si es mayor de edad o no.


escriba un programa que pida al usuario un entero positivo y muestre por pantalla los numeros impares de 1 hasta ese numero separado por commas.


escriba una funcion que convierta de un numero decimal a binario y otro de binario a decimal sin usar conversiones de python


crear funcion que reciba un numero y retorne una lista de todos los numeros primos hasta ese numero.
Nota: 1 no es primo.

Homework

Gamma functions --> factorials