class Veiculo:
    def __init__(self, marca, modelo, proprietario):
        self.marca = marca
        self.modelo = modelo
        self.proprietario = proprietario
        self.vetor = [None] * 4
    def __str__(self):
        return '{} {} {}'.format(self.marca, self.modelo, self.proprietario)
    def __repr__(self):
        return '{} {} {}'.format(self.marca, self.modelo, self.proprietario)
    
    def converter(self):
        lista = [self.marca, self.modelo, self.proprietario, self.placa]
        return lista

    def formatar(self, placa):
        return placa.lower()

    def inserir(self, placa):
        placa = self.formatar(placa)
        indice = self.funcao_hash(placa)

        if self.vetor[indice] == None:
            self.vetor[indice] = [placa]
        else:
            try:
              self.vetor[indice].index(placa)
            except ValueError:
              self.vetor[indice].append(placa)

    def funcao_hash(self, placa):
        placa2 = placa[0:2]
        if placa2 == "aa" or placa2 == "be":
            return 0
        elif placa2 == "gk" or placa2 == "ho":
            return 1
        elif placa2 == "ia" or placa2 == "jd":
            return 2
        elif placa2 == "jk" or placa2 == "js":
            return 3
    
    def remover(self, placa):
        placa = self.formatar(placa)
        indice = self.funcao_hash(placa)
        
        try:
          ind_placa = self.vetor[indice].index(placa)
          self.vetor[indice].pop(ind_placa)
        except ValueError:
          pass
        

veiculo = Veiculo("Audi", "A4", "Augusto")
veiculo.inserir("JKI 7987")
print(veiculo.vetor)
veiculo.remover("JKI 7987")
print(veiculo.vetor)
    

        

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