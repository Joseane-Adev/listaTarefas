import tkinter as tk
from tkinter import messagebox
import os

lista = []
def adicionaTarefa():
    tarefa = entrada.get().capitalize()
    if tarefa:
        lista.append(tarefa)
        entrada.delete(0,tk.END)
    else:
        messagebox.showwarning("Aviso", "Escreva uma tarefa antes de adicionar!")

#listar a tarefa
def listarTarefa():
    #mostrar a lista
    for item in lista:
        listaBox.insert(tk.END, item)

        
# remover uma tarefa
def removerTarefa():
    #mostrar a lista e depois escolher qual quer apagar
    escolha = listaBox.curselection()
    if escolha:
        indice = escolha[0]
        tarefa_removida = lista[indice]
        del lista[indice]
        listaBox.delete(indice)
        messagebox.showinfo("Removido com sucesso!", f"Removido da lista: {tarefa_removida}")
    else:
        # mensagem de aviso correta
        messagebox.showwarning("Aviso", "Clique em cima da tarefa a ser removida!")
    
#sair
def sair():
    janela.destroy()

janela = tk.Tk()
janela.title('LISTA DE TAREFAS')

entrada = tk.Entry(janela, width=50)
entrada.pack(pady=10)

btnAdd = tk.Button(janela, text="Adicionar tarefa", command=adicionaTarefa)
btnAdd.pack(pady=5)

btnListar = tk.Button(janela, text="Listar tarefa", command=listarTarefa)
btnListar.pack(pady=5)

btnRemove = tk.Button(janela, text="Remover tarefa", command=removerTarefa)
btnRemove.pack(pady=5)

btnSair = tk.Button(janela, text="Sair", command=sair)
btnSair.pack(pady=5)

listaBox = tk.Listbox(janela, width=50, height=10)
listaBox.pack(pady=10)

janela.mainloop()


