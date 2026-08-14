import customtkinter as ctk
import sqlite3

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')

conn =  sqlite3.connect('dados.db')
cursor = conn.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS itens(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    documento TEXT,
                    idade INTEGER,
                    telefone TEXT,
                    endereco TEXT
                    )
               ''')
conn.commit()



select_id = None

# funções
def atualizar_lista():
    for widget in scroll.winfo_children():
        widget.destroy()
    cursor.execute('SELECT  * FROM itens ORDER BY id DESC')
    for item_id, nome, documento, idade, telefone, endereco in cursor.fetchall():
        btn = ctk.CTkButton(
        scroll,
        text=(f'''
        Nome: {nome}
        Documento: {documento}
        Idade: {idade}
        Telefone: {telefone}
        Endereço: {endereco}
            '''),
        
        anchor='center',
        fg_color=('gray','gray20'),
        text_color=('black', 'white'),
        hover_color=('gray','gray30'),
        command = lambda  i = item_id , n = nome, d = documento, y = idade, t = telefone, e = endereco: selecionar(i, n, d, y, t, e)

        )
        btn.pack(fill = 'x', padx = 2)    


def selecionar(item_id, nome, documento, idade, telefone, endereco):
    global select_id
    select_id =  item_id
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')


    entry1.insert(0, nome)
    entry2.insert(0, documento)
    entry3.insert(0, idade)
    entry4.insert(0, telefone)
    entry5.insert(0, endereco)

    btn_save.configure(text = 'Atualizar')


def limpar():
    global select_id
    select_id =  None
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')
    btn_save.configure(text =  'salvar')
    

def salvar():
    txt1 =  entry1.get().strip()
    txt2 =  entry2.get().strip()
    txt3 =  entry3.get().strip()
    txt4 =  entry4.get().strip()
    txt5 =  entry5.get().strip()

    if not txt1:
        return
    if select_id:
        cursor.execute(
            "UPDATE itens SET nome = ?  WHERE id = ?", (select_id)
        ) 
    else:
        cursor.execute('INSERT INTO itens (nome, documento, idade, telefone, endereco) VALUES (?,?,?,?,?)', (txt1,txt2,txt3,txt4,txt5,))
    conn.commit()
    atualizar_lista()

    limpar()        


def excluir():
    if select_id:
        cursor.execute('DELETE FROM itens WHERE id = ? ', (select_id,))
        conn.commit()
        atualizar_lista()

        limpar()
    

# interface 
app = ctk.CTk()
app.title('CRUD COM CUSTOM TKINTER')
app.geometry('500x600')

# inputs:
nome_label = ctk.CTkLabel(app, text='Nome:')
nome_label.pack(padx= 20)
entry1 =  ctk.CTkEntry(app, placeholder_text='')
entry1.pack(padx= 20, pady=(0,5), fill= 'x')

documento_label = ctk.CTkLabel(app, text='Documento:')
documento_label.pack(padx= 20)
entry2 =  ctk.CTkEntry(app, placeholder_text='', width=150)
entry2.pack(padx= 20, pady=(0,5), )

idade_label = ctk.CTkLabel(app, text='Idade:')
idade_label.pack(padx= 20)
entry3 =  ctk.CTkEntry(app, placeholder_text='', width=50)
entry3.pack(padx= 20, pady=(0,5))

telefone_label = ctk.CTkLabel(app, text='Telefone:')
telefone_label.pack(padx= 20)
entry4 =  ctk.CTkEntry(app, placeholder_text='', width=150)
entry4.pack(padx= 20, pady=(0,5))

endereco_label = ctk.CTkLabel(app, text='Endereço:')
endereco_label.pack(padx= 20)
entry5 =  ctk.CTkEntry(app, placeholder_text='',)
entry5.pack(padx= 20, pady=(0,20), fill = 'x')

# sessão do  btn
btn_frame = ctk.CTkFrame(app, fg_color='transparent')
btn_frame.pack(padx = 20, fill = 'x')

btn_save =  ctk.CTkButton(btn_frame, text= 'salvar' , width=100, command=salvar)
btn_save.pack(side = 'left', expand = True, padx = 2)

btn_delete =  ctk.CTkButton(btn_frame, text= 'deletar', 
                            hover_color = 'yellow',
                            fg_color='red',
                            width =  100  ,                         
                            command=excluir)
btn_delete.pack(side = 'left', expand = True, padx = 2)

btn_clear  =  ctk.CTkButton(btn_frame, text='limpar',
                            hover_color = 'white',
                            fg_color='green',
                            width =  100 ,
                            border_width=2,
                            command=limpar
                            ) 

btn_clear.pack(side = 'left', expand = True, padx = 2)

scroll = ctk.CTkScrollableFrame(app)
scroll.pack(padx = 20, pady =  20, fill = 'both', expand  =  True)


atualizar_lista()

# listar .... 
app.mainloop()

