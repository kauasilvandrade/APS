import customtkinter as ctk

# ----- Configuração da aparência -----
ctk.set_appearance_mode('dark')

#  ----- Criação das funções de funcionalidades -----
def validar_login():
  usuario = campoUsuario.get()
  senha = campoSenha.get()

  if usuario == "joao" and senha == '16789':
    resultadoLogin.configure(text="Login feito com sucesso!", text_color="green")
  else:
    resultadoLogin.configure(text="Login Inválido!", text_color="red")

  
#  ----- Criação da janela principal -----
app = ctk.CTk()
app.title('ECO SCORE')
app.geometry('300x300') 

#  ----- Criação dos campos ----
labelUsuario = ctk.CTkLabel(app, text="Usuário: ")
labelUsuario.pack(pady=10)

campoUsuario = ctk.CTkEntry(app, placeholder_text="Digite o seu usuário: ")
campoUsuario.pack(pady=10)

labelSenha = ctk.CTkLabel(app, text="Senha: ")
labelSenha.pack(pady=10)

campoSenha = ctk.CTkEntry(app, placeholder_text="Digite a sua senha: ", show="*")
campoSenha.pack(pady=10)

botaoLogin = ctk.CTkButton(app, text="Login", command=validar_login)
botaoLogin.pack(pady=10)

resultadoLogin = ctk.CTkLabel(app, text="")
resultadoLogin.pack(pady=10)

app.mainloop()