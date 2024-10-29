import tkinter as tk
from tkinter import messagebox, ttk

# Função para adicionar placeholder nos Entry
def add_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", lambda event: clear_placeholder(event, placeholder))
    entry.bind("<FocusOut>", lambda event: set_placeholder(event, placeholder))

def clear_placeholder(event, placeholder):
    if event.widget.get() == placeholder:
        event.widget.delete(0, tk.END)
        event.widget.config(foreground='black')

def set_placeholder(event, placeholder):
    if event.widget.get() == "":
        event.widget.insert(0, placeholder)
        event.widget.config(foreground='grey')

# Função para alternar entre mostrar e ocultar senha
def toggle_password():
    if entry_senha.cget('show') == '':
        entry_senha.config(show='*')
        btn_toggle_password.config(text='Mostrar')
    else:
        entry_senha.config(show='')
        btn_toggle_password.config(text='Ocultar')

def abrir_tela_denuncia():
    # Fechar a janela de login
    janela_login.destroy()
    
    # Criar a janela de denúncia
    janela_denuncia = tk.Tk()
    janela_denuncia.title("Formulário de Denúncia")
    janela_denuncia.geometry("400x600")
    janela_denuncia.configure(bg="#f0f0f0")
    
    # Menu de navegação
    frame_menu = tk.Frame(janela_denuncia, bg="#F49CF5", height=50)
    frame_menu.pack(fill="x")
    
    btn_suporte = tk.Button(frame_menu, text="Suporte Psicológico", bg="#F49CF5", fg="#000000", relief="flat")
    btn_suporte.pack(side="left", padx=10)
    
    btn_denuncia = tk.Button(frame_menu, text="Denúncias e Queixas", bg="#F49CF5", fg="#000000", relief="flat")
    btn_denuncia.pack(side="left", padx=10)
    
    btn_recursos = tk.Button(frame_menu, text="Recursos Comunitários", bg="#F49CF5", fg="#000000", relief="flat")
    btn_recursos.pack(side="left", padx=10)
    
    # Título do formulário
    label_titulo = tk.Label(janela_denuncia, text="Formulário de Denúncia", font=("Helvetica", 24), bg="#f0f0f0", fg="#F49CF5")
    label_titulo.pack(pady=20)
    
    # Campo de entrada do nome completo
    entry_nome_completo = ttk.Entry(janela_denuncia, font=("Helvetica", 14), style="Rounded.TEntry")
    entry_nome_completo.pack(pady=5, ipadx=10, ipady=10)
    add_placeholder(entry_nome_completo, "Nome Completo")
    
    # Campo de entrada do e-mail
    entry_email = ttk.Entry(janela_denuncia, font=("Helvetica", 14), style="Rounded.TEntry")
    entry_email.pack(pady=5, ipadx=10, ipady=10)
    add_placeholder(entry_email, "E-mail")
    
    # Campo de entrada da descrição da denúncia
    entry_denuncia = ttk.Entry(janela_denuncia, font=("Helvetica", 14), style="Rounded.TEntry")
    entry_denuncia.pack(pady=5, ipadx=10, ipady=10)
    add_placeholder(entry_denuncia, "Descreva sua denúncia")
    
    # Campo de entrada do tipo de denúncia
    entry_tipo_denuncia = ttk.Entry(janela_denuncia, font=("Helvetica", 14), style="Rounded.TEntry")
    entry_tipo_denuncia.pack(pady=5, ipadx=10, ipady=10)
    add_placeholder(entry_tipo_denuncia, "Tipo de Denúncia")
    
    # Campo de confirmação da senha
    entry_confirm_password = ttk.Entry(janela_denuncia, font=("Helvetica", 14), style="Rounded.TEntry", show="*")
    entry_confirm_password.pack(pady=5, ipadx=10, ipady=10)
    add_placeholder(entry_confirm_password, "Confirm Password")
    
    # Botão de registrar denúncia
    botao_registrar = tk.Button(janela_denuncia, text="Registrar Denúncia", font=("Helvetica", 14), bg="#F49CF5", fg="#000000")
    botao_registrar.pack(pady=20)
    
    # Iniciar a interface gráfica da janela de denúncia
    janela_denuncia.mainloop()

def validar_login():
    usuario = entry_nome.get()
    senha = entry_senha.get()
    
    if usuario == "aluno" and senha == "123":
        messagebox.showinfo("Login", "Login realizado com sucesso!")
        abrir_tela_denuncia()
    else:
        messagebox.showerror("Erro", "Nome de usuário ou senha incorretos")

# Função para criar uma nova conta (apenas uma mensagem de exemplo)
def criar_conta():
    messagebox.showinfo("Criar Conta", "Função de criar conta não implementada.")

# Configuração da janela principal de login
janela_login = tk.Tk()
janela_login.title("Login")
janela_login.geometry("300x400")
janela_login.configure(bg="#f0f0f0")

# Ícone de login (pode ser ajustado conforme necessário)
icon_login = tk.Label(janela_login, text="👤", font=("Helvetica", 48), bg="#f0f0f0")
icon_login.pack(pady=20)

# Título
label_titulo = tk.Label(janela_login, text="Login", font=("Helvetica", 24), bg="#f0f0f0")
label_titulo.pack(pady=10)

# Campo de entrada do nome
entry_nome = ttk.Entry(janela_login, font=("Helvetica", 14), style="Rounded.TEntry")
entry_nome.pack(pady=5, ipadx=10, ipady=10)
add_placeholder(entry_nome, "Nome")

# Campo de entrada da senha
entry_senha = ttk.Entry(janela_login, font=("Helvetica", 14), style="Rounded.TEntry", show="*")
entry_senha.pack(pady=5, ipadx=10, ipady=10)
add_placeholder(entry_senha, "Senha")

# Botão para mostrar/ocultar senha
btn_toggle_password = tk.Button(janela_login, text="Mostrar", command=toggle_password, bg="#F49CF5", fg="#000000", relief="flat")
btn_toggle_password.pack(pady=5)

# Botão de entrar
botao_entrar = tk.Button(janela_login, text="ENTRAR", font=("Helvetica", 14), bg="#F49CF5", fg="#000000", command=validar_login)
botao_entrar.pack(pady=10)

# Botão de criar conta
botao_criar_conta = tk.Button(janela_login, text="CRIAR CONTA", font=("Helvetica", 14), bg="#F49CF5", fg="#000000", command=criar_conta)
botao_criar_conta.pack(pady=10)

# Estilo personalizado para os campos de entrada arredondados
style = ttk.Style()
style.configure("Rounded.TEntry", fieldbackground="#ffffff", bordercolor="#F49CF5", relief="flat")
style.map("Rounded.TEntry", fieldbackground=[('focus', '#ffffff')])

# Iniciar a interface gráfica
janela_login.mainloop()