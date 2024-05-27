# Importando bibliotecas
import sqlite3 as lite
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Conectando ao banco de dados
conexao = lite.connect('Oficina.db')

# Criando a tabela tbl_clientes se não existir
with conexao:
    cur = conexao.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tbl_clientes (
            id_client INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone INTEGER,
            nif INTEGER,
            morada TEXT
        )
    """)

# Função para inserir dados na tabela tbl_clientes
def inserir_dados(i):
    with conexao:
        cur = conexao.cursor()
        query = "INSERT INTO tbl_clientes (nome, email, telefone, nif, morada) VALUES (?, ?, ?, ?, ?)"
        cur.execute(query, i)

# Função para obter informações da tabela tbl_clientes
def mostrar_info():
    lista = []
    with conexao:
        cur = conexao.cursor()
        query = "SELECT * FROM tbl_clientes"
        cur.execute(query)
        informacoes = cur.fetchall()
        for i in informacoes:
            lista.append(i)
    return lista

# Função para inserir dados através da interface gráfica
def inserir():
    nome = caixaTexto_nome.get()
    email = caixa_email.get()
    telefone = caixa_telefone.get()
    nif = caixa_nif.get()
    morada = caixa_morada.get()

    lista = [nome, email, telefone, nif, morada]

    if nome == '':
        messagebox.showerror('Erro', 'O nome não pode ser vazio')
    else:
        inserir_dados(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
        caixaTexto_nome.delete(0, 'end')
        caixa_email.delete(0, 'end')
        caixa_telefone.delete(0, 'end')
        caixa_nif.delete(0, 'end')
        caixa_morada.delete(0, 'end')

        mostrar()

# Função para mostrar dados na tabela
def mostrar():
    for widget in frame_centro.winfo_children():
        widget.destroy()
    
    tree = ttk.Treeview(frame_centro, selectmode="extended", columns=tabela_head, show="headings")

    vsb = ttk.Scrollbar(frame_centro, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_centro, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_centro.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "center"]
    h = [30, 170, 140, 100, 120, 150]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    lista = mostrar_info()
    for item in lista:
        tree.insert('', 'end', values=item)

################# Configurando Interface Gráfica ###############

# Cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # Branca
co2 = "#4fa882"  # Verde
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra
co5 = "#e06636"  # - Profit
co6 = "#038cfc"  # Azul
co7 = "#ef5350"  # Vermelha
co8 = "#263238"  # + Verde
co9 = "#e9edf5"  # Sky Blue

# Criando janela principal
janela = Tk()
janela.title("Formulário de Clientes")
janela.geometry("1043x453")
janela.configure(background=co9)
janela.resizable(width=False, height=False)

# Dividindo a janela em frames
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky='NSEW', padx=0, pady=1)

frame_centro = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_centro.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky='NSEW')

# Label de título
label_titulo = Label(frame_cima, text='Formulário de Clientes', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
label_titulo.place(x=10, y=20)

# Configurando Frame de baixo (campos de entrada)
label_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_nome.place(x=10, y=10)

caixaTexto_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
caixaTexto_nome.place(x=10, y=40)

label_email = Label(frame_baixo, text='Email *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_email.place(x=10, y=70)

caixa_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
caixa_email.place(x=10, y=100)

label_telefone = Label(frame_baixo, text='Telefone *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_telefone.place(x=10, y=130)

caixa_telefone = Entry(frame_baixo, width=45, justify='left', relief='solid')
caixa_telefone.place(x=10, y=160)

label_nif = Label(frame_baixo, text='Nif *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_nif.place(x=10, y=190)

caixa_nif = Entry(frame_baixo, width=45, justify='left', relief='solid')
caixa_nif.place(x=10, y=220)

label_morada = Label(frame_baixo, text='Morada *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_morada.place(x=10, y=250)

caixa_morada = Entry(frame_baixo, width=45, justify='left', relief='solid')
caixa_morada.place(x=10, y=280)

# Botões
botao_inserir = Button(frame_baixo, text="Inserir", command=inserir, bg=co6, fg=co1, font=('Ivy 10 bold'), relief='flat')
botao_inserir.place(x=10, y=320)

botao_atualizar = Button(frame_baixo, text="Atualizar", bg=co2, fg=co1, font=('Ivy 10 bold'), relief='flat')
botao_atualizar.place(x=110, y=320)

botao_eliminar = Button(frame_baixo, text="Eliminar", bg=co7, fg=co1, font=('Ivy 10 bold'), relief='flat')
botao_eliminar.place(x=210, y=320)

# Configurando Frame do centro (tabela)
tabela_head = ['ID', 'Nome', 'Email', 'Telefone', 'Nif', 'Morada']

mostrar()

janela.mainloop()
