import pandas as pd

from operacoesbd import *
from tabulate import *
from pandas import *

# ==> ELOGIOS <==
def addelogio(conex):
    try:
        print("==> \033[1;34mADICIONAR-ELOGIOS\033[m <==")
        print()
        elogio = str(input("=> "))
        if not elogio:
            print('\033[31mERRO\033[m: O campo não pode estar vazio!')
            return
        print()
        add_elogio = "INSERT INTO elogio ( manifestacao ) VALUES ( %s )"
        novo_elogio = [ elogio ]
        banco_elogio = insertNoBancoDados(conex, add_elogio, novo_elogio)
        if banco_elogio:
            print("\033[1;32mAdicionado com Sucesso!\033[m")
            print(f"=> O código do seu elogio é (\033[1;34m{banco_elogio}\033[m) <=")
        else:
            print("\033[1;31mNão foi possivel Adicionar!\nTente novamente!\033[m")
        print()
    except Exception as e:
        print(f"\033[1;31mErro ao acessar o banco de dados: {e}\033[m")

def excluirelogio(conex):
    try:
        print("==> \033[1;34mExcluir Elogios\033[m <==")
        print()
        opcao = input("\033[1;34m=>\033[m Qual o código do Elogio: ")
        if not opcao:
            print('\033[31mERRO\033[m: O campo não pode estar vazio!')
            print()
            return
        consulta_list = "select * from elogio where id = %s"
        dados = [opcao]
        lista = listarBancoDados(conex, consulta_list, params=dados)
        if len(lista) != 0:
            print(f"\033[1;34m=>\033[m1 {lista[0][1]}")
        codremocao = "delete from elogio where id = %s"
        manifestacaoexluida = [ opcao ]
        exclusao = excluirBancoDados(conex, codremocao, manifestacaoexluida)
        if exclusao == 0:
            print("\033[1;31mNão existe Elogio com esse código!\033[m")
            print()
        else:
            print("\033[1;32mElogio Excluido com Sucesso!\033[m")
            print()
    except Exception as e:
        print(f"\033[1;31mErro ao acessar o banco de dados: {e}\033[m")

def listarelogio(conex):
    try:
        print("==> \033[1;34mLISTA DE ELOGIOS\033[m <==")
        print()
        consulta_lista = "select * from elogio"
        lista = listarBancoDados(conex, consulta_lista)
        if len(lista) == 0:
            print("\033[1;31mNão existe Elogios!\033[m")
        else:
            print("_" * 5, "CODIGO", "_" * 8, "ELOGIOS", "_" * 10)
            for elogio in range(len(lista)):
                print(f"{elogio + 1:2} \033[1;34m=>\033[m   {lista[elogio][0]:<8} | \033[1;34m-\033[m {lista[elogio][1]:<50}")
#================================================================================================================================
            # USANDO TABULATE
            print(tabulate(lista, headers=["\033[1;34mID\033[m", "\033[1;34mELOGIOS\033[m"], tablefmt="grid"))
#================================================================================================================================
            # USANDO PANDAS
            tabelapanda = pd.DataFrame(lista)
            print(tabelapanda)
#================================================================================================================================
        print()

    except Exception as e:
        print(f"\033[1;31mErro ao acessar o banco de dados: {e}\033[m")

def quantidadeelogio(conex):
    try:
        print("==> \033[1;34mQUANTIDADE\033[m <==")
        print()
        consultaquantidade = "select count(*) from elogio"
        quantidade = listarBancoDados(conex, consultaquantidade)
        if len(quantidade) == 0:
            print("\033[1;31mNão existe Manifestação!\033[m")
        else:
            print(f"\033[1;34m=>\033[m No momento exite ( \033[1;34m{quantidade[0][0]}\033[m ) Elogio no Banco de Dados!")
        print()
    except Exception as e:
        print(f"\033[1;31mErro ao acessar o banco de dados: {e}\033[m")

def pesquisaelogio(conex):
    try:
        print("==> \033[34mPESQUISA\033[m <==")
        print()
        consultacod = input("\033[1;34m=>\033[m Digite o código da sua manifetação: ")
        print()
        if not consultacod:
            print('\033[31mERRO\033[m: O campo não pode estar vazio!')
            print()
            return
        consultaListagem = "select * from elogio where id = %s"
        codigo = [consultacod]
        listaBanco = listarBancoDados(conex, consultaListagem, codigo)
        if len(listaBanco) == 0:
            print(f'\033[31mLista de manifestações vazia!\033[m')
        else:
#================================================================================================================================
            print("_" * 6, "COD", "_" * 8, "MANIFESTAÇÃO", "_" * 10)
            for elogio in range(len(listaBanco)):
                print(f"{elogio + 1:2} \033[1;34m=>\033[m   {listaBanco[elogio][0]:<5} | \033[1;34m-\033[m {listaBanco[elogio][1]:<50}")
#================================================================================================================================
                # USANDO TABULATE
                print(tabulate(listaBanco, headers=["\033[1;34mID\033[m", "\033[1;34mELOGIOS\033[m"], tablefmt="grid"))
#================================================================================================================================

        print()
    except Exception as e:
        print(f"\033[1;31mErro ao acessar o banco de dados: {e}\033[m")

#=====================================
# ==> RECLAMAÇÃO <== OK
def addreclamacao(conex):
    try:
        print("==> \033[1;34mADICIONAR RECLAMAÇÃO\033[m <==")
        print()
        reclamacao = str(input("\033[1;34m=>\033[m "))
        if not reclamacao:
            print('\033[31mERRO\033[m: O campo não pode estar vazio!')
            return
        print()
        add_reclamcao = "INSERT INTO reclamacao ( manifestacao ) VALUES ( %s )"
        novo_reclamcao = [ reclamacao ]
        banco_reclamacao = insertNoBancoDados(conex, add_reclamcao, novo_reclamcao)
        if banco_reclamacao:
            print("\033[1;34m=>\033[m \033[1;32mAdicionado com Sucesso!\033[m")
            print(f"\033[1;34m=>\033[m O código da sua reclamação é (\033[1;34m{banco_reclamacao}\033[m) \033[1;34m<=\033[m")
        else:
            print("\033[1;31mNão foi possivel Adicionar!\nTente novamente!\033[m")
        print()
    except Exception as e:
        print(f"\033[1;31mErro ao acessar o banco de dados: {e}\033[m")

def excluireclamacao(conex):
    try:
        print("==> \033[1;34mExcluir Reclamação\033[m <==")
        print()
        opcao = input("\033[1;34m=>\033[m Qual o código da Reclamação: ")
        if not opcao:
            print('\033[31mERRO\033[m: O campo não pode estar vazio!')
            print()
            return
        consulta_list = "select * from reclamacao where id = %s"
        dados = [opcao]
        lista = listarBancoDados(conex, consulta_list, params=dados)
        if len(lista) != 0:
            print(f"\033[1;34m=>\033[m {lista[0][1]}")
        codremocao = "delete from reclamacao where id = %s"
        manifestacaoexluida = [ opcao ]
        exclusao = excluirBancoDados(conex, codremocao, manifestacaoexluida)
        if exclusao == 0:
            print("\033[1;31mNão existe Reclamação com esse código!\033[m")
            print()
        else:
            print("\033[1;32mReclamação Excluida com Sucesso!\033[m")
            print()
    except Exception as e:
        print(f"\033[1;31mErro ao acessar o banco de dados: {e}\033[m")

def listareclamacao(conex):
    try:
        print("==> \033[1;34mLISTA DE RECLAMAÇÃO\033[m <==")
        print()
        consulta_lista = "select * from reclamacao"
        lista = listarBancoDados(conex, consulta_lista)
        if len(lista) == 0:
            print("\033[1;31mNão existe Reclamção!\033[m")
        else:
#================================================================================================================================
            print("_" * 5, "CODIGO", "_" * 8, "RECLAMAÇÃO", "_" * 10)
            for elogio in range(len(lista)):
                print(f"{elogio + 1:2} \033[1;34m=>\033[m   {lista[elogio][0]:<8} | \033[1;34m-\033[m {lista[elogio][1]:<50}")
#================================================================================================================================
                # USANDO TABULATE
                print(tabulate(lista, headers=["\033[1;34mID\033[m", "\033[1;34mELOGIOS\033[m"], tablefmt="grid"))
#================================================================================================================================

        print()

    except Exception as e:
        print(f"\033[1;31mErro ao acessar o banco de dados: {e}\033[m")

def quantidareclamacao(conex):
    try:
        print("==> \033[1;34mQUANTIDADE\033[m <==")
        print()
        consultaquantidade = "select count(*) from reclamacao"
        quantidade = listarBancoDados(conex, consultaquantidade)
        if len(quantidade) == 0:
            print("\033[1;31mNão existe Reclamação!\033[m")
        else:
            print(f"\033[1;34m=>\033[m No momento exite ( \033[1;34m{quantidade[0][0]}\033[m ) Reclamação no Banco de Dados!")
        print()
    except Exception as e:
        print(f"\033[1;31mErro ao acessar o banco de dados: {e}\033[m")

def pesquisareclamacao(conex):
    try:
        print("==> \033[1;34mPESQUISA\033[m <==")
        print()
        consultacod = input("\033[1;34m=>\033[m Digite o código da sua reclamação: ")
        print()
        if not consultacod:
            print('\033[31mERRO\033[m: O campo não pode estar vazio!')
            print()
            return
        consultaListagem = "select * from reclamacao where id = %s"
        codigo = [consultacod]
        listaBanco = listarBancoDados(conex, consultaListagem, codigo)
        if len(listaBanco) == 0:
            print(f'\033[31mLista de reclamação vazia!\033[m')
        else:
            print("_" * 6, "\033[1;34mCODIGO\033[m", "_" * 8, "\033[1;34mRECLAMAÇÃO\033[m", "_" * 10)
            for elogio in range(len(listaBanco)):
                print(f"{elogio + 1:2} \033[1;34m=>\033[m     {listaBanco[elogio][0]:<6} | \033[1;34m-\033[m {listaBanco[elogio][1]:<50}")
#================================================================================================================================
                # USANDO TABULATE
                print(tabulate(listaBanco, headers=["\033[1;34mID\033[m", "\033[1;34mELOGIOS\033[m"], tablefmt="grid"))
#================================================================================================================================
        print()
    except Exception as e:
        print(f"\033[1;31mErro ao acessar o banco de dados: {e}\033[m")

#==================================
# ==> SEGESTAO <== OK
def addsugestao(conex):
    try:
        print("==> \033[1;34mADICIONAR SUGESTÃO\033[m <==")
        print()
        sugestao = str(input("\033[1;34m=>\033[m "))
        if not sugestao:
            print('\033[31mERRO\033[m: O campo não pode estar vazio!')
            return
        print()
        add_sugestao = "INSERT INTO sugestao ( manifestacao ) VALUES ( %s )"
        nova_sugestao = [ sugestao ]
        banco_sugestao = insertNoBancoDados(conex, add_sugestao, nova_sugestao)
        if banco_sugestao:
            print("\033[1;32mAdicionado com Sucesso!\033[m")
            print(f"\033[1;34m=>\033[m O código da sua sugestão é (\033[1;34m{banco_sugestao}\033[m) \033[1;34m<=\033[m")
        else:
            print("\033[1;31mNão foi possivel Adicionar!\nTente novamente!\033[m")
        print()
    except Exception as e:
        print(f"\033[1;31mErro ao acessar o banco de dados: {e}\033[m")

def excluirsugestao(conex):
    try:
        print("==> \033[1;34mExcluir Sugestão\033[m <==")
        print()
        opcao = input("\033[1;34m=>\033[m Qual o código da Sugestão: ")
        if not opcao:
            print('\033[31mERRO\033[m: O campo não pode estar vazio!')
            print()
            return
        consulta_list = "select * from sugestao where id = %s"
        dados = [opcao]
        lista = listarBancoDados(conex, consulta_list, params=dados)
        if len(lista) != 0:
            print(f"\033[1;34m=>\033[m {lista[0][1]}")
        codremocao = "delete from sugestao where id = %s"
        manifestacaoexluida = [ opcao ]
        exclusao = excluirBancoDados(conex, codremocao, manifestacaoexluida)
        if exclusao == 0:
            print("\033[1;31mNão existe Sugestão com esse código!\033[m")
            print()
        else:
            print("\033[1;32mSugestão Excluida com Sucesso!\033[m")
            print()
    except Exception as e:
        print(f"\033[1;31mErro ao acessar o Banco de Dados: {e}\033[m")

def listarsugestao(conex):
    try:
        print("==> \033[1;34mLISTA DE SUGESTÃO\033[m <==")
        print()
        consulta_lista = "select * from sugestao"
        lista = listarBancoDados(conex, consulta_lista)
        if len(lista) == 0:
            print("\033[1;31mNão existe Sugestão!\033[m")
        else:
#================================================================================================================================
            print("_" * 5, "CODIGO", "_" * 8, "SUGESTÃO", "_" * 10)
            for elogio in range(len(lista)):
                print(f"{elogio + 1:2} \033[1;34m=>\033[m   {lista[elogio][0]:<8} | \033[1;34m-\033[m {lista[elogio][1]:<50}")
#================================================================================================================================
                # USANDO TABULATE
                print(tabulate(lista, headers=["\033[1;34mID\033[m", "\033[1;34mELOGIOS\033[m"], tablefmt="grid"))
#================================================================================================================================

        print()

    except Exception as e:
        print(f"\033[1;31mErro ao acessar o Banco de Dados: {e}\033[m")

def quantidadesugestao(conex):
    try:
        print("==> \033[1;34mQUANTIDADE\033[m <==")
        print()
        consultaquantidade = "select count(*) from sugestao"
        quantidade = listarBancoDados(conex, consultaquantidade)
        if len(quantidade) == 0:
            print("\033[1;31mNão existe Manifestação!\033[m")
        else:
            print(f"\033[1;34m=>\033[m No momento exite \033[1;34m{quantidade[0][0]}\033[m Sugestão no Banco de Dados!")
        print()

    except Exception as e:
        print(f"\033[1;31mErro ao acessar o Banco de Dados: {e}\033[m")

def pesquisasugestao(conex):
    try:
        print("==> \033[1;34mPESQUISA\033[m <==")
        print()
        consultacod = input("\033[1;34m=>\033[m Digite o código da sua Sugestão: ")
        print()
        if not consultacod:
            print('\033[31mERRO\033[m: O campo não pode estar vazio!')
            print()
            return
        consultaListagem = "select * from sugestao where id = %s"
        codigo = [consultacod]
        listaBanco = listarBancoDados(conex, consultaListagem, codigo)
        if len(listaBanco) == 0:
            print(f'\033[31mLista de Sugestão vazia!\033[m')
        else:
#================================================================================================================================
            print("_" * 5, "COD", "_" * 8, "SUGESTÃO", "_" * 10)
            for elogio in range(len(listaBanco)):
                print(f"{elogio + 1:2} \033[1;34m=>\033[m   {listaBanco[elogio][0]:<8} | \033[1;34m-\033[m {listaBanco[elogio][1]:<50}")
#================================================================================================================================
                # USANDO TABULATE
                print(tabulate(listaBanco, headers=["\033[1;34mID\033[m", "\033[1;34mELOGIOS\033[m"], tablefmt="grid"))
#================================================================================================================================

        print()
    except Exception as e:
        print(f"\033[1;31mErro ao acessar o Banco de Dados: {e}\033[m")

# ==> FINALIZAR <== OK
def encerrarConexao(conex):
    print("\033[1;34m=>\033[m Obrigado pelo contato!\n\033[1;34m=>\033[mVolte sempre!")
    print()