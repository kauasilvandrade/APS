import customtkinter as ctk

# ----- Configuração da aparência -----
ctk.set_appearance_mode('dark') # Tema

#  ----- Criação das funções de funcionalidades -----
def validar_login():
  usuario = campoUsuario.get() # Pegar valor digitado
  senha = cammpoSenha.get() # Pegar valor digitado

  # Verificação
  if usuario == 'kaua' and senha == '123456':
    resultadoLogin.configure(text='Login feito com sucesso!', text_color='green') # Alterar propriedades do elemento
  else:
    resultadoLogin.configure(text="Login inválido!", text_color='red')
  
#  ----- Criação da janela principal -----
app = ctk.CTk() # Configurações APLICAÇÃO PRINCIPAL
app.title('ECO SCORE')
app.geometry('300x300') # Tamanho da janela em px

#  ----- Criação dos campos ----

# Label NOME DO USUÁRIO
labelUsuario = ctk.CTkLabel(app, text="Usuário; ")
labelUsuario.pack(pady=10) # Adiciona o campo ao app / 10px em cima e em baixo

# Entry (input) 
campoUsuario = ctk.CTkEntry(app, placeholder_text='Digite o seu usuário')
campoUsuario.pack(pady=10)

# Label SENHA DO USUÁRIO
labelSenha = ctk.CTkLabel(app, text="Senha: ")
labelSenha.pack(pady=10) # Adiciona ao app

# Entry (input)
cammpoSenha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
cammpoSenha.pack(pady=10)

# Button
botaoLogin = ctk.CTkButton(app, text='Login', command=validar_login)
botaoLogin.pack(pady=10)
# Feedback de login
resultadoLogin = ctk.CTkLabel(app, text='')
resultadoLogin.pack(pady=10)
#  ----- inicia o loop da aplicação -----
app.mainloop()