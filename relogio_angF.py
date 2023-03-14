def calcAngulo(hora,minut):  
    if hora > 12: hora = hora - 12
         
    #Para uma resposta exata, que considera o movimento do ponteiro da hora a cada minuto, e não a cada hora, pode-se substituir a variável angulo_pH = ((hora*60) + minut)*0.5
    angulo_pH = hora * 30  
    angulo_pM = minut * 6
    angulo_0 = abs(angulo_pH - angulo_pM) 
    angulo = min(angulo_0, 360 - angulo_0)

    return angulo

while 1:
    try:
        horario = input()
        if horario == 'f': 
            print('Fim...') 
            break 

        hora = int(horario[slice(0,2)])
        minut = int(horario[slice(3,5)])

        if hora > 23 or minut > 59 or len(horario) != 5 or horario[2] != ':':
             print("Input Inválido")            
        else:
            print('O menor ângulo é ' + str(calcAngulo(hora,minut)) + '°')

    except ValueError or NameError :
        print("Input Inválido")