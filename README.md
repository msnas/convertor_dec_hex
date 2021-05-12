# CONVERTER DECIMAL PARA BINÁRIO

Este é bastante simples, simplesmente fazer uma tabela como o abaixo:
```
0 | 0 | 0 | 0 | 0
0 | 0 | 0 | 1 | 1
0 | 0 | 1 | 0 | 2
0 | 0 | 1 | 1 | 3
0 | 1 | 0 | 0 | 4
0 | 1 | 0 | 1 | 5
0 | 1 | 1 | 0 | 6
0 | 1 | 1 | 1 | 7
1 | 0 | 0 | 0 | 8
1 | 0 | 0 | 1 | 9
1 | 0 | 1 | 0 | 10
1 | 0 | 1 | 1 | 11
1 | 1 | 0 | 0 | 12
1 | 1 | 0 | 1 | 13
1 | 1 | 1 | 0 | 14
1 | 1 | 1 | 1 | 15
```
	
A primeira coluna terá que ter sempre 8 números iguais repetidos, ou seja 8 zeros ou 8 uns
A segunda coluna terá sempre 4 números iguais, 4 zeros ou 4 uns
A terceira coluna terá sempre 2 números iguais, 2 zeros ou 2 uns
A quarta coluna será sempre alteranadamente, nunca podendo existir 2 números iguais, começando sempre pelo 0

Ex: (00 -> ERRADO | 001101-> ERRADO | 10110 -> ERRADO | 10101 -> ERRADO | 01010101 -> CORRETO)



# CONVERTER DECIMAL PARA HEXADECIMAL

- Passo 1: Se o número for inferior a 16, o seu valor é igual ao que está inserido na tabela (ex: 1 equivale a 1, 10 equivale ao A)

- Passo 2: Se o número for superior a 16, é dividido por 16:
		Ex: 501/16 (porque o 16 é o hexadecimal)
		
- Passo 3: Guardar todo o número a partir do ponto decimal:
		Ex: 501/16 = 31.3125 (neste caso: 0.3125)

- Passo 4: Multiplicar o último valor por 16:
		Ex: 0.3125 * 16 = 5 (neste caso o 5 representa na tabela o valor "5", mas se o valor fosse igual ou superior a 16, teria que ser feito a conta de novo)
		
- Passo 5: Dividir a parte antes do ponto decimal por 16 e guardar o número depois do ponto:
		(Visto que 31 é superior a 16, temos que repetir o passo 2)
		Ex: 31/16 = 1.9375 (neste caso: 0.9375)

- Passo 6: Repetir o processo todo até que o número decimal seja inferior a 16:
Ex: (Repetir o passo 4 uma vez que já temos o número guardado - 0.9375 -)
			0.9375 * 16 = 15 (15 representa a letra "F" na tabela)
			
			(O 1 representa o número antes do ponto décimal do exemplo do Passo 5)
			1 / 16 = 0.0625
			
			0.0625 * 16 = 1 (este número representa o "1" na tabela)
			
Resultado final: 1F5 (16)

É de baixo para cima, o último valor a ser descoberto representa o 1º número e o primeiro representa o último

