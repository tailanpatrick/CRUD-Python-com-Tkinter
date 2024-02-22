from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from model.produtoDAO import ProdutoDAO
from model.produto import Produto

#variavel tree global
global tree

################# validador número ###############
def validar_entrada_preco(event):
    valor = e_preco.get()
    if not valor.replace(".", "", 1).isdigit():
        e_preco.delete(0,END)

# Mostar Frame Direita
def mostrar():
    # Tabela com valores
    global tree

    produtodao = ProdutoDAO()
    
    lista = produtodao.listar_produtos()

    # lista para cabecario
    tabela_head = ['ID Produto','Nome Produto', 'Preço Produto']


    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)


    tree.configure(yscrollcommand=vsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')


    frame_direita.grid_rowconfigure(0, weight=100)


    hd=["center","center","center"]
    h=[80,170,100,]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)
 
# função inserir
def inserir():
    nome = e_nome.get()
    preco = e_preco.get()

    if nome == '':
        messagebox.showerror('Erro', 'O nome não pode ser vazio')
    else:
        produto = Produto(nome, preco)
        produtoDao = ProdutoDAO()
        produtoDao.cadastrar_produto(produto)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

        e_nome.delete(0, END)
        e_preco.delete(0, END)
    
    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()
    

# funcao atualizar
def atualizar():
    try:
        b_inserir['state'] = DISABLED
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor = tree_lista[0]

        e_nome.delete(0, END)
        e_preco.delete(0, END)

        e_nome.insert(0, tree_lista[1])
        e_preco.insert(0, tree_lista[2])

        def update():
            nome = e_nome.get()
            preco = e_preco.get()

            if nome == '':
                messagebox.showerror('Erro', 'O nome não pode ser vazio')
            else:
                produto = Produto(nome, preco)
                produto.set_id_produto(valor)
                produtoDao = ProdutoDAO()
                produtoDao.alterar_produto(produto)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')

                e_nome.delete(0, END)
                e_preco.delete(0, END)
                b_confirmar.destroy()
            
            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar()
            b_inserir['state'] = NORMAL

        # Botão Confirmar Atualização
        b_confirmar = Button(frame_baixo, command=update, text='Confirmar Alteração', width=15,bg=co2, fg=co1, relief='raised',overrelief='ridge')
        b_confirmar.place(x=100, y=200)
        b_confirmar.destroy();
        

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados da tabela primeiro!')

# funcao deletar
def deletar():
    try:
        
        b_inserir['state'] = DISABLED
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor = tree_lista[0]

        produto = Produto(tree_lista[1], tree_lista[2])
        produto.set_id_produto(valor)
        produtoDao = ProdutoDAO()
        produtoDao.deletar_produto(produto)
        messagebox.showinfo('Sucesso', 'O dado foi deletado com sucesso!')

        for widget in frame_direita.winfo_children():
                widget.destroy()

        mostrar()
        b_inserir['state'] = NORMAL
        e_nome.delete(0, END)
        e_preco.delete(0, END)
        

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados da tabela primeiro!')

################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

################# criando janela ###############
janela = Tk()
janela.title("Cadastro de Produtos")
janela.geometry('680x281')
janela.configure(background=co9)
janela.resizable(width=False, height=False)

################# dividindo a janela ###############
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1,pady=0, sticky=NSEW)

################# label cima ###############
app_nome = Label(frame_cima, text="Cadastro de Produtos", anchor=NW, font=('Ivy 13 bold'), fg=co1, bg=co2, relief='flat')
app_nome.place(x=10, y=20)

################# configurando Frame baixo  ###############
l_nome = Label(frame_baixo, text="Nome Produto*", anchor=NW, font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
l_nome.place(x=10, y=10)

e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=15, y=40)

l_preco = Label(frame_baixo, text="Preço Produto*", anchor=NW, font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
l_preco.place(x=10, y=80)

e_preco = Entry(frame_baixo, width=15, justify='left', relief='solid')
e_preco.place(x=15, y=110)
e_preco.bind('<KeyRelease>', validar_entrada_preco)

# Botão inserir
b_inserir = Button(frame_baixo, command=inserir, text='Inserir', width=10, bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=160)

# Botão atualizar
b_atualizar = Button(frame_baixo, command=atualizar, text='Alterar', width=10, bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=105, y=160)

# Botão deletar
b_deletar = Button(frame_baixo,command=deletar,text='Deletar', width=10, bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_deletar.place(x=195, y=160)



#chamando funcao mostrar
mostrar()


janela.mainloop()