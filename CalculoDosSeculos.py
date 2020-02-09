#~~~~O codigo está incompleto~~~~
#toda vez que alguém digita um ano por exemplo 2000 codigo coloca um seculo a mais
#não conseguir resolver esse problema me desculpem !

def Seculos( ano):
    resultado = ano / 100
    seculo = resultado + 1

    print(f'O Ano é {ano} o seculo é {seculo}')
    print('-' * 30)


print('-'*30)
print('  CALCULO DOS SÉCULOS  ')
print('-'*30)

ano = int(input('Informe o ano para saber o século: '))
Seculos(ano)