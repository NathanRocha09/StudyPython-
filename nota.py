

qntd_alunos = int(input(""))
qnt = 0
media_geral = 0
while qnt <= qntd_alunos-1:
    MB1 = float(input(""))
    MB2 = float(input(""))
    media_semestral = (MB1 + MB2)  
    media_geral += media_semestral
    if media_semestral > 6:
        print("PARABÉNS VOCÊ ESTÁ APROVADO")
        print(media_semestral)
    else:
        print("NÃO HOUVE PROCESSAMENTO")
    qnt = qnt+1
    if qnt == 1:
        print( qntd_alunos - qnt)

    else:
        print(qnt, qntd_alunos - qnt)
print( media_geral / qntd_alunos)