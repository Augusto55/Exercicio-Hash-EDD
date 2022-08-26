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
        veiculo = self.criar_veiculo(marca, modelo, proprietario, placa)

        placa_formatada = self.formatar(placa)
        indice = self.funcao_hash(placa_formatada)

        print(indice)

        if self.vetor[indice] == None:
            self.vetor[indice] = [str(veiculo)]
            self._tamanho += 1
        else:
            try:
              self.vetor[indice].index(str(veiculo))
            except ValueError:
              self.vetor[indice].append(str(veiculo))
              self._tamanho += 1

    def funcao_hash(self, placa):
        placa1 = placa[0:3]
        placa2 = str(placa1)

        if placa2 >= "aaa" and placa2 <= "bez":
            return 0
        elif placa2 >= "gkj" and placa2 <= "hok":
            return 1
        elif placa2 >= "iaq" and placa2 <="jdo":
            return 2
        elif placa2 >= "jks" and placa2 <= "jsz":
            return 3
    
    def remover(self, placa):
        placa = self.formatar(placa)
        indice = self.funcao_hash(placa)
        
        try:
          ind_placa = self.vetor[indice].index(placa)
          self.vetor[indice].pop(ind_placa)
        except ValueError:
          pass
        
carro = Veiculo()
carro.inserir("Audi", "A4", "Augusto", "JKY9001")
carro.inserir("Mercedez", "C200", "Augusto", "JSY9001")
print("deu certo")
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