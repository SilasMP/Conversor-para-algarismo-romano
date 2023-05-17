try:    
    entrada = input('insira o numero que deseja converter: ')
    numero = int(entrada)
    num_romanos = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}

    if numero in num_romanos:
        print(num_romanos[numero])
                
    else:
        def contando_caracteres(): #conta a quantidade de caracteres que possui o valor informado
            return (len(entrada))
       
        def um_caracter(posicao_um): #separa o primeiro grupo de numeros romanos pelo primeiro caracter
            
            if posicao_um < 4:
                return (num_romanos[1]*(posicao_um))
            elif posicao_um == 4:
                return (num_romanos[1]+num_romanos[5])
            elif posicao_um <= 8:
                return (num_romanos[5]+num_romanos[1]*(posicao_um-5))
            elif posicao_um == 9:
                return (num_romanos[1]+num_romanos[10])

        def dois_caracteres(posicao_dois): #separa o segundo grupo de numeros romanos pelo segundo caracter
            
            if posicao_dois != 0:

                if posicao_dois < 4:
                    return (num_romanos[10]*posicao_dois)
                elif posicao_dois == 4:
                    return (num_romanos[10]+num_romanos[50])
                elif posicao_dois <= 8:
                    return (num_romanos[50]+num_romanos[10]*(posicao_dois-5))
                elif posicao_dois == 9:
                    return (num_romanos[10]+num_romanos[100])

            else: return ""
                    
        def tres_caracteres(posicao_tres): #separa o terceiro grupo de numeros romanos pelo terceiro caracter

            if posicao_tres <= 4:
                return (num_romanos[100]*posicao_tres)
            elif posicao_tres == 4:
                return (num_romanos[100]+num_romanos[500])
            elif posicao_tres <= 8:
                return (num_romanos[500]+num_romanos[100]*(posicao_tres-5))
            elif posicao_tres == 9:
                return (num_romanos[100]+num_romanos[1000])     

        match contando_caracteres(): #converte o numero em algoritmo romano concatenando os caracteres
            case 1: print(um_caracter(numero)) #caso 1 caracter
            case 2: print(dois_caracteres(int(entrada[0])) + um_caracter(int(entrada[1]))) #caso 2 caracteres
            case 3: print(tres_caracteres(int(entrada[0])) + dois_caracteres(int(entrada[1]))+ um_caracter(int(entrada[2])))#caso 3 caracteres
            case 4: print('inicialmente este app só converte até o numero 1.000')

except: print("Favor informar um numero inteiro e positivo.")