def posCavalo(entrada):     
    if len(entrada) != 5: return('erro')

    linhas = ['1','2','3','4','5','6','7','8']
    colunas = ['a','b','c','d','e','f','g','h']
    p_final =  entrada[slice(3,5)]
    index_l = linhas.index(entrada[1])
    index_c = colunas.index(entrada[0])
    v = [-2,2,-1,1]
    l_check = []
    c_check = []
    pf_vlds = []

    for mov in v:
        if len(linhas) > index_l + mov and index_l + mov > -1: l_check.append(mov)

    for mov in v:
        if len(colunas) > index_c + mov and index_c + mov > -1:  c_check.append(mov)

    for linha in l_check:
        for coluna in c_check:
            if abs(linha) != abs(coluna):
                pf_vlds.append(colunas[index_c+coluna] + linhas[index_l+linha] ) 
            
    if p_final in pf_vlds: return('VÁLIDO')
    else: return('INVÁLIDO')

while 1:
    try:
        entr = input()
        if entr == 'f':
            print('Fim...') 
            break           
        else: print(posCavalo(entr))
    except ValueError: print('erro')