import numpy as np
a = int(input("Digite la base: "))
b = int(input("Digite el exponente: "))
def a_power_b(a,b):
     contP= 1
     print("Si la base digitada es 0, se detendrá la función")
while a != (0): 
    for i in range(0,b,) :
        contP = contP * a
        print(contP)

a_power_b(a,b)
