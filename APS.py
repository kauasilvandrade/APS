import customtkinter as ctk
import pandas as pd
import os

# --- Configurações iniciais ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("EcoScore – Monitoramento de Hábitos Sustentáveis")
app.geometry("500x600")
app.resizable(False, False)

# --- Variáveis globais ---
usuarios = {}
usuario_logado = None
arquivo_excel = "usuarios.xlsx"

# --- Funções auxiliares ---
def carregar_usuarios():
    if os.path.exists(arquivo_excel):
        dados = pd.read_excel(arquivo_excel)
        for _, row in dados.iterrows():
            usuarios[row["E-mail"]] = {
                "nome": row["Nome"],
                "senha": str(row["Senha"]),
                "pontuacao": row["Pontuação"]
            }

def salvar_usuarios():
    df = pd.DataFrame([
        {"Nome": v["nome"], "E-mail": k, "Senha": v["senha"], "Pontuação": v["pontuacao"]}
        for k, v in usuarios.items()
    ])
    df.to_excel(arquivo_excel, index=False)

carregar_usuarios()

# --- Funções principais ---
def mostrar_frame(frame):
    for f in (frame_menu, frame_cadastro, frame_login, frame_quiz, frame_resultado):
        f.pack_forget()
    frame.pack(pady=20)

def cadastrar_usuario():
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    senha = entry_senha.get().strip()

    if not nome or not email or not senha:
        label_status.configure(text="⚠️ Preencha todos os campos.", text_color="#FACC15")
        return

    if email in usuarios:
        label_status.configure(text="❌ Este e-mail já está cadastrado.", text_color="#EF4444")
        return

    usuarios[email] = {"nome": nome, "senha": senha, "pontuacao": 0}
    label_status.configure(text=f"✅ {nome} cadastrado com sucesso!", text_color="#22C55E")
    entry_nome.delete(0, "end")
    entry_email.delete(0, "end")
    entry_senha.delete(0, "end")

def fazer_login():
    global usuario_logado
    email = entry_email_login.get().strip()
    senha = entry_senha_login.get().strip()

    if email in usuarios and usuarios[email]["senha"] == senha:
        usuario_logado = email
        label_status_login.configure(
            text=f"✅ Bem-vindo(a), {usuarios[email]['nome']}!", text_color="#22C55E"
        )
        entry_email_login.delete(0, "end")
        entry_senha_login.delete(0, "end")
        app.after(1000, lambda: mostrar_frame(frame_quiz))
    else:
        label_status_login.configure(text="❌ E-mail ou senha incorretos.", text_color="#EF4444")

def calcular_pontuacao():
    global usuario_logado
    if not usuario_logado:
        return

    respostas = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get()]
    pontos = sum(respostas)
    usuarios[usuario_logado]["pontuacao"] += pontos

    salvar_usuarios()
    mostrar_feedback(pontos)

def mostrar_feedback(pontos):
    if pontos >= 40:
        msg = "Excelente! Você é um exemplo de sustentabilidade! 💚"
    elif pontos >= 20:
        msg = "Muito bom! Continue evoluindo seus hábitos verdes. 🌱"
    else:
        msg = "Vamos melhorar? Pequenas mudanças geram grandes impactos. 🌍"

    label_resultado.configure(text=f"Sua pontuação: {pontos}\n\n{msg}")
    mostrar_frame(frame_resultado)

# --- Menu Principal ---
frame_menu = ctk.CTkFrame(app)
frame_menu.pack(pady=20)

label_titulo_menu = ctk.CTkLabel(frame_menu, text="🌿 EcoScore 🌿", font=ctk.CTkFont(size=26, weight="bold"))
label_titulo_menu.pack(pady=(0,30))

btn_login_menu = ctk.CTkButton(frame_menu, text="Login", width=250, command=lambda: mostrar_frame(frame_login))
btn_login_menu.pack(pady=10)

btn_cadastro_menu = ctk.CTkButton(frame_menu, text="Cadastro", width=250, command=lambda: mostrar_frame(frame_cadastro))
btn_cadastro_menu.pack(pady=10)

btn_sair_menu = ctk.CTkButton(frame_menu, text="Sair", width=250, fg_color="#9CA3AF", hover_color="#6B7280", command=app.destroy)
btn_sair_menu.pack(pady=10)

# --- Cadastro ---
frame_cadastro = ctk.CTkFrame(app, width=400, height=500, corner_radius=15)
label_titulo_cad = ctk.CTkLabel(frame_cadastro, text="Cadastrar Usuário", font=ctk.CTkFont(size=22, weight="bold"))
label_titulo_cad.pack(pady=(10,20))

entry_nome = ctk.CTkEntry(frame_cadastro, placeholder_text="Nome completo", width=300)
entry_nome.pack(pady=5)
entry_email = ctk.CTkEntry(frame_cadastro, placeholder_text="E-mail", width=300)
entry_email.pack(pady=5)
entry_senha = ctk.CTkEntry(frame_cadastro, placeholder_text="Senha", show="*", width=300)
entry_senha.pack(pady=5)

botao_cadastrar = ctk.CTkButton(frame_cadastro, text="Cadastrar", width=300, height=40, fg_color="#3B82F6", hover_color="#2563EB", command=cadastrar_usuario)
botao_cadastrar.pack(pady=10)

label_status = ctk.CTkLabel(frame_cadastro, text="", font=ctk.CTkFont(size=14))
label_status.pack(pady=10)

botao_ir_login = ctk.CTkButton(frame_cadastro, text="Já tem conta? Login", width=300, fg_color="transparent", text_color="#A1A1AA", command=lambda: mostrar_frame(frame_login))
botao_ir_login.pack(pady=5)

# --- Login ---
frame_login = ctk.CTkFrame(app, width=400, height=500, corner_radius=15)
label_titulo_login = ctk.CTkLabel(frame_login, text="Fazer Login", font=ctk.CTkFont(size=22, weight="bold"))
label_titulo_login.pack(pady=(10,20))

entry_email_login = ctk.CTkEntry(frame_login, placeholder_text="E-mail", width=300)
entry_email_login.pack(pady=5)
entry_senha_login = ctk.CTkEntry(frame_login, placeholder_text="Senha", show="*", width=300)
entry_senha_login.pack(pady=5)

botao_login = ctk.CTkButton(frame_login, text="Entrar", width=300, height=40, fg_color="#22C55E", hover_color="#16A34A", command=fazer_login)
botao_login.pack(pady=10)

label_status_login = ctk.CTkLabel(frame_login, text="", font=ctk.CTkFont(size=14))
label_status_login.pack(pady=10)

botao_ir_cad = ctk.CTkButton(frame_login, text="Não tem conta? Cadastre-se", width=300, fg_color="transparent", text_color="#A1A1AA", command=lambda: mostrar_frame(frame_cadastro))
botao_ir_cad.pack(pady=5)

# --- Questionário ---
frame_quiz = ctk.CTkFrame(app)
label_quiz = ctk.CTkLabel(frame_quiz, text="Questionário Sustentável", font=ctk.CTkFont(size=20, weight="bold"))
label_quiz.pack(pady=20)

var1 = ctk.IntVar()
var2 = ctk.IntVar()
var3 = ctk.IntVar()
var4 = ctk.IntVar()
var5 = ctk.IntVar()

ctk.CTkCheckBox(frame_quiz, text="Usou transporte sustentável hoje?", variable=var1, onvalue=10, offvalue=0).pack(anchor="w", padx=50, pady=5)
ctk.CTkCheckBox(frame_quiz, text="Evitou uso de descartáveis?", variable=var2, onvalue=10, offvalue=0).pack(anchor="w", padx=50, pady=5)
ctk.CTkCheckBox(frame_quiz, text="Separou o lixo reciclável?", variable=var3, onvalue=10, offvalue=0).pack(anchor="w", padx=50, pady=5)
ctk.CTkCheckBox(frame_quiz, text="Economizou energia elétrica?", variable=var4, onvalue=10, offvalue=0).pack(anchor="w", padx=50, pady=5)
ctk.CTkCheckBox(frame_quiz, text="Reaproveitou materiais?", variable=var5, onvalue=10, offvalue=0).pack(anchor="w", padx=50, pady=5)

botao_enviar = ctk.CTkButton(frame_quiz, text="Enviar respostas", width=250, height=40, command=calcular_pontuacao)
botao_enviar.pack(pady=20)

# --- Resultado ---
frame_resultado = ctk.CTkFrame(app)
label_resultado = ctk.CTkLabel(frame_resultado, text="", font=("Arial", 18))
label_resultado.pack(pady=40)

btn_voltar_menu = ctk.CTkButton(frame_resultado, text="Voltar ao Menu", command=lambda: mostrar_frame(frame_menu))
btn_voltar_menu.pack()

# Iniciar no menu
mostrar_frame(frame_menu)
app.mainloop()
