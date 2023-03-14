def CalcNotas(valor):    
    lista_notas = [100, 50, 20, 10, 5, 2]
    lista_moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

    print('\nNOTAS: ')
    for nota in lista_notas:
        if valor >= nota:
            div = valor // nota 
            valor = valor % nota 
            print(str(int((div)))+' nota(s) de R$ ' + str(nota))
        else: print('0 nota(s) de R$ '+ str(nota))

    print('\nMOEDAS: ')
    for moeda in lista_moedas:
        if valor >= moeda:
            div = valor // moeda 
            valor = valor % moeda
            print(str(int((div)))+' moeda(s) de R$ ' +  str(format(moeda,'.2f')))
        else: print('0 moeda(s) de R$ '+ str(format(moeda,'.2f')))

def CasasDecValid(inp):
        try:
            if len(inp) >= 4:
                if inp[-3] == '.': 
                    float(inp)
                    return True 
        except ValueError: return None

entry = input()
if CasasDecValid(entry) == True: CalcNotas(float(entry))
else: print('Erro. Insira um input com duas casas decimais que represente um valor monetário.')
        
