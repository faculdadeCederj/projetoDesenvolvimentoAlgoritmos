teste = ['cavalo', 'manco', 'cagou', 'calca', 'puta', 'pariu', 'rato', 'rico', 'rei', 'roma']




def tamanho(v):
	return len(v)

def charAt(str, pos):
	return str[pos-1]


def iniciais(lista, k):
	alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l',
	'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

	minimo = k
	resultado = list(range(tamanho(lista)))

	for palavra in range(tamanho(lista)):
		letra = list(range(tamanho(lista)))
		letra[palavra] = lista[palavra][0]

	for qtd in range(tamanho(letra)):
		cont = 0
		for qtdLetras in range(tamanho(letra)):
			if letra[qtd] == letra[qtdLetras]:
				cont += 1
		if cont >= minimo:
			resultado[qtd] = letra[qtd]
	print(resultado)





iniciais(teste, 4)
