import sqlite3
import tkinter as tk
from tkinter import messagebox

def criar_tabela_alunos():
    conexao = sqlite3.connect('alunos.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            curso TEXT NOT NULL
        )
    ''')

    conexao.commit()
    conexao.close()

def cadastrar_aluno():
    nome = entry_nome.get()
    email = entry_email.get()
    curso = entry_curso.get()

    if nome and email and curso:
        conexao = sqlite3.connect('alunos.db')
        cursor = conexao.cursor()

        cursor.execute('INSERT INTO alunos (nome, email, curso) VALUES (?, ?, ?)', (nome, email, curso))

        conexao.commit()
        conexao.close()

        messagebox.showinfo("Cadastro de Aluno", "Aluno cadastrado com sucesso.")
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_curso.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Preencha todos os campos.")

def listar_alunos():
    conexao = sqlite3.connect('alunos.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM alunos')
    alunos = cursor.fetchall()

    conexao.close()

    if alunos:
        aluno_listbox.delete(0, tk.END)
        for aluno in alunos:
            aluno_listbox.insert(tk.END, f"ID: {aluno[0]}, Nome: {aluno[1]}, Email: {aluno[2]}, Curso: {aluno[3]}")
    else:
        aluno_listbox.delete(0, tk.END)
        aluno_listbox.insert(tk.END, "Nenhum aluno cadastrado ainda.")

def buscar_aluno_por_nome():
    nome_busca = entry_busca_nome.get()

    conexao = sqlite3.connect('alunos.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM alunos WHERE nome LIKE ?', (f'%{nome_busca}%',))
    alunos = cursor.fetchall()

    conexao.close()

    if alunos:
        aluno_listbox.delete(0, tk.END)
        for aluno in alunos:
            aluno_listbox.insert(tk.END, f"ID: {aluno[0]}, Nome: {aluno[1]}, Email: {aluno[2]}, Curso: {aluno[3]}")
    else:
        messagebox.showinfo("Busca de Aluno", f"Nenhum aluno com o nome '{nome_busca}' encontrado.")
        aluno_listbox.delete(0, tk.END)

def sair():
    root.destroy()

root = tk.Tk()
root.title("Gerenciamento de Alunos")

frame_cadastro = tk.Frame(root)
frame_cadastro.pack(pady=10)

label_nome = tk.Label(frame_cadastro, text="Nome:")
label_nome.grid(row=0, column=0)
entry_nome = tk.Entry(frame_cadastro)
entry_nome.grid(row=0, column=1)

label_email = tk.Label(frame_cadastro, text="Email:")
label_email.grid(row=1, column=0)
entry_email = tk.Entry(frame_cadastro)
entry_email.grid(row=1, column=1)

label_curso = tk.Label(frame_cadastro, text="Curso:")
label_curso.grid(row=2, column=0)
entry_curso = tk.Entry(frame_cadastro)
entry_curso.grid(row=2, column=1)

button_cadastrar = tk.Button(frame_cadastro, text="Cadastrar Aluno", command=cadastrar_aluno)
button_cadastrar.grid(row=3, columnspan=2)

frame_busca = tk.Frame(root)
frame_busca.pack(pady=10)

label_busca_nome = tk.Label(frame_busca, text="Buscar por Nome:")
label_busca_nome.grid(row=0, column=0)
entry_busca_nome = tk.Entry(frame_busca)
entry_busca_nome.grid(row=0, column=1)

button_buscar = tk.Button(frame_busca, text="Buscar Aluno", command=buscar_aluno_por_nome)
button_buscar.grid(row=0, column=2)

frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

aluno_listbox = tk.Listbox(frame_lista, width=40)
aluno_listbox.pack()

button_listar = tk.Button(frame_lista, text="Listar Alunos", command=listar_alunos)
button_listar.pack()

frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=10)

button_sair = tk.Button(frame_botoes, text="Sair", command=sair)
button_sair.pack()

criar_tabela_alunos()

root.mainloop()
