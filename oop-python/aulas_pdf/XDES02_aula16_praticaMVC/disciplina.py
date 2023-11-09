import tkinter as tk
from tkinter import messagebox

class Disciplina:
    
    def __init__ (self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome
    
class LimiteInsereDisciplinas(tk.Toplevel):
    def __init__(self, controle):
    #Construtor da Janela
        #Especificações da janela
        tk.Toplevel.__init__(self)
        self.geometry("300x300")
        self.title("Disciplina")
        self.controle = controle

        #Criação dos containers
        self.frameCodigo = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameButton.pack()

        #Criando container codigo
        self.labelCodigo = tk.Label(self.frameCodigo,text="Código: ")
        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.labelCodigo.pack(side="left")
        self.inputCodigo.pack(side="left")

        #Criando container nome
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.labelNome.pack(side="left")
        self.inputNome.pack(side="left")

        #Criando container button
        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClose = tk.Button(self.frameButton, text="Concluído")
        self.buttonSubmit.pack(side="left")
        self.buttonClear.pack(side="left")
        self.buttonClose.pack(side="left")

        #Bindando button
        self.buttonSubmit.bind("<Button>", controle.submitHandler)
        self.buttonClear.bind("<Button>", controle.clearHandler)
        self.buttonClose.bind("<Button>", controle.closeHandler)

    #Função para dar feedback ao usuário
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraDisciplinas():
    def __init__ (self, str):
        messagebox.showinfo("Lista de Disciplinas", str)

class CtrlDisciplina(): #Controle da Janela
    def __init__(self):
        self.listaDisciplinas = []

    def insereDisciplina(self):
        self.limiteIns = LimiteInsereDisciplinas(self)

    def mostraDisciplinas(self):
        str = "Código --- Nome\n"
        for disc in self.listaDisciplinas:
            str += disc.codigo + " --- " + disc.nome + "\n"
        self.limiteLista = LimiteMostraDisciplinas(str)

    #Funções dos botões
    def submitHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get()
        disciplina = Disciplina(codigo, nome)
        self.listaDisciplinas.append(disciplina)
        self.limiteIns.mostraJanela("Sucesso", "Disciplina cadastrada com sucesso!")
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def closeHandler(self, event):
        self.limiteIns.destroy()