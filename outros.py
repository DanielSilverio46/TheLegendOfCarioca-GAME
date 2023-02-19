def vericar_armas():
    dic = {}

    with open('armas.txt', 'r') as file:
        armas = file.read()
        armas = armas.split(',')

    for arma in armas:
        ultima_letra = len(arma)

        chave = arma[:ultima_letra - 2]
        valor = arma[ultima_letra - 1 : ultima_letra]

        dic[chave] = int(valor)
