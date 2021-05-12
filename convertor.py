# @Mário - 22/09/2020

# Convertor Decimal para Binário
# Convertor Decimal para Hexadecimal (Exemplos: 128, 399)
# ------------------------------------------

# Imports 
import math
###


# Tabela hexadecimal
hex_table = { 
	0: "0",	8: "8",
	1: "1",	9: "9",
	2: "2",	10: "A",
	3: "3",	11: "B",
	4: "4",	12: "C",
	5: "5",	13: "D",
	6: "6",	14: "E",
	7: "7",	15: "F",
}

DEBUG_ = True	 # True = Mostrar os passos todos | False = Mostrar somente o final
HEXADECIMAL_NUMBER = 16 # Representa hexadecimal

def convertor_dec_to_bin(decimal):
	if decimal > 1: # Se o número for maior que 1, uma vez que não vamos fazer a divisão (em termos float) de 1
		"""
			É divido por 2 porque relembrando: 
			# 2 - Binário
			# 10 - Decimal
			# 16 - Hexadecimal
			
			E nós queremos passar de decimal (10) para binário (2)
		"""
		
		# funciona como um loop até que o número seja inferior a 1
		convertor_dec_to_bin(decimal // 2) # Utilizaremos // de forma a não aparecer números décimais
	"""
		O símbolo % representa o resto da divisão que se encontra por fora, ou seja:
		Ex: 7 % 2 = 1, isto porque o 2 nunca chega ao 7 (fica 6 porque é 2 + 2 + 2), a diferença entre os dois (6 e 7) é 1
		Ex: 13 % 5 = 3, porque 5 + 5 é 10, a diferença entre 13 e 10 é 3
		
		A conta nunca pode ser maior do que o 1º valor (por exemplo, não podiamos fazer 5 + 5 + 5 que daria 15 porque passaria dos 13)
		
		Outro exemplo:
		20 % 5 = 0, porque 5 + 5 + 5 + 5 dá 20, ou seja, ele iguala ao número
		
		32 % 6 = 2, porque 6 + 6 + 6 + 6 + 6 dá 30, 30 para 32 dá 2
		
		Isto faz com que o resto da divisão (que será sempre 0 ou 1) seja mostrado
	"""
	print(decimal % 2, end = '') 

# Função da conversão decimal para hexadecimal
def convertor_dec_to_hex(decimal): 
	print("Valor Decimal: {}".format(decimal))
	if decimal >= HEXADECIMAL_NUMBER: # Passo 2
		division, number = math.modf(decimal / HEXADECIMAL_NUMBER)
		multiply = division * HEXADECIMAL_NUMBER
		dec, real = math.modf(number / HEXADECIMAL_NUMBER)
		dec = dec * HEXADECIMAL_NUMBER

		while (int(real) >= HEXADECIMAL_NUMBER):
			real = real / HEXADECIMAL_NUMBER
		else:
			if DEBUG_:
				print_output = [division, hex_table[multiply], hex_table[dec], hex_table[real]]
				for i in range(len(print_output)):
					print("<Debug> Passo {}: {}".format(i + 3, print_output[i]))

		print("Valor Hexadecimal: {}{}{}".format(hex_table[real], hex_table[dec], hex_table[multiply]))
	else: # Passo 1
		print("Valor Hexadecimal: {}".format(hex_table[decimal])) 

# Código principal
if __name__ == '__main__':
	print("Insire o número de acordo com a opção que quer utilizar.\n")
	print("1: Conversão Décimal para Binário\n")
	print("2: Conversão Décimal para Hexadecimal")
	
	f_input = None
	while f_input is None:
		try:
			f_input = int(input("Insire a opção: "))
		except ValueError:
			print("Por favor, insire um número e não um caracter.")
	else:
		if f_input == 1:
			print("----------------------------------------------")
			print("Escolheu: Conversão Décimal para Binário\n")
			t_input = None
			while t_input is None:
				try:
					t_input = int(input("Insire o número que pretende converter: "))
				except ValueError:
					print("Por favor, insire um número e não um caracter.")
			else:
				convertor_dec_to_bin(t_input)
		elif f_input == 2:
			print("----------------------------------------------")
			print("Escolheu: Conversão Décimal para Hexadecimal\n")
			t_input = None
			while t_input is None:
				try:
					t_input = int(input("Insire o número que pretende converter: "))
				except ValueError:
					print("Por favor, insire um número e não um caracter.")
			else:
				convertor_dec_to_hex(t_input)
		else:
			print("O número que está a tentar adicionar não existe!")
