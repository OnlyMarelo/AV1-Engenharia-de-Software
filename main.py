
def menu_principal():
    print('\n=== Calculadora de Finanças ===')
    print('''Selecione uma opção para começarmos:
1: Adicionar Entrada
2: Adicionar Saída
3: Ver o Extrato
4: Excluir uma Entrada/Saida
5: Limpar todo o Extrato
6: Ver Média dos Lançamentos
7: Sair do Programa''')
def main():

    Entradas = []
    Saidas = []

    while True:
        menu_principal()
        opcao = str(input('\nEscolha uma opção (1 a 7): '))

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
            del_lancamento = str(input('Gostaria de Excluir uma entrada (1) ou uma saida (2)?').strip())
            if del_lancamento == '1':
                if not Entradas:
                    print('⚠️ Nenhuma Entrada cadastrada para excluir.')
                else:
                    print('\n--- SUAS ENTRADAS ---')
                    for i, valor in enumerate(Entradas, 1):
                        print(f'{i}: R$ {valor:.2f}')   
                    try:
                        del_entrada = int(input('Qual o número da Entrada que deseja deletar? '))
                        removido = Entradas.pop(del_entrada - 1)
                        print(f'✅ Entrada de R$ {removido:.2f} deletada com sucesso!')
                    except (ValueError, IndexError):
                        print('⚠️ Número de entrada inválido!')
            elif del_lancamento == '2':
                if not Saidas:
                    print('⚠️ Nenhuma Saída cadastrada para excluir.')
                else:
                    print('\n--- SUAS SAÍDAS ---')
                    for i, valor in enumerate(Saidas, 1):
                        print(f'{i}: R$ {valor:.2f}')
                    try:
                        del_saida = int(input('Qual o número da Saída que deseja deletar? '))
                        removido = Saidas.pop(del_saida - 1)
                        print(f'✅ Saída de R$ {removido:.2f} deletada com sucesso!')
                    except (ValueError, IndexError):
                        print('⚠️ Número de saída inválido!')
            else:
                print('Nenhuma opção valida selecionada!')

        elif opcao == '5':
            Entradas.clear()
            Saidas.clear()
            print('✅ Pronto, seu Extrato foi zerado!')

        elif opcao == '6':
            ver_media = str(input('Você gostaria de ver a média de Entradas (1) ou Saídas (2)? ').strip())
            
            if ver_media == '1':
                if Entradas:  # Verifica se a lista NÃO está vazia
                    soma_entradas = sum(Entradas)
                    med_Entradas = soma_entradas / len(Entradas)
                    print(f'Aqui está a soma total: R$ {soma_entradas:.2f} e a média: R$ {med_Entradas:.2f}')
                else:
                    print('⚠️ Sua lista de Entradas ainda está vazia!')
                    
            elif ver_media == '2':
                if Saidas:  # Verifica se a lista NÃO está vazia
                    soma_saidas = sum(Saidas)
                    med_Saidas = soma_saidas / len(Saidas)
                    print(f'Aqui está a soma total: R$ {soma_saidas:.2f} e a média: R$ {med_Saidas:.2f}')
                else:
                    print('⚠️ Sua lista de Saídas ainda está vazia!')
                    
            else:
                print('⚠️ Opção inválida! Escolha 1 ou 2.')



        elif opcao == '7':
            print('Okay, volte sempre!')
            break

        else:
            print('⚠️ Opção Invalida! Escolha um numero de 1 a 7')

if __name__ == '__main__':
    main()
