nome = input('Qual e seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome)) #quantidade de espacos
print('Prazer em te conhecer {:>20}!'.format(nome)) #alinhar a esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) #alinhar a centralizado
print('Prazer em te conhecer {:<20}!'.format(nome)) #alinhar a direita
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma e {},\n O produto e {},\n e a divisao e {:.3f}'.format(s,m,d), end='>>> ')
print('Divisao inteira {},\n e potencia {}'.format(di,e))
