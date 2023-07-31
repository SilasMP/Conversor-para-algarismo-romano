class Conversor:

    def __init__(self):
        try:
            self.entrada = input('insira o numero que deseja converter: ')
            self.numero = int(self.entrada)
            self.num_romanos = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
            self.gerador()
        except:
            print("Favor informar um numero inteiro e positivo.")
            Conversor()

    def contando_caracteres(self): #conta a quantidade de caracteres que possui o valor informado
        return (len(self.entrada))
       
    def um_caracter(self, posicao_um): #separa o primeiro grupo de numeros romanos pelo primeiro caracter
        
        if posicao_um < 4:
            return (self.num_romanos[1]*(posicao_um))
        elif posicao_um == 4:
            return (self.num_romanos[1]+self.num_romanos[5])
        elif posicao_um <= 8:
            return (self.num_romanos[5]+self.num_romanos[1]*(posicao_um-5))
        elif posicao_um == 9:
            return (self.num_romanos[1]+self.num_romanos[10])

    def dois_caracteres(self, posicao_dois): #separa o segundo grupo de numeros romanos pelo segundo caracter
        
        if posicao_dois != 0:

            if posicao_dois < 4:
                return (self.num_romanos[10]*posicao_dois)
            elif posicao_dois == 4:
                return (self.num_romanos[10]+self.num_romanos[50])
            elif posicao_dois <= 8:
                return (self.num_romanos[50]+self.num_romanos[10]*(posicao_dois-5))
            elif posicao_dois == 9:
                return (self.num_romanos[10]+self.num_romanos[100])

        else: return ""
                
    def tres_caracteres(self, posicao_tres): #separa o terceiro grupo de numeros romanos pelo terceiro caracter

        if posicao_tres <= 4:
            return (self.num_romanos[100]*posicao_tres)
        elif posicao_tres == 4:
            return (self.num_romanos[100]+self.num_romanos[500])
        elif posicao_tres <= 8:
            return (self.num_romanos[500]+self.num_romanos[100]*(posicao_tres-5))
        elif posicao_tres == 9:
            return (self.num_romanos[100]+self.num_romanos[1000])     

    def gerador(self):
        
        if self.entrada in self.num_romanos:
            return print(self.num_romanos[self.entrada])
        
        match self.contando_caracteres(): #converte o numero em algoritmo romano concatenando os caracteres
            case 1: print(self.um_caracter(self.numero)) #caso 1 caracter
            case 2: print(self.dois_caracteres(int(self.entrada[0])) + self.um_caracter(int(self.entrada[1]))) #caso 2 caracteres
            case 3: print(self.tres_caracteres(int(self.entrada[0])) + self.dois_caracteres(int(self.entrada[1]))+ self.um_caracter(int(self.entrada[2])))#caso 3 caracteres
            case 4: print('inicialmente este app só converte até o numero 1.000')
        Conversor()
        
if __name__ == '__main__':
    conv_romano = Conversor()