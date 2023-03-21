perguntas = [
    {
        'pergunta': 'em que ano foi criado a primeira linguaguem de programação?',
        'opções': ['1843','1853','1888','1890'],
        'Respostas': '1843',
    },
    {
        'pergunta': 'quem foi o criador da primeira linguagem de programação?',
        'opções': [' Roberto Ierusalimschy','Guido van Rossum','Dennis Ritchie','Ada Lovelace'],
        'Respostas': 'Ada Lovelace',
    },
]

qtd_acertos = 0 
 
for pergunta in perguntas:
    print('pergunta:', pergunta['pergunta'])
    print()

    opcoes = pergunta['opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})',opcao)
    print()    

    escolha = input('escolha uma opção: ')

    acertou = False
    escolha_int = None
    qntd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qntd_opcoes:
           if opcoes[escolha_int] == pergunta['Respostas']: 
               acertou = True 

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou!')
    else:
        print('Errou') 

    print()


    print('Vocẽ acertou', qtd_acertos)
    print('de',  len(perguntas), 'perguntas')


