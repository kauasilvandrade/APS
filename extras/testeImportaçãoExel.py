import pandas as pd

# Recebe dois dados do usuário
nome = input("Digite o nome: ")
idade = input("Digite a idade: ")

# Cria um DataFrame com esses dados
dados = pd.DataFrame({
    "Nome": [nome],
    "Idade": [idade]
})

# Exporta para um arquivo Excel
dados.to_excel("dados.xlsx", index=False)

print("Arquivo 'dados.xlsx' criado com sucesso!")
