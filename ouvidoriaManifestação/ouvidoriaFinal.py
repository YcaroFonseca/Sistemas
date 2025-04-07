from operacoesbd import *

#listagem OK
def listagemManifestacoes(conn):
    print("=" * 15, "\033[34mLISTA\033[m", "=" * 15)
    print()
    consultaListagem = 'select * from tabelaOuvidoria'
    listaBanco = listarBancoDados(conn, consultaListagem)
    if len(listaBanco) == 0:
        print(f'\033[31mLista de manifestações vazia!\033[m')
    else:
        print("_" * 20,"\033[1;34mCPF\033[m","_" * 10,"\033[1;34mNOME\033[m","_" * 10,"\033[1;34mTIPO\033[m","_" * 10,"\033[1;34mRECLAMAÇÃO\033[m")
        for item in range(len(listaBanco)):
            print(f'\033[34mManifestação {item + 1:2})\033[m {listaBanco[item][0]:<5} |     {listaBanco[item][1]:<10} |       {listaBanco[item][2]:<6} | {listaBanco[item][3]:<50}')
            print()

#listagemTipo OK
def listagemTipo(conn):
    try:
        print("=" * 15, "\033[34mPESQUISA POR TIPO\033[m", "=" * 15)
        print("[ 1 ] Reclamação [ 2 ] Sugestão [ 3 ] Elogio")
        print()
        tipo = input("Digite o codigo do tipo da manifestação: ")
        if not tipo:
            print("\033[1;31mERRO\033[m: O campo não pode ficar vazio!")
            print()
            return
        if tipo == 1:
            print("=" * 15, "\033[34mRECLAMAÇÃO\033[m", "=" * 15)
        elif tipo == 2:
            print("=" * 15, "\033[34mSUGESTÃO\033[m", "=" * 15)
        elif tipo == 3:
            print("=" * 15, "\033[34mELOGIO\033[m", "=" * 15)
        else:
            print()

    except Exception as e:
        print(f'\033[1;31mERRO\033[m: {e}. Tente novamente!')

    consultalistagem = "select * from tabelaOuvidoria where tipo = %s"
    opcao = [ tipo ]
    listaBanco = listarBancoDados(conn, consultalistagem, opcao)
    if len(listaBanco) == 0:
        print(f'\033[31mLista de manifestações vazia!\033[m')
    else:
        print("_" * 20, "\033[1;34mCPF\033[m", "_" * 10, "\033[1;34mNOME\033[m", "_" * 10, "\033[1;34mTIPO\033[m", "_" * 10, "\033[1;34mRECLAMAÇÃO\033[m")
        for item in range(len(listaBanco)):
            print(f'\033[34mManifestação {item + 1:2})\033[m {listaBanco[item][0]:<5} |     {listaBanco[item][1]:<10} |       {listaBanco[item][2]:<6} | {listaBanco[item][3]:<50}')
            print()

# ADICIONAR OK
def adicionarManifestacao(conn):
    try:
        print("=" * 15, "\033[34mADICIONAR\033[m", "=" * 15)
        cpf = input('Digite seu CPF: ').strip()
        nome = input('Digite seu nome: ').strip()
        print("[ 1 ] Reclamação [ 2 ] Sugestão [ 3 ] Elogio")
        tipo = input("Qual é o tipo da manifestação: ")
#=============================================================
        if "0" < tipo < "4":
            print(f'\033[1;31mERRO\033[m: Tente novamente!')
            return
#=============================================================
        reclamacao = input('Digite sua reclamação: ').strip()
        if not cpf or not nome or not tipo or not reclamacao:
            print('\033[1;31mERRO\033[m: O campo não pode ficar vazio!')
            return
        consultaReclamacao = 'INSERT INTO tabelaOuvidoria (cpf, nome, tipo, reclamacao) VALUES (%s, %s, %s, %s)'
        dados = [cpf, nome, tipo, reclamacao]
        inserirBanco = insertNoBancoDados(conn, consultaReclamacao, dados)
        if not inserirBanco:
            print('\033[1;31mERRO\033[m: Verifique se seu CPF já está cadastrado!')
        else:
            print(f'Perfeito, {nome.capitalize()}! Sua reclamação foi registrada com sucesso.')
    except Exception as e:
        print(f'\033[1;31mERRO\033[m: {e}. Tente novamente!')

#Atualizar OK
def atualizarInformacoes(conn):
    try:
        print("=" * 15, "\033[34mATUALIZAR\033[m", "=" * 15)
        qualCpf = input('\033[1;34m=>\033[m Digite o cpf que a manifestação está relacionada: (Se preferir, pode digitar APENAS os dois últimos dígitos do cpf) ')
        manifestacao = input('\033[1;34m=>\033[m Digite a nova manifestação: ')
        print()
        if not qualCpf or not manifestacao:
            print('\033[1;31mERRO\033[m: O campo não pode ficar vazio!!')
            return

        consultaAtualizar = 'update tabelaOuvidoria set reclamacao = %s where cpf like %s'
        dados = [ manifestacao, '%' + qualCpf]
        atualizarBanco = atualizarBancoDados(conn, consultaAtualizar, dados)

        if not atualizarBanco:
            print('\033[1;31mCpf inválido!\033[m')
        else:
            print('\033[1;32mAtualização feita com sucesso!\033[m')

    except Exception as e:
        print(f'\033[1;31mERRO\033[m: {e}. Tente novamente!')

# QUANTIDADE OK
def quantidadeManifestacoes(conn):
    try:
        print("=" * 15, "\033[34mQUANTIDADE\033[m", "=" * 15)
        print()
        consultaQuantidade = 'select reclamacao from tabelaOuvidoria'
        listarQuantidadeDeReclamacoes = listarBancoDados(conn, consultaQuantidade)

        if len(listarQuantidadeDeReclamacoes) == 0:
            print(f'\033[31mLista de manifestações vazia!\033[m')
        else:
            print(f'\033[1;34m=>\033[m Total de \033[1;34m{len(listarQuantidadeDeReclamacoes)}\033[m manifestações.')
            print()

    except Exception as e:
        print(f"\033[1;31mERRO\033[m: {e}. Tente novamente!")

# PESQUISAR OK
def pesquisarManifestacoes(conn):
    try:
        print("=" * 15, "\033[34mPESQUISA\033[m", "=" * 15)
        qualCpf = input('Digite o CPF para exibir a reclamação realizada: (Se preferir, pode digitar APENAS os dois últimos dígitos do cpf) ').strip()
        print()

        # Verifica se o CPF foi preenchido antes de buscar no banco
        if not qualCpf:
            print('\033[1;31mERRO\033[m: O CPF não pode estar vazio. Por favor, insira um CPF válido!')
            return

        consultaPesquisar = 'SELECT reclamacao FROM tabelaOuvidoria WHERE cpf like %s'
        dados = ['%' + qualCpf]

        reclamacaoDesejada = listarBancoDados(conn, consultaPesquisar, dados)

        # Verifica se o CPF existe no banco antes de exibir a reclamação
        if not reclamacaoDesejada:
            print(f'\033[31mErro: Nenhuma manifestação encontrada para o CPF informado.\033[m')
        else:
            print(f'A reclamação referente a esse CPF é: "{reclamacaoDesejada[0][0]}"')

    except ValueError:
        print(f'\033[1;31mERRO\033[m: {e}. Tente novamente!')

#Excluir OK
def excluirManifestacoes(conn):
    try:
        print("=" * 15, "\033[34mEXCLUIR\033[m", "=" * 15)
        cpf = input('Digite o cpf para remover a manifestação: (Se preferir, pode digitar APENAS os dois últimos dígitos do cpf) ')
        consultaExcluir = 'delete from tabelaOuvidoria where cpf like %s'
        dados = ['%' + cpf]
        if not cpf:
            print('\033[31mERRO\033[m: O campo não pode ficar vazio!')
            return

        excluindoManifestacoes = excluirBancoDados(conn, consultaExcluir, dados)

        if excluindoManifestacoes == 0:
            print('\033[1;31mERRO\033[m: Nenhuma manifestação removida!')
        else:
            print(f'\033[1;34=>\033[m Manifestação com CPF ( \033[1;34m{cpf}\033[m ) excluída com sucesso!')
            print()
    except Exception as e:
        print(f'\033[1;31mERRO\033[m: {e}. Tente novamente!')

#Finalizar OK
def encerrar(conn):
    encerrarConexao(conn)
    print('\033[1;34m=>\033[m Obrigado pelo contato!\n\033[1;34m=>\033[mVolte Sempre!')