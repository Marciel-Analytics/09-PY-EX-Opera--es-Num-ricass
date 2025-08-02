n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
    [1] SOMAR 
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS 
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('Qual a sua opção: '))
    if opcao == 1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))
    elif opcao == 2:
        print('{} x {} = {}'.format(n1,n2,n1*n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o maior valor é {}'.format(n1,n2,maior))

    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Finalizando...')

    else:
        print('Opção inválida tente de novo')
    print('=-='*10)
print('Fim do programa, volte sempre!')