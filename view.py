#importando o Tkinter
from tkinter import *
from tkinter import ttk
from main import mostrar_info

################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # - profit
co6 = "#038cfc"  # azul
co7 = "#ef5350"  # vermelha
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # sky blue

################# criando Janela ###############

janela = Tk()
janela.title("Formulario de Clientes")
janela.geometry("1043x453")
janela.configure(background=co9)
janela.resizable(width=False, height=False)

################# Dividindo a janela ###############
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky='NSEW', padx=0, pady=1)

frame_centro = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_centro.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky='NSEW')

################# label de titulo ###############
label_titulo = Label(frame_cima, text='Formulario de Clientes', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
label_titulo.place(x=10, y=20)

################# Configurando Frame de baixo ###############
label_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_nome.place(x=10, y=10)

# campo Nome
caixaTexto_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
caixaTexto_nome.place(x=10, y=40)

# Email
label_email = Label(frame_baixo, text='Email *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_email.place(x=10, y=70)

# campo Email
caixa_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
caixa_email.place(x=10, y=100)

# Telefone
label_telefone = Label(frame_baixo, text='Telefone *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_telefone.place(x=10, y=130)

# campo Telefone
caixa_telefone = Entry(frame_baixo, width=45, justify='left', relief='solid')
caixa_telefone.place(x=10, y=160)

# Nif
label_nif = Label(frame_baixo, text='Nif *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_nif.place(x=10, y=190)

# campo Nif
caixa_nif = Entry(frame_baixo, width=45, justify='left', relief='solid')
caixa_nif.place(x=10, y=220)

# Morada
label_morada = Label(frame_baixo, text='Morada *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_morada.place(x=10, y=250)

# campo Morada
caixa_morada = Entry(frame_baixo, width=45, justify='left', relief='solid')
caixa_morada.place(x=10, y=280)

# Função para inserir dados na tabela
def inserir_dados():
    nome = caixaTexto_nome.get()
    email = caixa_email.get()
    telefone = caixa_telefone.get()
    nif = caixa_nif.get()
    morada = caixa_morada.get()

    if nome and email and telefone and nif and morada:  # Verifica se todos os campos estão preenchidos
        tree.insert('', 'end', values=(tree.get_children().__len__()+1, nome, email, telefone, nif, morada))
        caixaTexto_nome.delete(0, END)
        caixa_email.delete(0, END)
        caixa_telefone.delete(0, END)
        caixa_nif.delete(0, END)
        caixa_morada.delete(0, END)
    else:
        print("Preencha todos os campos")

# Função para atualizar dados selecionados na tabela
def atualizar_dados():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        tree.item(selected_item, values=(item['values'][0], caixaTexto_nome.get(), caixa_email.get(), caixa_telefone.get(), caixa_nif.get(), caixa_morada.get()))
    else:
        print("Selecione um item para atualizar")

# Função para deletar dados selecionados na tabela
def deletar_dados():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        print("Selecione um item para deletar")

# Botão de Inserir
botao_inserir = Button(frame_baixo, text="Inserir", command=inserir_dados, bg=co6, fg=co1, font=('Ivy 10 bold'), relief='flat')
botao_inserir.place(x=10, y=320)

# Botão de Atualizar
botao_atualizar = Button(frame_baixo, text="Atualizar", command=atualizar_dados, bg=co2, fg=co1, font=('Ivy 10 bold'), relief='flat')
botao_atualizar.place(x=110, y=320)

# Botão de Eliminar
botao_eliminar = Button(frame_baixo, text="Eliminar", command=deletar_dados, bg=co7, fg=co1, font=('Ivy 10 bold'), relief='flat')
botao_eliminar.place(x=210, y=320)

################# Configurando Frame do centro ###############

#lista para cabeçalho
tabela_head = ['ID', 'Nome', 'Email', 'Telefone', 'Nif', 'Morada']

# criando a tabela
tree = ttk.Treeview(frame_centro, selectmode="extended", columns=tabela_head, show="headings")

# vertical scrollbar
vsb = ttk.Scrollbar(frame_centro, orient="vertical", command=tree.yview)

# horizontal scrollbar
hsb = ttk.Scrollbar(frame_centro, orient="horizontal", command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')

frame_centro.grid_rowconfigure(0, weight=12)

# Configurando as colunas da tabela
hd = ["nw", "nw", "nw", "nw", "nw", "center"]
h = [30, 170, 140, 100, 120, 150]
n = 0

for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
    tree.column(col, width=h[n], anchor=hd[n])
    n += 1

# Função para mostrar dados na tabela
def mostrar():
    lista = mostrar_info()  # Obtendo dados de uma função externa (main.py)
    for item in lista:
        tree.insert('', 'end', values=item)

mostrar()

janela.mainloop()
