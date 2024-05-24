#importando o Tkinter
from tkinter import *
from tkinter import ttk

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

# Botão de Inserir
botao_inserir = Button(frame_baixo, text="Inserir", bg=co6, fg=co1, font=('Ivy 10 bold'), relief='flat')
botao_inserir.place(x=10, y=320)

# Botão de Atualizar
botao_atualizar = Button(frame_baixo, text="Atualizar", bg=co2, fg=co1, font=('Ivy 10 bold'), relief='flat')
botao_atualizar.place(x=110, y=320)

# Botão de Eliminar
botao_eliminar = Button(frame_baixo, text="Eliminar", bg=co7, fg=co1, font=('Ivy 10 bold'), relief='flat')
botao_eliminar.place(x=210, y=320)

lista = [[1,'Joao Futi Muanda','joao@mail.com', 933273210, 322613647, 'Praca Luis de Camoes N8'],
           [2,'Fortnato Mpngo', 'joao@mail.com', 931728499,322613647 , 'Praca Joao Vilarete N12'],
           [3,'Usando Python',  'joao@mail.com', 929374017, 322613647, 'Praceta Joa vilarete N14'],
           [4,'Clinton Berclidio', 'joao@mail.com', 931878297,322613647 , 'Praceta Joa vilarete N14', ],
           [5,'A traicao da Julieta','joao@mail.com', 922945564,322613647 , 'Praceta Joa vilarete N14']
           ]

#lista para cabecario
tabela_head = ['ID','Nome',  'email','telefone', 'Nif', 'Morada']


#criando a tabela
tree = ttk.Treeview(frame_centro, selectmode="extended", columns=tabela_head, show="headings")

#vertical scrollbar
vsb = ttk.Scrollbar(frame_centro, orient="vertical", command=tree.yview)

#horizontal scrollbar
hsb = ttk.Scrollbar( frame_centro, orient="horizontal", command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')

frame_centro.grid_rowconfigure(0, weight=12)


hd=["nw","nw","nw","nw","nw","center","center"]
h=[30,170,140,100,120,50,100]
n=0

for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
   # adjust the column's width to the header string
    tree.column(col, width=h[n],anchor=hd[n])
    
    n+=1

for item in lista:
    tree.insert('', 'end', values=item)




janela.mainloop()
