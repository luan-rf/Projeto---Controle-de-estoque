from tkinter import *
import sqlite3
import tkinter.messagebox


# ------------------ FUNÇÕES DO BANCO DE DADOS
def conectar():
    """Abre a conexão com o banco de dados já criado."""
    return sqlite3.connect(r'db\estoque.db')


def inserir_insumo(nome, validade, lote, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        '''
        INSERT INTO EstoqueMentoria (nome_insumo, data_validade, lote, quantidade)
        VALUES(?, ?, ?, ?)''', (nome, validade, lote, quantidade)
    )
    conexao.commit()
    conexao.close()
    print(f"Insumo '{nome}' cadastrado com sucesso!")


def consumir_item(nome, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        '''
        UPDATE EstoqueMentoria
        SET quantidade = quantidade - ?
        WHERE nome_insumo = ?
        ''', (quantidade, nome)
    )
    conexao.commit()
    conexao.close()
    print(f"Quantidade do item {nome} foi atualizada com sucesso.")


def excluir_estoque(produto):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        DELETE from EstoqueMentoria
        WHERE nome_insumo = ?
    ''', (produto,))
    conexao.commit()
    conexao.close()
    print(f"Item {produto} foi excluido da base com sucesso.")


def buscar_produto(produto):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT * FROM EstoqueMentoria
        WHERE nome_insumo = ?
    ''', (produto,))
    resultados = cursor.fetchall()
    conexao.close()
    return resultados


# ------------------ FUNÇÕES PARA OS BOTÕES DO PROGRAMA

def btn_clicked1():  # Procurar insumo
    nome_produto = entry1.get().strip().upper()
    entry0.delete("1.0", END)  # Limpa a caixa de texto antes de inserir novo resultado

    if not nome_produto:
        tkinter.messagebox.showwarning(title="Aviso", message="Preencha o nome do insumo para pesquisar.")
        return

    dados = buscar_produto(produto=nome_produto)

    if dados:
        nome = dados[0][1]
        lote = dados[0][3]
        quantidade = dados[0][4]
        texto = f"Item: {nome}\nQuantidade: {quantidade}\nLote: {lote}"
        entry0.insert("1.0", texto)
    else:
        entry0.insert("1.0", "Insumo não encontrado na base de dados.")


def btn_clicked2():  # Deletar insumo
    nome_produto = entry1.get().strip().upper()

    if not nome_produto:
        tkinter.messagebox.showwarning(title="Aviso", message="Preencha o nome do insumo que deseja deletar.")
        return

    dados = buscar_produto(produto=nome_produto)
    if not dados:
        tkinter.messagebox.showerror(title="Erro", message=f"O item '{nome_produto}' não existe no banco de dados.")
        return

    excluir_estoque(produto=nome_produto)
    tkinter.messagebox.showinfo(title="Aviso Exclusão de Item",
                                message=f"Item '{nome_produto}' foi excluido da base com sucesso.")


def btn_clicked3():  # Registrar uso de insumo
    nome_produto = entry1.get().strip().upper()
    qtd_usada = entry4.get().strip()

    if not nome_produto or not qtd_usada:
        tkinter.messagebox.showwarning(title="Aviso", message="Preencha o NOME e a QUANTIDADE para registrar uso.")
        return

    if not qtd_usada.isdigit() or int(qtd_usada) <= 0:
        tkinter.messagebox.showerror(title="Erro",
                                     message="A quantidade a ser consumida deve ser um número inteiro e maior que zero.")
        return

    dados = buscar_produto(produto=nome_produto)
    if not dados:
        tkinter.messagebox.showerror(title="Erro", message=f"O item '{nome_produto}' não existe no banco de dados.")
        return

    estoque_atual = dados[0][4]
    if int(qtd_usada) > estoque_atual:
        tkinter.messagebox.showerror(title="Erro",
                                     message=f"Quantidade insuficiente! Estoque atual de {nome_produto} é {estoque_atual}.")
        return

    consumir_item(nome=nome_produto, quantidade=int(qtd_usada))
    tkinter.messagebox.showinfo(title="Consumo Registrado",
                                message=f"Uso registrado! Estoque de '{nome_produto}' atualizado.")


def btn_clicked4():  # Adicionar insumo
    nome_insumo = entry1.get().strip().upper()
    data_validade = entry2.get().strip()
    lote = entry3.get().strip()
    quantidade = entry4.get().strip()

    # Verifica se todos os campos foram preenchidos
    if not all([nome_insumo, data_validade, lote, quantidade]):
        tkinter.messagebox.showwarning(title="Aviso", message="Preencha todos os campos para adicionar o insumo.")
        return

    # Verifica se a quantidade é um número válido
    if not quantidade.isdigit() or int(quantidade) < 0:
        tkinter.messagebox.showerror(title="Erro", message="A quantidade deve ser um número inteiro válido.")
        return

    dados = buscar_produto(nome_insumo)
    if dados:
        tkinter.messagebox.showerror(title="Erro - Adicionar Itens",
                                     message="Já existe um produto com este nome na base. Evite duplicidades.")
    else:
        inserir_insumo(nome=nome_insumo, validade=data_validade, lote=lote, quantidade=int(quantidade))
        tkinter.messagebox.showinfo(title="Sucesso", message=f"O item '{nome_insumo}' foi adicionado com sucesso.")


# ------------------ INICIO DO TKINTER (TELA DO SISTEMA)
window = Tk()
window.geometry("711x646")
window.configure(bg="#ffffff")
window.title("Sistema de Gestão de Estoque")

canvas = Canvas(
    window,
    bg="#ffffff",
    height=646,
    width=711,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

try:
    background_img = PhotoImage(file="background.png")
    background = canvas.create_image(355.5, 323.0, image=background_img)

    img0 = PhotoImage(file="img0.png")
    b0 = Button(image=img0, borderwidth=0, highlightthickness=0, command=btn_clicked1, relief="flat")
    b0.place(x=479, y=195, width=178, height=38)

    img1 = PhotoImage(file="img1.png")
    b1 = Button(image=img1, borderwidth=0, highlightthickness=0, command=btn_clicked2, relief="flat")
    b1.place(x=247, y=197, width=178, height=36)

    img2 = PhotoImage(file="img2.png")
    b2 = Button(image=img2, borderwidth=0, highlightthickness=0, command=btn_clicked3, relief="flat")
    b2.place(x=479, y=123, width=178, height=35)

    img3 = PhotoImage(file="img3.png")
    b3 = Button(image=img3, borderwidth=0, highlightthickness=0, command=btn_clicked4, relief="flat")
    b3.place(x=247, y=125, width=178, height=34)

    entry0_img = PhotoImage(file="img_textBox0.png")
    entry0_bg = canvas.create_image(455.0, 560.0, image=entry0_img)
    entry0 = Text(bd=0, bg="#ffffff", highlightthickness=0)
    entry0.place(x=250, y=502, width=410, height=114)

    entry1_img = PhotoImage(file="img_textBox1.png")
    entry1_bg = canvas.create_image(517.0, 294.5, image=entry1_img)
    entry1 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
    entry1.place(x=377, y=278, width=280, height=31)

    entry2_img = PhotoImage(file="img_textBox2.png")
    entry2_bg = canvas.create_image(517.0, 340.5, image=entry2_img)
    entry2 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
    entry2.place(x=377, y=324, width=280, height=31)

    entry3_img = PhotoImage(file="img_textBox3.png")
    entry3_bg = canvas.create_image(517.0, 388.5, image=entry3_img)
    entry3 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
    entry3.place(x=377, y=372, width=280, height=31)

    entry4_img = PhotoImage(file="img_textBox4.png")
    entry4_bg = canvas.create_image(517.0, 436.5, image=entry4_img)
    entry4 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
    entry4.place(x=377, y=420, width=280, height=31)

except TclError as e:
    print(
        f"Aviso: Não foi possível carregar as imagens da interface. Certifique-se de que estão na mesma pasta do script. Erro: {e}")

window.resizable(False, False)
window.mainloop()