from funcoes import *

alunos = carregar_alunos()

while True:
    print('''
=== ACADEMIA FIT ===

1 - Cadastrar aluno
2 - Listar alunos
3 - Buscar aluno
4 - Atualizar peso
5 - Excluir aluno
6 - Relatório
0 - Sair
        ''')
    
    opcao = input('Escolha um opção: ')
    
    if opcao == '1':
        cadastrar_aluno(alunos)
    elif opcao == '2':
        listar_alunos(alunos)
    elif opcao == '3':
        buscar_aluno(alunos)
    elif opcao == '4':
        atualizar_peso(alunos)
    elif opcao == '5':
        excluir_aluno(alunos)
    elif opcao == '6':
        relatorio(alunos)
    elif opcao == '0':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida. Tente novamente.')

salvar_alunos(alunos)
