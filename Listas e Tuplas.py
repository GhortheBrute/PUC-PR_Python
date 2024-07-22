print('Listas')
estudantes = ['João', 'Clemencia', 'Maria', 'Felipe']
print(estudantes)
estudantes.append('Jesus')
print(estudantes)
estudantes.sort()
print(estudantes)
for estudante in estudantes:
    print(estudante)
print(f'\nTuplas')
professores = ('Fernando', 'Fernanda', 'Derik', 'Clodoaldo')
print(professores, "imutáveis")
print(f'\nDicionários')
turma = {100: 'Fernando', 101: 'João', 102: 'Maria'}
print(turma)
for classe in turma:
    print('turma', classe)
for classe in turma.keys():
    print('turma.keys', classe)
for classe, valor in turma.items():
    print('turma.itens', classe, valor)
for valor in turma.values():
    print('turma.values', valor)
print(estudantes[0])
code = [0, 0, 0, 0, 0]
print(code[0] + 1)
code[0] += 2
print(code[0] + 1)
print(code)

