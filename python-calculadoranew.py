from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json

arquivo_json = 'dados_agenda.json'

# Cores
co0 = "#feffff"  # Branca
co1 = "#f0f3f5"  # cizenta / grey
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # preta / black
co4 = "#403d3d"  # letra / letters
co5 = "#38576b"  # azul / blue
co6 = "#bc8f8f"  # marrom rosado / brown pink

# Criando janela de Login
janela_login = Tk()
janela_login.title("Login")
janela_login.geometry("310x300")
janela_login.configure(background=co1)
janela_login.resizable(width=FALSE, height=FALSE)

agenda = {}

atualizar_estado = False

# Dividindo a janela
Frame_cima = Frame(janela_login, width=310, height=50, bg=co1, relief='flat')
Frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

Frame_baixo = Frame(janela_login, width=310, height=250, bg=co1, relief='flat')
Frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configurando o frame cima
l_nome = Label(Frame_cima, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = Label(Frame_cima, text='', width=275,  anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
l_linha.place(x=10, y=45)

credenciais = ['David', '123456789']

# Função para verificar senha
def verificar_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem-vindo!!!')
        janela_login.destroy()  # Fecha a janela de login
        nova_janela()  # Abre a nova janela
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem-vindo!!! ' + credenciais[0])
        janela_login.destroy()  # Fecha a janela de login
        nova_janela()  # Abre a nova janela

        # Deletar itens presentes no frame baixo e cima    
        for widget in Frame_baixo.winfo_children():
            widget.destroy()
   
        for widget in Frame_cima.winfo_children():
            widget.destroy()

        nova_janela()
         
    else:
        messagebox.showwarning('Erro', 'Verifique o nome e a senha !!!')

# Configurando o frame baixo
l_nome = Label(Frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(Frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=14, y=50)

l_pass = Label(Frame_baixo, text='Senha *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(Frame_baixo, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
e_pass.place(x=14, y=130)

b_confirmar = Button(Frame_baixo, command=verificar_senha, text='Entrar', width=39, height=2, font=('Ivy 8 bold'), bg=co5, fg=co0, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15, y=180)


# Função da nova janela
def nova_janela():
    janela_agenda = Tk()
    janela_agenda.title("Agenda Telefônica")
    janela_agenda.geometry('450x500')
    janela_agenda.configure(background=co1)
    janela_agenda.resizable(width=FALSE, height=FALSE)

    # Frames
    frame_cima = Frame(janela_agenda, width=450, height=50, bg=co3, relief="flat")
    frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    frame_baixo = Frame(janela_agenda, width=450, height=200, bg=co0, relief="flat")
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    frame_tabela = Frame(janela_agenda, width=450, height=248, bg=co1, relief="flat")
    frame_tabela.grid(row=2, column=0, columnspan=2, padx=10, pady=1, sticky=NW)

    # Configurando Frame Cima
    nome1 = Label(frame_cima, text='Agenda Telefônica', anchor=NE, font=('arial 20 bold'), bg=co3, fg=co1)
    nome1.place(x=5, y=5)

    linha1 = Label(frame_cima, text='', width=450, anchor=NE, font=('arial 1'), bg=co2, fg=co1)
    linha1.place(x=0, y=45)

    # Configurando Frame Baixo
    Label(frame_baixo, text='Nome:', anchor=NW, font=('Ivy 10'), bg=co0, fg=co4).place(x=10, y=20)
    e_nome_agenda = Entry(frame_baixo, width=25, justify='left', font=('', 10), highlightthickness=1)
    e_nome_agenda.place(x=100, y=20)

    Label(frame_baixo, text='Sobrenome:', anchor=NW, font=('Ivy 10'), bg=co0, fg=co4).place(x=9, y=50)
    e_sobre_nome = Entry(frame_baixo, width=25, justify='left', font=('', 10), highlightthickness=1)
    e_sobre_nome.place(x=100, y=50)

    Label(frame_baixo, text='Sexo:', anchor=NW, font=('Ivy 10'), bg=co0, fg=co4).place(x=10, y=80)
    c_sexo = ttk.Combobox(frame_baixo, width=25)
    c_sexo['values'] = ('', 'F', 'M')
    c_sexo.place(x=100, y=80)

    Label(frame_baixo, text='Telefone:', anchor=NW, font=('Ivy 10'), bg=co0, fg=co4).place(x=10, y=110)
    e_tel = Entry(frame_baixo, width=25, justify='left', font=('', 10), highlightthickness=1)
    e_tel.place(x=100, y=110)

    Label(frame_baixo, text='E-mail:', anchor=NW, font=('Ivy 10'), bg=co0, fg=co4).place(x=10, y=140)
    e_email = Entry(frame_baixo, width=25, justify='left', font=('', 10), highlightthickness=1)
    e_email.place(x=100, y=140)
    
    
    Label(frame_baixo, text='Linkedin:', anchor=NW, font=('Ivy 10'), bg=co0, fg=co6).place(x=10, y=140)
    e_email = Entry(frame_baixo, width=30, justify='left', font=('', 10), highlightthickness=1)
    e_email.place(x=100, y=140)

    # Função para salvar os dados em um arquivo JSON
    def salvar_dados_json():
        dados = []
        for linha_id in tree.get_children():
            linha = tree.item(linha_id)['values']
            dados.append({
                'nome': linha[0],
                'sobrenome': linha[1],
                'sexo': linha[2],
                'telefone': linha[3],
                'email': linha[4]
            })

        with open(arquivo_json, 'w', encoding='utf-8') as file:
            json.dump(dados, file, ensure_ascii=False, indent=4)

    # Função para carregar os dados do arquivo JSON
    def carregar_dados_json():
        try:
            with open(arquivo_json, 'r', encoding='utf-8') as file:
                dados = json.load(file)
                for item in dados:
                    tree.insert('', 'end', values=(item['nome'], item['sobrenome'], item['sexo'], item['telefone'], item['email']))
        except FileNotFoundError:
            pass

    # Função para salvar contato
    def salvar_contato():
        nome = e_nome_agenda.get()
        sobrenome = e_sobre_nome.get()
        sexo = c_sexo.get()
        telefone = e_tel.get()
        email = e_email.get()
    
        if nome and sobrenome and sexo and telefone and email:
            messagebox.showinfo('Sucesso', 'Contato salvo com sucesso!')
            # Aqui você pode adicionar o código para salvar o contato em uma lista ou banco de dados
        else:
            messagebox.showwarning('Erro', 'Por favor, preencha todos os campos!')


    # Função para adicionar contato
    def adicionar():
        global agenda
        nome = e_nome_agenda.get()
        sobre_nome = e_sobre_nome.get()
        sexo = c_sexo.get()
        telefone = e_tel.get()
        email = e_email.get()

        if nome and sobre_nome and sexo and telefone and email:
            tree.insert('', 'end', values=(nome, sobre_nome, sexo, telefone, email))
            salvar_dados_json()  # Salva os dados após adicionar

            messagebox.showinfo("Adicionar", "Dados adicionados com sucesso!")

            e_nome_agenda.delete(0, END)
            e_sobre_nome.delete(0, END)
            c_sexo.set('')
            e_tel.delete(0, END)
            e_email.delete(0, END)

        else:
            messagebox.showwarning('Erro', 'Por favor, preencha todos os campos')
    

    def atualizar():
        global atualizar_estado
        if not atualizar_estado:
            try:
                item_selecionado = tree.selection()[0]
                valores = tree.item(item_selecionado, 'values')

                e_nome_agenda.delete(0, END)
                e_nome.insert(0, valores[0])

                e_sobre_nome.delete(0, END)
                e_sobre_nome.insert(0, valores[1])

                c_sexo.set(valores[2])

                e_tel.delete(0, END)
                e_tel.insert(0, valores[3])

                e_email.delete(0, END)
                e_email.insert(0, valores[4])
                
                linkedin.delete(0, END)
                linkedin.insert(0, valores[4])


                messagebox.showinfo("Atualizar", "Dados carregados. Agora edite e clique em 'Atualizar' novamente para salvar.")

                atualizar_estado = True

            except IndexError:
                messagebox.showwarning("Erro", "Nenhum item foi selecionado para atualizar.")

        else:
            try:
                item_selecionado = tree.selection()[0]

                novo_nome = e_nome_agenda.get()
                novo_sobrenome = e_sobre_nome.get()
                novo_sexo = c_sexo.get()
                novo_telefone = e_tel.get()
                novo_email = e_email.get()

                if novo_nome and novo_sobrenome and novo_sexo and novo_telefone and novo_email:
                    tree.item(item_selecionado, values=(novo_nome, novo_sobrenome, novo_sexo, novo_telefone, novo_email))

                    salvar_dados_json()  # Salva os dados após atualizar

                    messagebox.showinfo("Sucesso", "Dados atualizados com sucesso!")

                    e_nome.delete(0, END)
                    e_sobre_nome.delete(0, END)
                    c_sexo.set('')
                    e_tel.delete(0, END)
                    e_email.delete(0, END)

                    atualizar_estado = False

                else:
                    messagebox.showwarning("Erro", "Preencha todos os campos!")

            except IndexError:
                messagebox.showwarning("Erro", "Nenhum item selecionado para salvar.")



    def deletar():
        try:
            # Seleciona o item que está selecionado na tabela
            item_selecionado = tree.selection()[0]
            tree.delete(item_selecionado)

            # Salva os dados restantes no JSON
            salvar_dados_json()

            messagebox.showinfo("Deletar", "Dados deletados com sucesso!")

        except IndexError:
            messagebox.showwarning("Erro", "Nenhum item foi selecionado para deletar.")


    # Botão Adicionar
    b_adicionar = Button(frame_baixo, command=adicionar, text="Adicionar", width=15, height=0, bg=co0, fg=co4, font=("Ivy 8 bold"), relief=RAISED, overrelief=RIDGE)
    b_adicionar.place(x=300, y=20)

    # Botão Atualizar
    b_atualizar = Button(frame_baixo, command=atualizar, text="Atualizar", width=15, height=0, bg=co0, fg=co4, font=("Ivy 8 bold"), relief=RAISED, overrelief=RIDGE)
    b_atualizar.place(x=300, y=80)

    # Botão Deletar
    b_deletar = Button(frame_baixo, command=deletar, text="Deletar", width=15, height=1, bg=co0, fg=co4, font=("Ivy 8 bold"), relief=RAISED, overrelief=RIDGE)
    b_deletar.place(x=300, y=140)


    # Configurando Frame Tabela
    dados_h = ['Nome', 'Sobre Nome', 'Sexo', 'Telefone', 'E-mail' , 'Linkedin']

    tree = ttk.Treeview(frame_tabela, selectmode="extended",columns=dados_h, show="headings")

    
    # Vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
    # Horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')


    # Tree Cabeçalho
    tree.heading(0,text='Nome', anchor=NW)
    tree.heading(1,text='Sobre Nome', anchor=NW)
    tree.heading(2,text='Sexo', anchor=NW)
    tree.heading(3,text='Telefone', anchor=NW)
    tree.heading(4,text='E-mail', anchor=NW)
    tree.heading(5,text='Linkedin', anchor=NW)

    # Tree Corpo
    tree.column(0, width=80,anchor='nw')
    tree.column(1, width=100,anchor='nw')
    tree.column(2, width=50,anchor='nw')
    tree.column(3, width=95,anchor='nw')
    tree.column(4, width=100,anchor='nw')

    
    # Carregar dados do arquivo JSON ao abrir a janela
    carregar_dados_json()

    janela_agenda.mainloop()

janela_login.mainloop()