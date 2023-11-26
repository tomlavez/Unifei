import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pickle
import os.path

class Estudante():
    def __init__ (self, nroMatric, nome, curso):
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__curso = curso

    @property
    def nroMatric(self):
        return self.__nroMatric
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def curso(self):
        return self.__curso
    
class Curso():
    def __init__ (self, sigla, nome):
        self.__sigla = sigla
        self.__nome = nome

    @property
    def sigla(self):
        return self.__sigla
    
    @property
    def nome(self):
        return self.__nome
    
class Equipe():
    def __init__ (self, curso):
        self.__curso = curso

        self.__listaEstudantes = []

    @property
    def curso(self):
        return self.__curso
    
    @property
    def listaEstudantes(self):
        return self.__listaEstudantes
    
    def addEstudante(self, estudante):
        self.__listaEstudantes.append(estudante)
    
class LimiteIns(tk.Toplevel):
    def __init__ (self, controle):

        tk.Toplevel.__init__(self)
        self.geometry("300x100")
        self.title("Equipe")
        self.controle = controle

        self.frameCurso = tk.Frame(self)
        self.frameEstud = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCurso.pack()
        self.frameEstud.pack()
        self.frameButton.pack()

        self.listaCursos = self.controle.getListaCursosNome()

        self.labelCurso = tk.Label(self.frameCurso, text="Selecione o curso:")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameCurso, width=15, values=self.listaCursos, textvariable=self.escolhaCombo)
        self.labelCurso.pack(side="left")
        self.combobox.pack(side="left")

        self.labelEstud = tk.Label(self.frameEstud, text="Matricula do estudante: ")
        self.inputMatric = tk.Entry(self.frameEstud, width=20)
        self.labelEstud.pack(side="left")
        self.inputMatric.pack(side="left")

        self.buttonAdd = tk.Button(self.frameButton,text="Adicionar a equipe")
        self.buttonClear = tk.Button(self.frameButton,text="Clear")
        self.buttonCria = tk.Button(self.frameButton,text="Criar Equipe")
        self.buttonAdd.pack(side="left")
        self.buttonClear.pack(side="left")
        self.buttonCria.pack(side="left")

        self.buttonAdd.bind("<Button>", controle.InsSubmitHandler)
        self.buttonClear.bind("<Button>", controle.InsClearHandler)
        self.buttonCria.bind("<Button>", controle.InsCriaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteCons(tk.Toplevel):
    def __init__ (self, controle):

        tk.Toplevel.__init__(self)
        self.grometry = ("250x250")
        self.title = ("Equipes")
        self.controle = controle

        self.frameSigla = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameSigla.pack()
        self.frameButton.pack()

        self.labelSigla = tk.Label(self.frameSigla,text="Sigla do Curso: ")
        self.inputSigla = tk.Entry(self.frameSigla,width=20)
        self.labelSigla.pack()
        self.inputSigla.pack()

        self.buttonEnter = tk.Button(self.frameButton, text="Enter")
        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClose = tk.Button(self.frameButton, text="Concluído")
        self.buttonEnter.pack(side="left")
        self.buttonClear.pack(side="left")
        self.buttonClose.pack(side="left")

        self.buttonEnter.bind("<Button>", controle.ConsSubmitHandler)
        self.buttonClear.bind("<Button>", controle.ConsClearHandler)
        self.buttonClose.bind("<Button>", controle.ConsCloseHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ctrlEquipe():
    def __init__ (self):
        if not os.path.isfile("equipe.pickle"):
            self.listaEquipe = []
        else:
            with open("equipe.pickle", "rb") as f:
                self.listaEquipe = pickle.load(f)

        self.listaEstEquipe = []

        c1 = Curso("CCO", "Ciência da Computação")
        c2 = Curso("SIN", "Sistemas de Informação")
        c3 = Curso("EEL", "Engenharia Elétrica")
        self.listaCurso = []
        self.listaCurso.append(c1) 
        self.listaCurso.append(c2) 
        self.listaCurso.append(c3) 
        self.listaEstudante = [] 
        self.listaEstudante.append(Estudante(1001, "José da Silva", c1)) 
        self.listaEstudante.append(Estudante(1002, "João de Souza", c1))
        self.listaEstudante.append(Estudante(1003, "Jorge", c1))
        self.listaEstudante.append(Estudante(1004, "Rui Santos", c2))
        self.listaEstudante.append(Estudante(1005, "João Paulo", c2))
        self.listaEstudante.append(Estudante(1006, "Roberto", c2))
        self.listaEstudante.append(Estudante(1007, "Tigre", c2))
        self.listaEstudante.append(Estudante(1008, "Júlia Julinha", c3))
        self.listaEstudante.append(Estudante(1009, "Pedro pedra", c3))
        self.listaEstudante.append(Estudante(1010, "Maria Mariá", c3))

    def salvaEquipe(self):
        if len(self.listaEquipe) != 0:
            with open("equipe.pickle", "wb") as f:
                pickle.dump(self.listaEquipe, f)

    def cadastraEquipe(self):
        self.limiteIns = LimiteIns(self)
    
    def consultarEquipe(self):
        self.limiteCons = LimiteCons(self)

    def imprimirDados(self):
        contEquipe = 0
        contEstud = 0
        for equipe in self.listaEquipe:
            contEquipe += 1
            for aluno in equipe.listaEstudantes:
                contEstud += 1
        media = round(contEstud/contEquipe, 2)
        msg = "-Número de equipe: " + str(contEquipe) + "\n"
        msg += "-Número total de estudantes: " + str(contEstud) + "\n"
        msg += "-Média de estudante por equipe: " + str(media) + "\n"
        messagebox.showinfo("Dados do campeonato", msg)

    def getListaCursosNome(self):
        lista = []
        for curso in self.listaCurso:
            lista.append(curso.sigla)
        return lista

    def InsSubmitHandler(self, event):
        curso = self.limiteIns.combobox.get()
        matric = int(self.limiteIns.inputMatric.get())
        testeM = 0
        testeC = 0
        for estud in self.listaEstudante:
            if matric == estud.nroMatric:
                testeM = 1
                if curso == estud.curso.sigla:
                    testeC = 1
                    self.listaEstEquipe.append(estud)
        if testeM == 0:
            self.limiteIns.mostraJanela("Error", "Matrícula Inválida")
        elif testeC == 0:
            self.limiteIns.mostraJanela("Error", "Aluno não está matrículado no curso selecionado")
        else:
            self.limiteIns.mostraJanela("Sucesso", "Aluno adicionado")
        self.InsClearHandler(event)

    def InsClearHandler(self, event):
        self.limiteIns.inputMatric.delete(0, len(self.limiteIns.inputMatric.get()))

    def InsCriaHandler(self, event):
        sigla = self.limiteIns.combobox.get()
        for curso in self.listaCurso:
            if sigla == curso.sigla:
                objCurso = curso
        equipe = Equipe(objCurso)
        for estud in self.listaEstEquipe:
            equipe.addEstudante(estud)
        self.listaEquipe.append(equipe)
        self.listaEstEquipe = []
        self.limiteIns.mostraJanela("Sucesso", "Equipe criada")
        self.limiteIns.destroy()

    def ConsSubmitHandler(self, event):
        sigla = self.limiteCons.inputSigla.get()
        testeS = 0
        testeE = 0
        for curso in self.listaCurso:
            if sigla == curso.sigla:
                testeS = 1
                for equipe in self.listaEquipe:
                    if equipe.curso.sigla == sigla:
                        testeE = 1
                        self.imprimeEquipe(equipe)
        if testeS == 0:
            self.limiteCons.mostraJanela("Error", "Esta sigla de curso não existe")
        elif testeE == 0:
            self.limiteCons.mostraJanela("Error", "Não existe equipe desse curso")
        self.ConsClearHandler(event)

    def ConsClearHandler(self, event):
        self.limiteCons.inputSigla.delete(0, len(self.limiteCons.inputSigla.get()))

    def ConsCloseHandler(self, event):
        self.limiteCons.destroy()

    def imprimeEquipe(self, equipe):
        msg = "Equipe {}:\n".format(equipe.curso.sigla)
        for estud in equipe.listaEstudantes:
            msg += "Nome: {} - Matrícula: {}\n".format(estud.nome, estud.nroMatric)
        self.limiteCons.mostraJanela("Equipe", msg)

    
