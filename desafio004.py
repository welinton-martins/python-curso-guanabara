algo = input('Digite algo: ')
print('''
O numero primitivo desse valor e {}
So tem espacos? {} 
E um numero? {} 
E alfabetico? {} 
E alfanumerico? {} 
Esta um maiusculas? {} 
Esta em minusculas? {}
Esta capitalizada? {}
'''.format(
    type(algo),
    algo.isspace(),
    algo.isnumeric(),
    algo.isalpha(),
    algo.isalnum(),
    algo.isupper(),
    algo.islower(),
    algo.istitle()
))