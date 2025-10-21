import customtkinter as ctk

# Configuração inicial da janela
ctk.set_appearance_mode("light")  # "dark" ou "light"
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("EcoScore – Monitoramento de Hábitos Sustentáveis")
app.geometry("600x400")

# -----------------------------
# Variáveis globais
# -----------------------------
usuarios = {}
usuario_logado = None

# -----------------------------
# Funções de navegação
# -----------------------------
def mostrar_frame(frame):
    """Esconde todos os frames e mostra o escolhido"""
    for f in (frame_menu, frame_login, frame_cadastro, frame_quiz, frame_resultado):
        f.pack_forget()
    frame.pack(fill="both", expand=True)

# -----------------------------
# Funções do sistema
# -----------------------------
def cadastrar_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()

    if email in usuarios:
        label_status_cadastro.configure(text="❌ Este e-mail já está cadastrado.", text_color="red")
    else:
        usuarios[email] = {"nome": nome, "senha": senha, "pontuacao": 0}
        label_status_cadastro.configure(text=f"✅ {nome} cadastrado com sucesso!", text_color="green")

def login_usuario():
    global usuario_logado
    email = entry_login_email.get()
    senha = entry_login_senha.get()

    if email in usuarios and usuarios[email]["senha"] == senha:
        usuario_logado = email
        label_status_login.configure(text=f"✅ Bem-vindo(a), {usuarios[email]['nome']}!", text_color="green")
        app.after(1000, lambda: mostrar_frame(frame_quiz))
    else:
        label_status_login.configure(text="❌ E-mail ou senha incorretos.", text_color="red")

def calcular_pontuacao():
    global usuario_logado
    respostas = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get()]
    pontuacao = sum(respostas)
    usuarios[usuario_logado]["pontuacao"] += pontuacao
    mostrar_feedback(pontuacao)

def mostrar_feedback(pontos):
    if pontos >= 40:
        mensagem = "Excelente! Você é um exemplo de sustentabilidade! 💚"
    elif pontos >= 20:
        mensagem = "Muito bom! Continue evoluindo seus hábitos verdes. 🌱"
    else:
        mensagem = "Vamos melhorar? Pequenas mudanças geram grandes impactos. 🌍"

    label_resultado.configure(text=f"Sua pontuação: {pontos}\n\n{mensagem}")
    mostrar_frame(frame_resultado)

# -----------------------------
# FRAME MENU
# -----------------------------
frame_menu = ctk.CTkFrame(app)
label_titulo = ctk.CTkLabel(frame_menu, text="🌿 EcoScore 🌿", font=("Arial", 26, "bold"))
label_titulo.pack(pady=40)

btn_login = ctk.CTkButton(frame_menu, text="Fazer Login", command=lambda: mostrar_frame(frame_login))
btn_login.pack(pady=10)

btn_cadastro = ctk.CTkButton(frame_menu, text="Cadastrar-se", command=lambda: mostrar_frame(frame_cadastro))
btn_cadastro.pack(pady=10)

btn_sair = ctk.CTkButton(frame_menu, text="Sair", fg_color="gray", command=app.destroy)
btn_sair.pack(pady=10)

# -----------------------------
# FRAME CADASTRO
# -----------------------------
frame_cadastro = ctk.CTkFrame(app)
ctk.CTkLabel(frame_cadastro, text="Cadastro de Usuário", font=("Arial", 20, "bold")).pack(pady=20)

entry_nome = ctk.CTkEntry(frame_cadastro, placeholder_text="Nome completo")
entry_nome.pack(pady=5)

entry_email = ctk.CTkEntry(frame_cadastro, placeholder_text="E-mail")
entry_email.pack(pady=5)

entry_senha = ctk.CTkEntry(frame_cadastro, placeholder_text="Senha", show="*")
entry_senha.pack(pady=5)

btn_cadastrar = ctk.CTkButton(frame_cadastro, text="Cadastrar", command=cadastrar_usuario)
btn_cadastrar.pack(pady=10)

label_status_cadastro = ctk.CTkLabel(frame_cadastro, text="")
label_status_cadastro.pack()

btn_voltar_cadastro = ctk.CTkButton(frame_cadastro, text="Voltar", fg_color="gray", command=lambda: mostrar_frame(frame_menu))
btn_voltar_cadastro.pack(pady=10)

# -----------------------------
# FRAME LOGIN
# -----------------------------
frame_login = ctk.CTkFrame(app)
ctk.CTkLabel(frame_login, text="Login", font=("Arial", 20, "bold")).pack(pady=20)

entry_login_email = ctk.CTkEntry(frame_login, placeholder_text="E-mail")
entry_login_email.pack(pady=5)

entry_login_senha = ctk.CTkEntry(frame_login, placeholder_text="Senha", show="*")
entry_login_senha.pack(pady=5)

btn_entrar = ctk.CTkButton(frame_login, text="Entrar", command=login_usuario)
btn_entrar.pack(pady=10)

label_status_login = ctk.CTkLabel(frame_login, text="")
label_status_login.pack()

btn_voltar_login = ctk.CTkButton(frame_login, text="Voltar", fg_color="gray", command=lambda: mostrar_frame(frame_menu))
btn_voltar_login.pack(pady=10)

# -----------------------------
# FRAME QUESTIONÁRIO
# -----------------------------
frame_quiz = ctk.CTkFrame(app)
ctk.CTkLabel(frame_quiz, text="Questionário Sustentável", font=("Arial", 20, "bold")).pack(pady=20)

var1 = ctk.IntVar()
var2 = ctk.IntVar()
var3 = ctk.IntVar()
var4 = ctk.IntVar()
var5 = ctk.IntVar()

ctk.CTkCheckBox(frame_quiz, text="Usou transporte sustentável hoje?", variable=var1, onvalue=10, offvalue=0).pack(anchor="w", padx=80)
ctk.CTkCheckBox(frame_quiz, text="Evitou uso de descartáveis?", variable=var2, onvalue=10, offvalue=0).pack(anchor="w", padx=80)
ctk.CTkCheckBox(frame_quiz, text="Separou o lixo reciclável?", variable=var3, onvalue=10, offvalue=0).pack(anchor="w", padx=80)
ctk.CTkCheckBox(frame_quiz, text="Economizou energia elétrica?", variable=var4, onvalue=10, offvalue=0).pack(anchor="w", padx=80)
ctk.CTkCheckBox(frame_quiz, text="Reaproveitou materiais?", variable=var5, onvalue=10, offvalue=0).pack(anchor="w", padx=80)

btn_enviar = ctk.CTkButton(frame_quiz, text="Enviar respostas", command=calcular_pontuacao)
btn_enviar.pack(pady=20)

# -----------------------------
# FRAME RESULTADO
# -----------------------------
frame_resultado = ctk.CTkFrame(app)
label_resultado = ctk.CTkLabel(frame_resultado, text="", font=("Arial", 18))
label_resultado.pack(pady=40)

btn_voltar_menu = ctk.CTkButton(frame_resultado, text="Voltar ao Menu", command=lambda: mostrar_frame(frame_menu))
btn_voltar_menu.pack()

# Iniciar na tela de menu
mostrar_frame(frame_menu)
app.mainloop()
