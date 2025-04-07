from metodo_rd import *
conex = criarConexao("localhost", "root", "Roberto1799", "suporteouvidoria")

# Projeto - Ouvidoria
print("===============> \033[1;34mBEM VINDO A OUVIDORIA RD REPRESENTAÇÕES\033[m <====================")
while True:
    print()
    print("=" * 80)
    print(" " * 30," \033[1;34mMenu Principal\033[m "," " * 30)
    print("       [ 1 ] Elogios [ 2 ] Reclamações [ 3 ] Sugestões [ 4 ] Finalizar")
    print("=" * 80)
    print()
    opcao = int(input("\033[1;34m=>\033[m Qual opção deseja: "))
    print()

# ELOGIO ok
    if opcao == 1:
        while True:
            print("=" * 35, " \033[1;34mELOGIOS\033[m ", "=" * 35)
            print("[ 1 ] Visualizar [ 2 ] Adicionar [ 3 ] Quantidade [ 4 ] Pesquisar [ 5 ] Excluir  [ 6 ] Sair")
            print()
            elogio = int(input("Qual opção deseja: "))
            print()
            # VISUALIZAR OK
            if elogio == 1:
                listarelogio(conex)
            # ADICIONAR OK
            elif elogio == 2:
                addelogio(conex)
            # QUANTIDADE OK
            elif elogio == 3:
                quantidadeelogio(conex)
            # PESQUISAR
            elif elogio == 4:
                pesquisaelogio(conex)
            # EXCLUIR OK
            elif elogio == 5:
                excluirelogio(conex)
            #SAIR ok
            elif elogio == 6:
                print(" \033[1;32mOperação Finalizada!\033[m")
                print()
                break
            #INVALIDO
            else:
                print("\033[1;31m=> Opção Invalida! <=\033[m")
                print()

# RECLAMAÇÕES
    elif opcao == 2:
        while True:
            print("=" * 35, " \033[1;34mRECLAMAÇÕES\033[m", "=" * 35)
            print("[ 1 ] Visualizar [ 2 ] Adicionar [ 3 ] Quantidade [ 4 ] Pesquisar [ 5 ] Excluir  [ 6 ] Sair")
            print()
            reclamacao = int(input("\033[1;34m=>\033[m Qual opção deseja: "))
            print()
            #LISTA
            if reclamacao == 1:
                listareclamacao(conex)
            #ADD
            elif reclamacao == 2:
                addreclamacao(conex)
            #QUANTIDADE
            elif reclamacao == 3:
                quantidareclamacao(conex)
            #PESQUISAR
            elif reclamacao == 4:
                pesquisareclamacao(conex)
            #EXCLUIR
            elif reclamacao == 5:
                excluireclamacao(conex)
            #SAIR
            elif reclamacao == 6:
                print("\033[1;32mOperação Finalizada!\033[m")
                break

            else:
                print("\033[1;31m=> Opção Invalida! <=\033[m")
                print()

# SUGESTÕES
    elif opcao == 3:
        while True:
            print("=" * 35, " \033[1;34mSUGESTÕES\033[m ", "=" * 35)
            print("[ 1 ] Visualizar [ 2 ] Adicionar [ 3 ] Quantidade [ 4 ] Pesquisar [ 5 ] Excluir  [ 6 ] Sair")
            print()
            sugestao = int(input("\033[1;34m=>\033[m Qual opção deseja: "))
            print()
            # VISUALIZAR OK
            if sugestao == 1:
                listarsugestao(conex)
            # ADICIONAR OK
            elif sugestao == 2:
                addsugestao(conex)
            #QUANTIDADE OK
            elif sugestao == 3:
                quantidadesugestao(conex)
            # PESQUISA OK
            elif sugestao == 4:
                pesquisasugestao(conex)
            # EXCLUIR OK
            elif sugestao == 5:
                excluirsugestao(conex)
            # SAIR
            elif sugestao == 6:
                print("Operação Finalizada!")
                break
            # INVALIDO
            else:
                print("\033[1;31m=> Opção Invalida! <=\033[m")
                print()

# SAIR
    elif opcao == 4:
        encerrarConexao(conex)
        break

#INVALIDO
    else:
        print("\033[1;31m=> Opção Invalida! <=\033[m")
