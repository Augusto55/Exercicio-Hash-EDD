from distutils import core


class Veiculo:
    def __init__(self):
        self.vetor = [None] * 4
        self._tamanho = 0
    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(self.marca, self.modelo, self.placa, self.renavam, 
        self.exercicio, self.anofabr, self.anomodelo, self.tipo, self.chassi, self.cor, self.combustivel, self.categoria, 
        self.potencia, self.proprietario, self.cpf, self.local, self.data)
    def __repr__(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(self.marca, self.modelo, self.placa, self.renavam, 
        self.exercicio, self.anofabr, self.anomodelo, self.tipo, self.chassi, self.cor, self.combustivel, self.categoria, 
        self.potencia, self.proprietario, self.cpf, self.local, self.data)
    
    def formatar(self, placa):
        return placa.lower()

    def criar_veiculo(self, marca, modelo, placa, renavam, exercicio, anofabr, anomodelo, tipo,
    chassi, cor, combustivel, categoria, potencia, proprietario, cpf, local, data):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.renavam = renavam
        self.exercicio = exercicio
        self.anofabr = anofabr
        self.anomodelo = anomodelo
        self.tipo = tipo
        self.chassi = chassi
        self.cor = cor
        self.combustivel = combustivel
        self.categoria = categoria
        self.potencia = potencia
        self.proprietario = proprietario
        self.cpf = cpf
        self.local = local
        self.data = data
        return self

    def inserir(self, marca, modelo, placa, renavam, exercicio, anofabr, anomodelo, tipo,
    chassi, cor, combustivel, categoria, potencia, proprietario, cpf, local, data):
        self.veiculo = self.criar_veiculo(marca, modelo, placa, renavam, exercicio, anofabr, anomodelo, tipo,
    chassi, cor, combustivel, categoria, potencia, proprietario, cpf, local, data)

        placa_formatada = self.formatar(placa)
        indice = self.funcao_hash(placa_formatada)
        bucket = ""
        boolean = ""

        try:
            bucket = self.vetor[indice]
            boolean = self.contem_boolean(bucket, placa)
        except TypeError:
            pass


        if boolean:
            print("Erro: Placa já está sendo utilizada")
        else:
            try:
                if self.vetor[indice] == None:
                    self.vetor[indice] = [str(self.veiculo)]
                    self._tamanho += 1
                else:
                    try:
                        self.vetor[indice].index(str(self.veiculo))
                    except ValueError:
                        self.vetor[indice].append(str(self.veiculo))
                        self._tamanho += 1
            except TypeError:
                print("Insira uma placa válida")
    
    def contem(self, bucket, placa):
         for i in bucket:
            if(placa in i):
                return i
    
    def contem_boolean(self, bucket, placa):
         for i in bucket:
            if(placa in i):
                return i


    def funcao_hash(self, placa):
        placa1 = placa[0:3]
        
        if placa1 >= "aaa" and placa1 <= "bez":
            return 0
        elif placa1 >= "gkj" and placa1 <= "hok":
            return 1
        elif placa1 >= "iaq" and placa1 <="jdo":
            return 2
        elif placa1 >= "jks" and placa1 <= "jsz":
            return 3
    
    def remover(self, placa):
        placa_formatada = self.formatar(placa)
        indice = self.funcao_hash(placa_formatada)
        bucket = ""

        try:
            bucket = self.vetor[indice]
        except TypeError:
            print("Erro: Registro não foi encontrado")
        
        for i in bucket:
            if(placa in i):
                ind_placa = bucket.index(i)
                self.vetor[indice].pop(ind_placa)
                self._tamanho -= 1
    
    def buscar_por_placa(self, placa):
        placa_formatada = self.formatar(placa)
        indice = self.funcao_hash(placa_formatada)
        bucket = self.vetor[indice]

        try:
            i = self.contem(bucket, placa)
            ind_placa = bucket.index(i)
            print("Registro encontrado: ", self.vetor[indice][ind_placa])
        except TypeError:
            print("Registro não encontrado")

    def mostrar_registros(self):
        print(self.vetor)

    def mostrar_registros_parametros(self, placa, *args):
        placa_formatada = self.formatar(placa)
        indice = self.funcao_hash(placa_formatada)
        bucket = self.vetor[indice]
        i = self.contem(bucket, placa)
        lista = []
        lista_final = []

        try:
            ind_placa = bucket.index(i)
            lista = self.vetor[indice][ind_placa]
            lista_formatada = lista.split(',')
            parametros = [x.lower() for x in args]
            parametros = ''.join(parametros)
            if "marca" in parametros:
                lista_final.append(lista_formatada[0])
            if "modelo" in parametros:
                lista_final.append(lista_formatada[1])
            if "placa" in parametros:
                lista_final.append(lista_formatada[3])
            if "renavam" in parametros:
                lista_final.append(lista_formatada[4])
            if "exercicio" in parametros:
                lista_final.append(lista_formatada[5])
            if "anofabr" in parametros:
                lista_final.append(lista_formatada[6])
            if "anomodelo" in parametros:
                lista_final.append(lista_formatada[7])
            if "tipo" in parametros:
                lista_final.append(lista_formatada[8])
            if "chassi" in parametros:
                lista_final.append(lista_formatada[9])
            if "cor" in parametros:
                lista_final.append(lista_formatada[10])
            if "combustivel" in parametros:
                lista_final.append(lista_formatada[11])
            if "categoria" in parametros:
                lista_final.append(lista_formatada[12])
            if "potencia" in parametros:
                lista_final.append(lista_formatada[13])
            if "proprietario" in parametros:
                lista_final.append(lista_formatada[14])
            if "cpf" in parametros:
                lista_final.append(lista_formatada[15])
            if "local" in parametros:
                lista_final.append(lista_formatada[16])
            if "data" in parametros:
                lista_final.append(lista_formatada[17])
            print("Registro encontrado com os parametros: ", lista_final )
        except (ValueError, TypeError):
            print("Registro não encontrado")
        

    
carro = Veiculo()

carro.inserir("Audi", "A4", "JKS9001", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
carro.inserir("Mercedez", "C200", "JSO9001", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
carro.inserir("Fiat", "Uno", "AAZ1234", "", "", "", "", "", "", "", "", "", "", "", "", "", "")


while True:    
    try:
        insertion = int(input('\n[1] Buscar por placa todos os dados\n[2] Buscar por placa dados específicos\n[3] Inserir nova placa\n[4] Excluir placa\n[5] Mostrar todos os registros\n[6] Encerrar o programa\nDIGITE O NUMERO DA OPÇÃO: '))
        if insertion == 1:
            placa = input("Digite a placa: ")
            carro.buscar_por_placa(placa)
        elif insertion == 2:
            placa = input("Digite a placa: ")
            tupla = input("Insira a placa os dados separados por vírgula: ")
            carro.mostrar_registros_parametros(placa, tupla)
        elif insertion == 3:
            marca = input("Digite a marca: ")
            modelo = input("Digite o modelo: ")
            placa = input("Digite a placa: ")
            renavam = input("Digite o renavam: ")
            exercicio = input("Digite o exercicio: ")
            anofabr = input("Digite o ano de fabricação: ")
            anomodelo = input("Digite o ano do modelo: ")
            tipo = input("Digite o tipo: ")
            chassi = input("Digite o chassi: ")
            cor = input("Digite a cor: ")
            combustivel = input("Digite o combustivel: ")
            categoria = input("Digite a categoria: ")
            potencia = input("Digite a potencia: ")
            proprietario = input("Digite o proprietario: ")
            cpf = input("Digite o cpf: ")
            local = input("Digite o local: ")
            data = input("Digite a data: ")
            carro.inserir(marca, modelo, placa, renavam, exercicio, anofabr, anomodelo, tipo, chassi, cor, combustivel, categoria, potencia, proprietario, cpf, local, data)
        elif insertion == 4:
            placa = input("Digite a placa do registro que quer excluir: ")
            carro.remover(placa) 
        elif insertion == 5:
            carro.mostrar_registros()
        elif insertion == 6:
            break
        else:
            print("Opção inválida!")
    except ValueError:
        print("Opção inválida")