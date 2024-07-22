""" PUC-PR | Atividade Somativa 1
    Disciplina: Raciocínio Computacional (11100010563_20241_03)
    Jesus Wildes Suathê Farias
"""

students = []  # Inicia uma lista vazia para o nome dos estudantes
dict_students = {}
code = 0

while True:  # Função While para o funcionamento do Menu-Principal
    print("----- MENU PRINCIPAL -----")
    print("\n(1) Gerenciar estudantes.")
    print("(2) Gerenciar professores.")
    print("(3) Gerenciar disciplinas.")
    print("(4) Gerenciar turmas.")
    print("(5) Gerenciar matrículas.")
    print("(9) Sair.")
    try:  # Função Try-Catch para input diferente de INT
        option = int(input("\nInforme a opção desejada: "))  # Armazena a escolha na var option para Match-Case e IFs
    except ValueError:  # Captura exceção de valores diferentes de INT
        print("Valor inválido! Por favor digite um valor entre 1-9.")
        continue  # Inicia uma próxima iteração, ignorando as linhas abaixo
    match option:  # Match-Case para escolha da opção
        case 1:  # Altera a variável choice que fixa a repetição do Menu-Secundário.
            choice = "ESTUDANTES"

        case 2:  # Conforme Tarefa. Qualquer opção fora "ESTUDANTES" deverá retornar "EM DESENVOLVIMENTO"
            choice = "PROFESSORES"
            print("##### EM DESENVOLVIMENTO #####")
            input("Pressione ENTER para continuar.")  # Mensagem exigindo qualquer tecla, para facilitar a leitura
            continue  # Inicia uma próxima iteração, ignorando as linhas abaixo
        case 3:
            choice = "DISCIPLINAS"
            print("##### EM DESENVOLVIMENTO #####")
            input("Pressione ENTER para continuar.")
            continue  # Inicia uma próxima iteração, ignorando as linhas abaixo
        case 4:
            choice = "TURMAS"
            print("##### EM DESENVOLVIMENTO #####")
            input("Pressione ENTER para continuar.")
            continue  # Inicia uma próxima iteração, ignorando as linhas abaixo
        case 5:
            choice = "MATRÍCULAS"
            print("##### EM DESENVOLVIMENTO #####")
            input("Pressione ENTER para continuar.")
            continue  # Inicia uma próxima iteração, ignorando as linhas abaixo
        case 9:  # Opção de encerrar o programa.
            print("====== Sistema finalizado ======")
            break  # Finaliza o While do Menu-Principal.

        case _:  # Opção default para o caso de um valor diferente das opções.
            print("\nOpção inválida!")
            continue

    while True:  # Segundo While para o Menu-Secundário
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
                print("\n===== INCLUSÃO =====\n")
                if option == 1:  # Checa se veio da opção de ESTUDANTES, verificando o option
                    name = input("Informe o nome do estudante: ")  # Pergunta o nome do aluno
                    cpf = int(input('Informe o CPF do estudante: '))  # Pergunta o CPF o aluno
                    dict_students = {'Código': code + 1, 'Nome': name, 'CPF': cpf}      # Adiciona os dados a um
                    # dicionário
                    students.append(dict_students)  # Adiciona o dicionário do aluno à lista students
                    code += 1   # Avança na codificação.
                    input("Pressione ENTER para continuar.")  # Aguarda uma tecla, para facilitar a leitura
                continue  # Nova iteração do Menu-Secundário
            case 2:
                print("\n===== LISTAGEM =====\n")
                if option == 1:  # Checa se veio da opção de ESTUDANTES, verificando o option
                    if students:  # Verifica se a lista students não está fazia
                        for registro in students:  # Estrutura de repetição para impressão da lista de nomes.
                            print(registro)
                    else:  # Se a lista students for vazia, imprime uma mensagem
                        print("Não há estudantes cadastrados.")
                input("Pressione ENTER para continuar.")
                continue
            case 3:  # Conforme a tarefa. Opções ATUALIZAÇÃO e EXCLUSÃO deve exibir apenas "EM DESENVOLVIMENTO"
                print("\n===== ATUALIZAÇÃO =====")
                if option == 1:
                    proc = int(input('Informe o código do aluno a ser atualizado: '))
                    escolha = int(input('Informe qual campo deseja atualizar: 1 - Nome; 2 - CPF  '))
                    for i in range(len(students)):
                        if students[i]['Código'] == proc:
                            if escolha == 1:
                                students[i]['Nome'] = input('Informe o novo nome: ')
                            elif escolha == 2:
                                students[i]['CPF'] = int(input('Informe o novo CPF: '))
                            break
                input("Pressione ENTER para continuar.")
                continue
            case 4:
                print("\n===== EXCLUSÃO =====")
                if option == 1:
                    exc = int(input('Informe o código do aluno a ser excluído: '))
                    for i in range(len(students)):
                        if students[i]['Código'] == exc:
                            del students[i]
                            break
                input("Pressione ENTER para continuar.")
                continue
            case 9:  # Finaliza o Menu-Secundário e retorna ao Menu-Principal
                break
            case _:  # Opção default de Match-Case para a escolha de uma ação diferente.
                print("\nOpção inválida!")
                continue
