lista = []
while 1 :
    valor = input()
    if valor == 'f': break
    elif valor.isnumeric() == True: lista.append(int(valor))
    
conjunto = set(lista)
for valor in conjunto:
    if lista.count(valor) == 1: print('O número ' + str(valor) + ' apareceu uma vez.')
    else: print('O número ' + str(valor) + ' apareceu ' + str(lista.count(valor))+ ' vezes.')
print('Fim...')
