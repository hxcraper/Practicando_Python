'''
def sumar(n1, n2):
    res = n1 + n2
    return res

def restar(n1, n2):
    res = n1 - n2
    return res

def multiplicar(n1, n2):
    res = n1 * n2
    return res

def dividir(n1, n2):
    res = n1 / n2
    return res

n1 = input('Ingresa un numero: ')
n2 = input('Ingresa otro numero: ')

n1 = int(n1);
n2 = int(n2);

print(f'La suma de {n1} y {n2} es: {sumar(n1,n2)}')
print(f'La resta de {n1} y {n2} es: {restar(n1,n2)}')
print(f'La multiplicacion de {n1} y {n2} es: {multiplicar(n1,n2)}')
print(f'La divicion de {n1} y {n2} es: {dividir(n1,n2)}')
'''

'''
Funciones
'''

# simple 

def saludo():
    print('Hola kike')

saludo()

# con retorno

def saludo_retorno():
    return 'Hola pedro'

saludo = saludo_retorno()
print(saludo)
print(saludo_retorno())

# funcion con un argumento

def argumento_saludo(nombre):
    print(f'Hola, {nombre} ! !')

argumento_saludo('kike')

# funcion con un argumentos

def argumento_saludo(nombre, apellido):
    print(f'Hola, {nombre} {apellido} ! !')

argumento_saludo(apellido='kike', nombre='burotto') # para poder cambiar el orden en caso de...

# funcion con un argumento predeterminado

def argumento_predeter_saludo(nombre="juan"):
    print(f'Hola, {nombre}  ! !')

argumento_predeter_saludo()

# con argumentos y retorno

def return_args_greet(greet, name):
    print(f'{greet} {name}')


# retorno con varios valores

def multiple_return_greet():
    return "Hola" , "kike"

greet, name = multiple_return_greet()
print(greet)
print(name)

# con un numero variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f'Hola, {name} ! ! !')

variable_arg_greet('kike', 'juan', 'pedro')

# con un numero variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items(): # el items, descontructura la variable
        print(f'{value} ({key}) !! ')

variable_key_arg_greet (
    lenguaje = "Python",
    name = "Enrique",
    alias = "kike",
    age = 30
)

''' FUNCIONES DENTRO DE OTRAS FUNCIONES '''

def outer_funtion():
    def inner_funtion():
        print("Función interna: Hola Python !!!")
    inner_funtion()

outer_funtion()


'''
Funciones del lenguaje (built-in)
'''

print(len("Enrique Burotto" )) # nos cuenta los caracteres
print(type(33)) # nos da el tipo de dato, en este caso int
print("kike".upper()) # nos transforma en mayuscula
print("KIKE".lower()) # nos transforma en minuscula

'''
Variables locales y globales
'''

global_variable = "Python"

print(global_variable)

def hellow_python():
    local_var = "Hola"
    print(f'{local_var}, {global_variable}')

hellow_python()

# print(local_var) -> No se puede acceder desde fuera de la funcion

'''
EXTRA
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
'''

'''
c1 = input("Ingresa una palabra")
c2 = input("Ingresa otra palabra")

def dosParametros(c1, c2):
    c1_len = len(c1)
    c2_len = len(c2)
    res_gen = c1_len + c2_len
    return res_gen

print(f'la suma de caracteres de {c1} y {c2} es : {dosParametros(c1,c2)}')



def unoAlCien():
    for i in range(1, 101):
        if i = 
        print(i)

unoAlCien()
'''

'''Este tipo de ejercicio se llama FIZ BUZZ'''

def print_numbers(text_1, text_2) -> int:
    for number in range(1 , 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
        

print_numbers("Multiplo de 3"," Multiplo de 5")












