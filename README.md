# 🏋️ Academia Fit

Sistema de gerenciamento de alunos desenvolvido em Python para academias e personal trainers.

Este projeto foi criado com foco em praticar conceitos fundamentais de Python, como funções, listas, dicionários, estruturas de repetição, condicionais, modularização e persistência de dados utilizando JSON.

---

## 📋 Funcionalidades

- ✅ Cadastro de alunos
- ✅ Listagem de alunos cadastrados
- ✅ Busca de alunos por nome
- ✅ Atualização de peso
- ✅ Exclusão de alunos
- ✅ Cálculo automático de IMC
- ✅ Classificação automática do IMC
- ✅ Relatório geral dos alunos
- ✅ Salvamento automático dos dados em JSON

---

## 🚀 Tecnologias Utilizadas

- Python 3
- JSON
- Terminal / Console

---

## 📂 Estrutura do Projeto

```text
academia-fit/

├── main.py
├── funcoes.py
├── alunos.json
└── README.md
```

---

## 🧮 Cálculo de IMC

O sistema calcula automaticamente o Índice de Massa Corporal (IMC) utilizando a fórmula:

IMC = Peso / Altura²

Classificações utilizadas:

| IMC | Classificação |
|------|---------------|
| Menor que 18.5 | Abaixo do peso |
| 18.5 até 24.9 | Peso normal |
| 25 até 29.9 | Sobrepeso |
| 30 até 34.9 | Obesidade Grau I |
| 35 até 39.9 | Obesidade Grau II |
| Acima de 40 | Obesidade Grau III |

---

## 💻 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/academia-fit.git
```

### 2. Acesse a pasta

```bash
cd academia-fit
```

### 3. Execute o programa

```bash
python main.py
```

---

## 📌 Exemplo de Menu

```text
===== ACADEMIA FIT =====

1 - Cadastrar aluno
2 - Listar alunos
3 - Buscar aluno
4 - Atualizar peso
5 - Excluir aluno
6 - Relatório geral
0 - Sair
```

---

## 🎯 Objetivos do Projeto

- Aplicar conceitos de lógica de programação.
- Desenvolver um CRUD completo em Python.
- Trabalhar com persistência de dados em JSON.
- Simular um sistema real de gerenciamento.
- Construir portfólio para vagas de desenvolvimento.

---

## 🔮 Melhorias Futuras

- Interface gráfica com Tkinter.
- Banco de dados SQLite.
- Sistema de treinos.
- Histórico de evolução corporal.
- Cadastro de avaliações físicas.
- Exportação de relatórios em PDF.
- API utilizando Flask.

---

## 👨‍💻 Autor

**João Pedro Zanandrez**

Estudante de Análise e Desenvolvimento de Sistemas e desenvolvedor em formação.

### Contato

GitHub: https://github.com/JoaoZanandrez

LinkedIn: https://www.linkedin.com/in/joaozanandrez

---

⭐ Se este projeto foi útil para você, deixe uma estrela no repositório.