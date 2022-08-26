teste = "CU CU 814979824719 cu"
print(teste[0:1])
print(teste.lower())

canalha = "JKY9412"
canalha1 = canalha.lower()
canalha2 = str(canalha1[0:3])
print(canalha2)


def test(canalha):
    if canalha> "aaa" and canalha < "bez":
        return 0
    elif canalha > "gkj" and canalha < "hok":
        return 1
    elif canalha > "iaq" and canalha < "jdo":
        return 2
    elif canalha > "jks" and canalha < "jsz":
        return 3

cu = test(canalha2)
print(cu)
