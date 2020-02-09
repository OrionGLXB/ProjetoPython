import numpy as np
def NumeroPrimo(nun):
 Primos = np.array([3, 5, 7, 11, 13, 17, 19])

 par = nun % 2

 if(par == 0):
     print('Numero par não e primo')

 else:
     resultado = nun % Primos

     print(f'{nun} / {Primos[0]} = {resultado[0]}')
     print(f'{nun} / {Primos[1]} = {resultado[1]}')
     print(f'{nun} / {Primos[2]} = {resultado[2]}')
     print(f'{nun} / {Primos[3]} = {resultado[3]}')
     print(f'{nun} / {Primos[4]} = {resultado[4]}')
     print(f'{nun} / {Primos[5]} = {resultado[5]}')
     print(f'{nun} / {Primos[6]} = {resultado[6]}')

nun = int(input('Informe o numero: '))

NumeroPrimo(nun)