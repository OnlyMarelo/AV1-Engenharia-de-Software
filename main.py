
def menu_principal():
    print('\n=== Calculadora de Finanças ===')
    print('''Selecione uma opção para começarmos:
1: Adicionar Entrada
2: Adicionar Saída
3: Ver o Extrato
4: Sair do Programa''')
def main():
    Entradas = []
    Saidas = []
    while True:
        menu_principal()
        opcao = str(input('\nEscolha uma opção (1 a 4): '))

        if opcao == '1':
            try:
                Entrada = float(input('Adicione o valor da Entrada: $').strip())
                Entradas.append(Entrada)
                print('✅ Entrada adicionada com sucesso!') 
            except ValueError:       
                print('⚠️Adicione um valor valido!')

        elif opcao == '2':
            try:
                Saida = float(input('Adicione o valor da Saida: $').strip())
                Saidas.append(Saida)
                print('✅ Saida adicionada com sucesso!')
            except ValueError:
                print('Adicione um valor valido!')

        elif opcao == '3':
            print('\n--- EXTRATO ---')
            print('Aqui estão suas Entradas:\n', Entradas)
            print('Aqui estão suas Saidas: \n', Saidas)
            total_entradas = sum(Entradas)
            total_saidas = sum(Saidas)
            saldo = total_entradas - total_saidas
            print(f'Saldo Atual: R$ {saldo:.2f}')

        elif opcao == '4':
            print('Okay, volte sempre!')
            break

        else:
            print('⚠️ Opção Invalida! Escolha um numero de 1 a 4')

if __name__ == '__main__':
    main()
