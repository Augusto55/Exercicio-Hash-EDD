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
            print("Erro: Placa não foi encontrada")
        
        for i in bucket:
            if(placa in i):
                ind_placa = bucket.index(i)
                self.vetor[indice].pop(ind_placa)
                self._tamanho -= 1

        
carro = Veiculo()
carro.inserir("Audi", "A4", "Augusto", "JKS9001")
carro.inserir("Mercedez", "C200", "Augusto", "JSO9001")
carro.remover("JKS9001")
print(carro.vetor)


        

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