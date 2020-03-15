questoes = int(input("Quantas questões? "))
respostas = ['a', 'b', 'c', 'd', 'e', '*']

for c in range(questoes):

	resultado = ''
	erro = False 

	print("Questão {}".format(c + 1))
	for alt in range(5):
		valor = int(input("valor lido: "))

		if valor == 0:
			if resultado != '':
				erro = True
			resultado = respostas[alt]

		if erro == True or (alt == 4 and resultado == ''):
			resultado = respostas[5]

	print("Resposta {}".format(resultado))

