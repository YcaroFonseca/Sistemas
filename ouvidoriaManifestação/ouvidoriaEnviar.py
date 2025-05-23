from ouvidoriaFinal import *

conn = criarConexao('localhost', 'root', 'Roberto1799', 'ouvidoriaoficial')

print()
print("="*15,"\033[34mProjeto Ouvidoria\033[m","="*15)
print()
while True:
    print('=' * 50)
    print('''
        1) Listagem das Manifestações 
        2) Lista por Tipo 
        3) Criar Nova Manifestação 
        4) Exibir Quantidade de Manifestações 
        5) Pesquisar Manifestação por Código 
        6) Atualizar Manifestação
        7) Excluir Manifestação 
        8) Sair do Sistema''')
    print()
    print('=' * 50)
    opcao = int(input('Selecione a opção: '))
    print()

    if opcao == 1:
        listagemManifestacoes(conn)

    elif opcao == 2:
        listagemTipo(conn)

    elif opcao == 3:
        adicionarManifestacao(conn)

    elif opcao == 4:
        quantidadeManifestacoes(conn)

    elif opcao == 5:
        pesquisarManifestacoes(conn)

    elif opcao == 6:
        atualizarInformacoes(conn)

    elif opcao == 7:
        excluirManifestacoes(conn)

    elif opcao == 8:
        encerrar(conn)
        break

    else:
        print('\033[1;31mOpção inválida!\033[m')