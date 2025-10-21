# EcoScore - Monitoramento de Hábitos Sustentáveis

usuarios = {}

def menuPrincipal():
  print("\n🌱 ECO SCORE - Monitoramento de Hábitos Sustentáveis 🌎")
  print("1. Cadastrar usuário")
  print("2. Fazer login")
  print("3. Sair")
  return input("Escolha uma opção: ")

def cadastroUsuario(): 
  print("\n--- Cadastro de Usuário ---")
  nome = input("Digite seu nome: ")
  email = input("Digite seu email: ")
  senha = input("Crie uma senha: ")

  if email in usuarios:
    print("❌ Este e-mail já está cadastrado.")
  else:
    usuarios[email] = {"nome": nome, "senha": senha, "pontuacao": 0}
    print(f"✅ Usuário {nome} cadastrado com sucesso!")

def login():
  print("\n--- Login ---")
  email = input("E-mail: ")
  senha = input("Senha: ")

  if email in usuarios and usuarios[email]["senha"] == senha:
    print(f"✅ Bem vindo(a), {usuarios[email]['nome']}!")
    questionario(email)
  else:
    print("❌ E-mail ou senha incorretos.")
    
def questionario(email):
  print("\n--- Questionário de Hábitos Sustentáveis ---")
  pontuacao = 0

  perguntas = [
    ("Você utilizou transporte público, bicicleta ou caminhou hoje? (s/n): ", 10),
    ("Você evitou o uso de copos e talheres descartáveis? (s/n): ", 10),
    ("Separou o lixo reciclável corretamente? (s/n): ", 10),
    ("Você economizou energia eletrica hoje? (s/n): ", 10),
    ("Você reduziu o consumo de carne vermelha hoje? (s/n): ", 10)
  ]

  for pergunta, pontos in perguntas:
    resposta = input(pergunta).lower()

    if resposta == "s":
      pontuacao += pontos

  usuarios[email]["pontuacao"] += pontuacao
  print(f"\n🌿 Sua pontuacao de hoje foi: {pontuacao} pontos!")
  feedback(pontuacao)

def feedback(pontos):
  print("\n--- Feedback Sustentável ---")
  if pontos >= 40: 
    print("Exelente! Você é um exemplo de sustentabilidade! 💚")
  elif pontos <= 20:
    print("Muito bom! Continue evoluindo seus hábitos verdes. 🌱")
  else:
    print("Vamos melhorar? Pequenas mudanças geram grandes impactos. 🌏")


# Loop principal
while True:
  opcao = menuPrincipal()
  if opcao == "1":
    cadastroUsuario()
  elif opcao == "2":
    login()
  elif opcao == "3":
    print("👋 Até logo! Continue praticando a sustentabilidade!")
    break
  else:
    print("❌ Opção inválida, tente novamente.")
    


# COMTENTARIOS ---------------
## OBJETO
# user = {
#   'kaua422@gmail.com': {
#       'nome': 'Kauã', 
#       'senha': '09092006z', 
#       'pontuacao': 0
#     }
# }

# print(user["kaua422@gmail.com"]["senha"])

# Perguntar/ dica - responder com uma messagem ✅