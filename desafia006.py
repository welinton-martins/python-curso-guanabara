n = float(input('Digite um numero: '))

print('''
O Dobro: {:.2f},
Triplo: {:.2f} e
a Raiz Quadrada: {:.2f}
'''.format(
    n**2,
    n**3,
    n**(1/2)
))