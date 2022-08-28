class Veiculo:
    def __init__(self):
        self.vetor = [None] * 4
        self._tamanho = 0
    def __str__(self):
        return '{}, {}, {}, {}'.format(self.marca, self.modelo, self.proprietario, self.placa)
    def __repr__(self):
        return '{}, {}, {}, {}'.format(self.marca, self.modelo, self.proprietario, self.placa)
    
    def formatar(self, placa):
        return placa.lower()

    def criar_veiculo(self, marca, modelo, proprietario, placa):
        self.marca = marca
        self.modelo = modelo
        self.proprietario = proprietario
        self.placa = placa
        return self

    def inserir(self, marca, modelo, proprietario, placa):
        self.veiculo = self.criar_veiculo(marca, modelo, proprietario, placa)

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
        i = self.contem(bucket, placa)

        try:
            ind_placa = bucket.index(i)
            print("Registro encontrado: ", self.vetor[indice][ind_placa])
        except ValueError:
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
            if "marca" in args:
                lista_final.append(lista_formatada[0])
            if "modelo" in args:
                lista_final.append(lista_formatada[1])
            print("Registro encontrado com os parametros: ", lista_final )
        except ValueError:
            print("Registro não encontrado")

    

    
carro = Veiculo()
carro.inserir("Audi", "A4", "Augusto", "JKS9001")
carro.inserir("Mercedez", "C200", "Augusto", "JSO9001")
carro.inserir("Fiat", "Uno", "Augusto", "AAZ1234")
# carro.inserir("Renault", "Kwid", "Pai careca do GS", "JSO9001")
# carro.remover("JKS9001")
#carro.buscar_por_placa("JSO9001")
carro.mostrar_registros_parametros("JSO9001", "marca", "modelo")
carro.mostrar_registros()


        

# while True:    
#     try:
#         insertion = int(input('\n[1] Buscar por placa todos os dados\n[2] Buscar por placa dados específicos\n[3] Inserir nova placa\n[4] Excluir placa\n[5] Mostrar todos os registros\nDIGITE O NUMERO DA OPÇÃO: '))
#         if insertion == 1:
#             pass
#         elif insertion == 2:
#             pass
#         elif insertion == 3:
#             pass
#         elif insertion == 4:
#             pass
#         elif insertion == 5:
#             pass
#         elif insertion == 6:
#             break
#         else:
#             print("Opção inválida!")
#     except ValueError:
#         print("O valor deve ser um número inteiro")