def remover_vírgula_beta(string):
	iterador = 0
	string_saida = ''
	while string[iterador] != ',':
		string_saida = string_saida + string[iterador]
		iterador = iterador+1
	return string_saida

def remover_virgula(string):
	string_saida = ''
	for x in range(len(string)):
		if string[x] == ',':
			string_saida = string_saida + '.'
		else:
			string_saida = string_saida + string[x]
	return string_saida







