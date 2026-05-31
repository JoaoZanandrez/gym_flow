import json

def carregar_alunos():
    try:
        with open('alunos.json', 'r', encoding='utf-8') as arquivo:
            alunos = json.load(arquivo)
            return alunos
    except FileNotFoundError:
        return []
    
def salvar_alunos(alunos):
    with open('alunos.json', 'w', encoding='utf-8') as arquivo:
            json.dump(alunos, arquivo, ensure_ascii=False, indent=4)
            
def calcular_imc(peso, altura):
    if altura <= 0:
        raise ValueError('A altura deve ser maior que zero')
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif 18.5 <= imc < 25:
        return 'Peso normal'
    elif 25 <= imc < 30:
        return 'Sobrepeso'
    else:
        return 'Obesidade'
    
def cadastrar_aluno(alunos):
    nome = input('Digite o nome do aluno: ')
    idade = int(input('Digite a idade do aluno: '))
    peso = float(input('Digite o peso do aluno (kg): '))
    altura = float(input('Digite a altura do aluno (m): '))
    imc = calcular_imc(peso, altura)
    aluno = {
        'Nome': nome,
        'Idade': idade,
        'Peso': peso,
        'Altura': altura,
        'imc': imc,
        'classificacao': classificar_imc(imc)
    }
    alunos.append(aluno)
    salvar_alunos(alunos)
    print(f'Aluno {nome} cadastrado com sucesso!')
    
def listar_alunos(alunos):
    if len(alunos) == 0:
        print('Nenhum aluno cadastrado.')
        return
    
    print('\nALUNOS CADASTRADOS\n')
    for aluno in alunos:
        print(f'Nome: {aluno["Nome"]}')
        print(f'Idade: {aluno["Idade"]} anos')
        print(f'Peso: {aluno["Peso"]} kg')
        print(f'Altura: {aluno["Altura"]} m')
        print(f'IMC: {aluno["imc"]:.2f}')
        print(f'Classificação: {aluno["classificacao"]}\n')
        print('-' * 30)
        
def buscar_aluno(alunos):
    nome = input('Digite o nome: ').strip()
    for aluno in alunos:
        if aluno['Nome'].lower() == nome.lower():
            print('\nAluno Encontrado\n')
            for chave, valor in aluno.items():
                print(f'{chave}: {valor}')
                
            return
    print('Aluno não encontrado.')
    
def atualizar_peso(alunos):

    nome = input("Nome do aluno: ")

    for aluno in alunos:

        if aluno["Nome"].lower() == nome.lower():

            novo_peso = float(input("Novo peso: "))

            aluno["Peso"] = novo_peso

            novo_imc = calcular_imc(
                aluno["Peso"],
                aluno["Altura"]
            )

            aluno["imc"] = round(novo_imc, 2)

            aluno["classificacao"] = classificar_imc(
                novo_imc
            )

            salvar_alunos(alunos)

            print("Peso atualizado!")
            return

    print("Aluno não encontrado.")
    
def excluir_aluno(alunos):
    nome = input('Nome do aluno: ')
    for aluno in alunos:
        if aluno['Nome'].lower() == nome.lower():
            alunos.remove(aluno)
            salvar_alunos(alunos)
            print('Aluno excluído com sucesso!')
            return
        
def relatorio(alunos):

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    media_idade = sum(
        aluno["Idade"] for aluno in alunos
    ) / len(alunos)

    maior_imc = max(
        alunos,
        key=lambda aluno: aluno["imc"]
    )

    menor_imc = min(
        alunos,
        key=lambda aluno: aluno["imc"]
    )

    print("\nRELATÓRIO")

    print(f"Total de alunos: {len(alunos)}")

    print(f"Média de idade: {media_idade:.1f}")

    print(
        f"Maior IMC: {maior_imc['nome']} "
        f"({maior_imc['imc']})"
    )

    print(
        f"Menor IMC: {menor_imc['nome']} "
        f"({menor_imc['imc']})"
    )