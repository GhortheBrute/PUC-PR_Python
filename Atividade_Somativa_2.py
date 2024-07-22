import json


def menu_principal():
    """
    Exibe o Menu Principal da aplicação.
    Não possui parâmetros
    Sem retorno
    """
    while True:  # Função While para o funcionamento do Menu-Principal
        print("----- MENU PRINCIPAL -----")
        print("\n(1) Gerenciar estudantes.")
        print("(2) Gerenciar professores.")
        print("(3) Gerenciar disciplinas.")
        print("(4) Gerenciar turmas.")
        print("(5) Gerenciar matrículas.")
        print("(9) Sair.")
        try:  # Função Try-Catch para input diferente de INT
            option = int(
                input("\nInforme a opção desejada: "))  # Armazena a escolha na var option para Match-Case e IFs
        except ValueError:  # Captura exceção de valores diferentes de INT
            print("Valor inválido! Por favor digite um valor entre 1-9.")
            continue  # Inicia uma próxima iteração, ignorando as linhas abaixo
        match option:  # Match-Case para escolha da opção
            case 1:  # Altera a variável choice que fixa a repetição do Menu-Secundário.
                choice = "Estudantes"
                menu_operacoes(choice, option, 'Alunos.json')
                break
            case 2:  # Conforme Tarefa. Qualquer opção fora "ESTUDANTES" deverá retornar "EM DESENVOLVIMENTO"
                choice = "PROFESSORES"
                menu_operacoes(choice, option, 'Professores.json')
                break
            case 3:
                choice = "DISCIPLINAS"
                menu_operacoes(choice, option, 'Disciplinas.json')
                break
            case 4:
                choice = "TURMAS"
                menu_operacoes(choice, option, 'Turmas.json')
                break
            case 5:
                choice = "MATRÍCULAS"
                menu_operacoes(choice, option, 'Matriculas.json')
                break
            case 9:  # Opção de encerrar o programa.
                print("====== Sistema finalizado ======")
                break  # Finaliza o While do Menu-Principal.

            case _:  # Opção default para o caso de um valor diferente das opções.
                print("\nOpção inválida!")
                continue


def menu_operacoes(choice, option, arquivo):
    """
    Exibe o Menu de Operações da aplicação
    :param arquivo: O arquivo que será escrito/lido.
    :param choice: Nome da escolha realizada para participar da repetição do cabeçalho no Menu Principal.
    :param option: Valor escolhido para representar Aluno/Professor/Disciplina/Turma/Matrícula.
    :return: Não há retorno
    """
    while True:  # While para o Menu-Secundário
        print(f"\n***** [{choice}] MENU DE OPERAÇÕES *****")  # Utiliza da variável choice para o título do menu.
        print("\n(1) Incluir.")
        print("(2) Listar.")
        print("(3) Atualizar.")
        print("(4) Excluir.")
        print("(9) Voltar ao menu principal.")
        try:  # Try-Catch para capturar valores diferentes de INT
            action = int(input("\nInforme a ação desejada: "))  # Armazena a ação na variável action
        except ValueError:  # Captura de exceções de valores diferentes de INT
            print("Valor inválido! Por favor digite um valor entre 1-9.")
            continue  # Inicia uma próxima iteração do Menu-Secundário, ignorando as linhas abaixo.
        match action:  # Match-Case da ações
            case 1:
                menu_inclusao(option, arquivo)
            case 2:
                menu_listagem(choice, arquivo)
            case 3:  # Conforme a tarefa. Opções ATUALIZAÇÃO e EXCLUSÃO deve exibir apenas "EM DESENVOLVIMENTO"
                menu_atualizacao(option, arquivo)
            case 4:
                menu_exclusao(option, arquivo)
            case 9:  # Finaliza o Menu-Secundário e retorna ao Menu-Principal
                menu_principal()
                break
            case _:  # Opção default de Match-Case para a escolha de uma ação diferente.
                print("\nOpção inválida!")
                continue


def menu_inclusao(option, nome_arquivo):
    """
    Exibe o Menu de Inclusão da aplicação
    :param nome_arquivo: Nome do arquivo a ser lido/escrito
    :param option: Valor escolhido para representar Aluno/Professor/Disciplina/Turma/Matrícula.
    :return: None
    """
    print("\n===== INCLUSÃO =====\n")
    lista = ler_dados(nome_arquivo)
    if option == 1:  # Checa se veio da opção de ESTUDANTES, verificando o option
        name = input("Informe o nome do(a) estudante: ")  # Pergunta o nome do aluno
        while True:
            try:
                cpf = int(input('Informe o CPF do estudante: '))  # Pergunta o CPF o aluno
                if type(cpf) is int:  # Valida se é do tipo INT para sair do loop
                    break
            except ValueError:
                print("Valor inválido! Por favor digite um valor entre 1-9.")
                continue  # Inicia uma próxima iteração do Menu-Secundário, ignorando as linhas abaixo.
        lista_add = {'Codigo': pegar_ultimo_id(nome_arquivo), 'Nome': name, 'CPF': cpf}  # Adiciona os dados a um
        # dicionário
    if option == 2:
        name = input("Informe o nome do(a) professor(a): ")
        while True:
            try:
                cpf = int(input('Informe o CPF do estudante: '))  # Pergunta o CPF o aluno
                if type(cpf) is int:  # Valida se é do tipo INT para sair do loop
                    break
            except ValueError:
                print("Valor inválido! Por favor digite um valor entre 1-9.")
                continue  # Inicia uma próxima iteração, ignorando as linhas abaixo.
        lista_add = {'Codigo': pegar_ultimo_id(nome_arquivo), 'Nome': name, 'CPF': cpf}  # Adiciona os dados a um
        # dicionário
    if option == 3:
        name = input('Informe o nome da disciplina: ')
        lista_add = {'Codigo': pegar_ultimo_id(nome_arquivo), 'Nome': name}  # Adiciona os dados a um dicionário
    if option == 4:
        while True:
            try:
                cod_prof = int(input('Informe o Código do(a) Professor(a): '))
            except ValueError:
                print('Valor inválido! Por favor digite um valor entre 1-99.')
                continue
            if pesquisar(cod_prof, 'Professores.json'):
                break
            else:
                print('Professor não cadastrado. Informe um Codigo válido.')
                continue
        while True:
            try:
                cod_disc = int(input('Informe o Codigo da disciplina: '))
            except ValueError:
                print('Valor inválido! Por favor digite um valor entre 1-99.')
                continue
            if pesquisar(cod_disc, 'Disciplinas.json'):
                break
            else:
                print('Professor não cadastrado. Informe um Codigo válido.')
                continue
        lista_add = {'Codigo': pegar_ultimo_id(nome_arquivo), 'Professor': cod_prof, 'Disciplina': cod_disc}
    if option == 5:
        while True:
            try:
                cod_turma = int(input('Informe o Codigo da Turma: '))
            except ValueError:
                print('Valor inválido! Por favor digite um valor entre 1-99.')
                continue
            if pesquisar(cod_turma, 'Turmas.json'):
                break
            else:
                print('Turma não cadastrada. Informe um Codigo válido.')
                continue
        while True:
            try:
                cod_aluno = int(input('Informe o Codigo do(a) aluno(a): '))
            except ValueError:
                print('Valor inválido! Por favor digite um valor entre 1-99.')
                continue
            if pesquisar(cod_aluno, 'Alunos.json'):
                break
            else:
                print('Professor não cadastrado. Informe um Codigo válido.')
                continue
        lista_add = {'Turma': cod_turma, 'Aluno': cod_aluno}
    lista.append(lista_add)  # Adiciona o dicionário  à lista
    gravar_dados(lista, nome_arquivo)
    input("Pressione ENTER para continuar.")  # Aguarda uma tecla, para facilitar a leitura


def menu_listagem(choice, arquivo):
    """
    Exibe o Menu de Listagem da aplicação.
    :param choice: Coloca uma parte do texto como variável.
    :param arquivo: O arquivo que será escrito/lido.
    :return: None
    """
    print("\n===== LISTAGEM =====\n")
    lista = ler_dados(arquivo)
    if lista:  # Verifica se a lista não está fazia
        for registro in lista:  # Estrutura de repetição para impressão da lista de nomes.
            print(registro)
    else:  # Se a lista for vazia, imprime uma mensagem
        print(f"Não há {choice} cadastrados(as).")
    input("Pressione ENTER para continuar.")


def menu_exclusao(option, arquivo):
    """
    Exibe o Menu de Exclusão da aplicação.
    :param arquivo: O arquivo que será escrito/lido.
    :param option: Valor escolhido para representar Aluno/Professor/Disciplina/Turma/Matrícula.
    :return: None
    """
    print("\n===== EXCLUSÃO =====")
    lista = ler_dados(arquivo)
    if option == 1:
        exc = int(input('Informe o Codigo do aluno a ser excluído: '))
        for i in range(len(lista)):
            if lista[i]['Codigo'] == exc:
                del lista[i]
                break
    gravar_dados(lista, arquivo)
    input("Pressione ENTER para continuar.")


def menu_atualizacao(option, arquivo):
    """
    Exibe o Menu de Atualização da aplicação.
    :param arquivo: O arquivo que será escrito/lido.
    :param option: Valor escolhido para representar Aluno/Professor/Disciplina/Turma/Matrícula.
    :return: None
    """
    print("\n===== ATUALIZAÇÃO =====")
    lista = ler_dados(arquivo)
    if option == 1:
        proc = int(input('Informe o Codigo do aluno a ser atualizado: '))
        escolha = int(input('Informe qual campo deseja atualizar: 1 - Nome; 2 - CPF  '))
        for i in range(len(lista)):
            if lista[i]['Codigo'] == proc:
                if escolha == 1:
                    lista[i]['Nome'] = input('Informe o novo nome: ')
                elif escolha == 2:
                    lista[i]['CPF'] = int(input('Informe o novo CPF: '))
                break
    gravar_dados(lista, arquivo)
    input("Pressione ENTER para continuar.")


def gravar_dados(lista, nome_arquivo):
    """
    Efetua a gravação de dados em um arquivo JSON especificado.
    :param lista: A lista de dados a ser gravada.
    :param nome_arquivo: O nome do arquivo a ser criado e/ou escrito.
    :return: None
    """
    with open(nome_arquivo, 'w', encoding='utf-8',) as arquivo:
        json.dump(lista, arquivo)


def ler_dados(nome_arquivo):
    """
    Efetua a leitura de dados de um arquivo JSON e o retorna em uma lista.
    :param nome_arquivo: Nome do arquivo a ser lido.
    :return: A lista registrada no arquivo JSON ou uma lista vazia, em caso de erro.
    """
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            lista = json.load(arquivo)
        return lista
    except:
        return []


def pegar_ultimo_id(nome_arquivo):
    """
    Obtém o último Codigo utilizado no arquivo, a fim de incrementar
    :param nome_arquivo: Nome do arquivo a ser lido.
    :return: Valor do próximo Id disponível.
    """
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as file:
            listagem = json.load(file)
            contagem = [entry['Codigo'] for entry in listagem]
            ultimo_id = max(contagem)
    except:
        ultimo_id = 0

    return ultimo_id + 1


def pesquisar(cod, arquivo):
    """
    Pesquisa um Id específico num arquivo JSON.
    :param cod: Id procurado
    :param arquivo: Arquivo JSON onde procurar
    :return: True or False
    """
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            listagem = json.load(file)
            if cod in listagem:
                return True
            else:
                return False
    except:
        return False


menu_principal()
