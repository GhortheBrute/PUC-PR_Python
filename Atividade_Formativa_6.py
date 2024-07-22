estudantes = []  # Inicia uma lista vazia para o nome dos estudantes
professores = []  # Inicia uma lista vazia para o nome dos professores
disciplinas = []  # Inicia uma lista vazia para o nome das disciplinas
turmas = []  # Inicia uma lista vazia para o nome das turmas
matriculas = []  # Inicia uma lista vazia para o nome das matrículas
code = [0, 0, 0, 0, 0, 0]  # Armazena a ordem de numeração de cada opção


# (Nada/Estudantes/Professores/Disciplinas/Turmas/Matriculas)


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
                choice = "ESTUDANTES"
                menu_operacoes(choice, option)
                break
            case 2:  # Conforme Tarefa. Qualquer opção fora "ESTUDANTES" deverá retornar "EM DESENVOLVIMENTO"
                choice = "PROFESSORES"
                menu_operacoes(choice, option)
                break
            case 3:
                choice = "DISCIPLINAS"
                menu_operacoes(choice, option)
                break
            case 4:
                choice = "TURMAS"
                menu_operacoes(choice, option)
                break
            case 5:
                choice = "MATRÍCULAS"
                menu_operacoes(choice, option)
                break
            case 9:  # Opção de encerrar o programa.
                print("====== Sistema finalizado ======")
                break  # Finaliza o While do Menu-Principal.

            case _:  # Opção default para o caso de um valor diferente das opções.
                print("\nOpção inválida!")
                continue


def menu_operacoes(choice, option):
    """
    Exibe o Menu de Operações da aplicação
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
                menu_inclusao(code, option)
            case 2:
                menu_listagem(option)
            case 3:  # Conforme a tarefa. Opções ATUALIZAÇÃO e EXCLUSÃO deve exibir apenas "EM DESENVOLVIMENTO"
                menu_atualizacao(option)
            case 4:
                menu_exclusao(option)
            case 9:  # Finaliza o Menu-Secundário e retorna ao Menu-Principal
                menu_principal()
                break
            case _:  # Opção default de Match-Case para a escolha de uma ação diferente.
                print("\nOpção inválida!")
                continue


def menu_inclusao(seq, option):
    """
    Exibe o Menu de Inclusão da aplicação
    :param seq: Valor da variável global Code que dá sequencia de código de inclusões.
    :param option: Valor escolhido para representar Aluno/Professor/Disciplina/Turma/Matrícula.
    :return: None
    """
    print("\n===== INCLUSÃO =====\n")
    if option == 1:  # Checa se veio da opção de ESTUDANTES, verificando o option
        name = input("Informe o nome do estudante: ")  # Pergunta o nome do aluno
        while True:
            try:
                cpf = int(input('Informe o CPF do estudante: '))  # Pergunta o CPF o aluno
                if type(cpf) is int:  # Valida se é do tipo INT para sair do loop
                    break
            except ValueError:
                print("Valor inválido! Por favor digite um valor entre 1-9.")
                continue  # Inicia uma próxima iteração do Menu-Secundário, ignorando as linhas abaixo.
        # noinspection PyUnboundLocalVariable
        estudante = {'Código': seq[option] + 1, 'Nome': name, 'CPF': cpf}  # Adiciona os dados a um
        # dicionário
        estudantes.append(estudante)  # Adiciona o dicionário do aluno à lista students
        seq[option] += 1  # Avança na codificação da opção específica.
    if option == 2:  # Checa se veio da opção de PROFESSORES, verificando o option
        name = input("Informe o nome do estudante: ")  # Pergunta o nome do aluno
        while True:
            try:
                cpf = int(input('Informe o CPF do estudante: '))  # Pergunta o CPF o aluno
                if type(cpf) is int:  # Valida se é do tipo INT para sair do loop
                    break
            except ValueError:
                print("Valor inválido! Por favor digite um valor entre 1-9.")
                continue  # Inicia uma próxima iteração do Menu-Secundário, ignorando as linhas abaixo.
        professor = {'Código': seq[option] + 1, 'Nome': name, 'CPF': cpf}  # Adiciona os dados a um
        # dicionário
        professores.append(professor)  # Adiciona o dicionário do aluno à lista students
        seq[option] += 1  # Avança na codificação da opção específica.
    if option == 3:  # Checa se veio da opção de DISCIPLINA, verificando o option
        name = input("Informe o nome do estudante: ")  # Pergunta o nome do aluno
        while True:
            try:
                cpf = int(input('Informe o CPF do estudante: '))  # Pergunta o CPF o aluno
                if type(cpf) is int:  # Valida se é do tipo INT para sair do loop
                    break
            except ValueError:
                print("Valor inválido! Por favor digite um valor entre 1-9.")
                continue  # Inicia uma próxima iteração do Menu-Secundário, ignorando as linhas abaixo.
        disciplina = {'Código': seq[option] + 1, 'Nome': name, 'CPF': cpf}  # Adiciona os dados a um
        # dicionário
        disciplinas.append(disciplina)  # Adiciona o dicionário da disciplina à lista disciplinas
        seq[option] += 1  # Avança na codificação da opção específica.
    if option == 4:  # Checa se veio da opção de TURMA, verificando o option
        name = input("Informe o nome do estudante: ")  # Pergunta o nome do aluno
        while True:
            try:
                cpf = int(input('Informe o CPF do estudante: '))  # Pergunta o CPF o aluno
                if type(cpf) is int:  # Valida se é do tipo INT para sair do loop
                    break
            except ValueError:
                print("Valor inválido! Por favor digite um valor entre 1-9.")
                continue  # Inicia uma próxima iteração do Menu-Secundário, ignorando as linhas abaixo.
        turma = {'Código': seq[option] + 1, 'Nome': name, 'CPF': cpf}  # Adiciona os dados a um
        # dicionário
        turmas.append(turma)  # Adiciona o dicionário do aluno à lista students
        seq[option] += 1  # Avança na codificação da opção específica.
    if option == 5:  # Checa se veio da opção de MATRÍCULA, verificando o option
        name = input("Informe o nome do estudante: ")  # Pergunta o nome do aluno
        while True:
            try:
                cpf = int(input('Informe o CPF do estudante: '))  # Pergunta o CPF o aluno
                if type(cpf) is int:  # Valida se é do tipo INT para sair do loop
                    break
            except ValueError:
                print("Valor inválido! Por favor digite um valor entre 1-9.")
                continue  # Inicia uma próxima iteração do Menu-Secundário, ignorando as linhas abaixo.
        matricula = {'Código': seq[option] + 1, 'Nome': name, 'CPF': cpf}  # Adiciona os dados a um
        # dicionário
        matriculas.append(matricula)  # Adiciona o dicionário do aluno à lista students
        seq[option] += 1  # Avança na codificação da opção específica.
    input("Pressione ENTER para continuar.")  # Aguarda uma tecla, para facilitar a leitura


def menu_listagem(option):
    """
    Exibe o Menu de Listagem da aplicação.
    :param option: Valor escolhido para representar Aluno/Professor/Disciplina/Turma/Matrícula.
    :return: None
    """
    print("\n===== LISTAGEM =====\n")
    if option == 1:  # Checa se veio da opção de ESTUDANTES, verificando o option
        if estudantes:  # Verifica se a lista students não está fazia
            for registro in estudantes:  # Estrutura de repetição para impressão da lista de nomes.
                print(registro)
        else:  # Se a lista students for vazia, imprime uma mensagem
            print("Não há estudantes cadastrados.")
    input("Pressione ENTER para continuar.")


def menu_exclusao(option):
    """
    Exibe o Menu de Exclusão da aplicação.
    :param option: Valor escolhido para representar Aluno/Professor/Disciplina/Turma/Matrícula.
    :return: None
    """
    print("\n===== EXCLUSÃO =====")
    if option == 1:
        exc = int(input('Informe o código do aluno a ser excluído: '))
        for i in range(len(estudantes)):
            if estudantes[i]['Código'] == exc:
                del estudantes[i]
                break
    input("Pressione ENTER para continuar.")


def menu_atualizacao(option):
    """
    Exibe o Menu de Atualização da aplicação.
    :param option: Valor escolhido para representar Aluno/Professor/Disciplina/Turma/Matrícula.
    :return: None
    """
    print("\n===== ATUALIZAÇÃO =====")
    if option == 1:
        proc = int(input('Informe o código do aluno a ser atualizado: '))
        escolha = int(input('Informe qual campo deseja atualizar: 1 - Nome; 2 - CPF  '))
        for i in range(len(estudantes)):
            if estudantes[i]['Código'] == proc:
                if escolha == 1:
                    estudantes[i]['Nome'] = input('Informe o novo nome: ')
                elif escolha == 2:
                    estudantes[i]['CPF'] = int(input('Informe o novo CPF: '))
                break
    input("Pressione ENTER para continuar.")


menu_principal()
