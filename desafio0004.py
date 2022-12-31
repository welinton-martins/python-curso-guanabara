tipo = input('Digite algo: ')
print('''
    O tipo primitivo do numero digitado e: {}\n
    isascii: {}
    isalpha: {}
    isalnum: {}
    isupper: {}
    isnumeric: {}
    isdecimal: {}
    isdigit: {}
    isprintable: {}
    isidentifier: {}
    isspace: {}
    islower: {}
'''.format(
    type(tipo),
    tipo.isascii(),
    tipo.isalpha(),
    tipo.isalnum(),
    tipo.isupper(),
    tipo.isnumeric(),
    tipo.isdecimal(),
    tipo.isdigit(),
    tipo.isprintable(),
    tipo.isidentifier(),
    tipo.isspace(),
    tipo.islower(),
))