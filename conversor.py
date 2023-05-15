try: #tratamento caso o usuario digite uma letra, ou um numero no input
    entrada = input('insira o numero que deseja converter: ')
    numero = int(entrada)
    num_romanos = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}

    def contando_caracteres(): #conta a quantidade de caracteres que possui o valor informado
        return (len(entrada))

    def separar_dezenas(): #gera a repeticão de vezes que a dezena aparece no numero com o algarismo X
        
        if (len(entrada[1:3])) == 2:
            num = numero - int(entrada[1:3])-800
            dezena = num / 100
            return(int(dezena)*"X")
        else:
            num = numero - int(entrada[1])-50
            dezena = num / 10
            return(int(dezena)*"X")

    def separar_centenas(): #gera a repeticão de vezes que a centena aparece no numero com o algarismo C
        vl_cen = numero - int(entrada[1:3])-500
        centena = vl_cen / 100
        return(int(centena)*"C")

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
        
        if posicao_dois <= 39:
            return (num_romanos[10]*int(entrada[0]))
        elif posicao_dois <= 49:
            return (num_romanos[10]+num_romanos[50])
        elif posicao_dois <= 89:
            return (num_romanos[50]+ separar_dezenas())
        elif posicao_dois <=99:
            return (num_romanos[10]+num_romanos[100])
        
    def tres_caracteres(posicao_tres): #separa o terceiro grupo de numeros romanos pelo terceiro caracter

        if posicao_tres <= 399:
            return (num_romanos[100]*int(entrada[0]))
        elif posicao_tres <=499:
            return (num_romanos[100]+num_romanos[500])
        elif posicao_tres <= 899:
            return (num_romanos[500]+ separar_centenas())
        elif posicao_tres <= 999:
            return (num_romanos[100]+num_romanos[1000])     

    match contando_caracteres(): #converte o numero em algoritmo romano concatenando os caracteres
        case 1: print(um_caracter(numero)) #caso 1 caracter
        case 2: print(dois_caracteres(numero) + um_caracter(int(entrada[1]))) #caso 2 caracteres
        case 3: print(tres_caracteres(numero) + dois_caracteres(int(entrada[1:3]))+ um_caracter(int(entrada[2])))#caso 3 caracteres
        case 4: 
            if numero == 1000:
                print('M')
            else:
                print('inicialmente este app só converte até o numero 1.000') #caso 4 caracteres
        case _:
            print('inicialmente este app só converte até o numero 1.000')


except:
    print("Favor digite um numero inteiro e positivo") 