import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import math
import pickle
import os.path

class Jogo():
    def __init__ (self, codigo, titulo, console, genero, preco):
        self.__codigo = codigo
        self.__titulo = titulo
        self.console = console
        self.genero = genero
        self.preco = preco

        self.__med = 0
        self.__avaliacoes = []
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def console(self):
        return self.__console
    
    @console.setter
    def console(self, valor):
        self.consoles = ["XBox", "PlayStation", "Switch", "PC"]
        if not valor in self.consoles:
            raise ValueError("Console inválido: {}".format(valor))
        else:
            self.__console = valor
    
    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, valor):
        self.generos = ["Ação", "Aventura", "Estratégia", "RPG", "Esporte", "Simulação"]
        if not valor in self.generos:
            raise ValueError("Gênero inválido: {}".format(valor))
        else:
            self.__genero = valor
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if valor <= 0 or valor > 500:
            raise ValueError("Preço inválido: {}".format(valor))
        else:
            self.__preco = valor
    
    @property
    def avaliacoes(self):
        return self.__avaliacoes
    
    @property
    def med(self):
        return self.__med

    def avaliar(self, avaliacao):
        self.__avaliacoes.append(int(avaliacao))
        self.media()

    def media(self):
        if len(self.__avaliacoes) > 0:
            media = sum(self.__avaliacoes) / len(self.__avaliacoes)
            media = math.ceil(media)
            self.__med = int(media)
        else:
            self.__med = 0

class LimiteInsereJogo(tk.Toplevel):
    def __init__ (self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("200x200")
        self.title("Insere Jogo")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameTitulo = tk.Frame(self)
        self.frameConsole = tk.Frame(self)
        self.frameGenero = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameTitulo.pack()
        self.frameConsole.pack()
        self.frameGenero.pack()
        self.framePreco.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.labelCodigo.pack(side="left")
        self.inputCodigo.pack(side="left")

        self.labelTitulo = tk.Label(self.frameTitulo, text="Título: ")
        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.labelTitulo.pack(side="left")
        self.inputTitulo.pack(side="left")

        self.labelConsole = tk.Label(self.frameConsole, text="Console: ")
        self.inputConsole = tk.Entry(self.frameConsole, width=20)
        self.labelConsole.pack(side="left")
        self.inputConsole.pack(side="left")

        self.labelGenero = tk.Label(self.frameGenero, text="Gênero: ")
        self.inputGenero = tk.Entry(self.frameGenero, width=20)
        self.labelGenero.pack(side="left")
        self.inputGenero.pack(side="left")

        self.labelPreco = tk.Label(self.framePreco, text="Preço: ")
        self.inputPreco = tk.Entry(self.framePreco, width=20)
        self.labelPreco.pack(side="left")
        self.inputPreco.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton,text="Enter")
        self.buttonClear = tk.Button(self.frameButton,text="Clear")
        self.buttonClose = tk.Button(self.frameButton,text="Concluido")
        self.buttonSubmit.pack(side="left")
        self.buttonClear.pack(side="left")
        self.buttonClose.pack(side="left")

        self.buttonSubmit.bind("<Button>", controle.InsSubmitHandler)
        self.buttonClear.bind("<Button>", controle.InsClearHandler)
        self.buttonClose.bind("<Button>", controle.InsCloseHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaJogo(tk.Toplevel):
    def __init__ (self, controle):
        
        tk.Toplevel.__init__(self)
        self.geometry = ("250x300")
        self.title = ("Avaliações")
        self.controle = controle

        self.frameAvaliacoes = tk.Frame(self)
        self.frameJogos = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameAvaliacoes.pack()
        self.frameJogos.pack()
        self.frameButton.pack()

        self.listaAvaliacoes = [1, 2, 3, 4, 5]

        self.labelAvaliacoes = tk.Label(self.frameAvaliacoes, text="Estrelas: ")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameAvaliacoes, width=15, values=self.listaAvaliacoes, textvariable=self.escolhaCombo)
        self.labelAvaliacoes.pack(side="left")
        self.combobox.pack(side="left")
        self.combobox.bind("<<ComboboxSelected>>", self.atualizaListaJogos)

        self.labelJogos = tk.Label(self.frameJogos, text="Jogos: ")
        self.jogos = tk.StringVar()
        self.listbox = tk.Listbox(self.frameJogos, listvariable=self.jogos)
        self.labelJogos.pack(side="left")
        self.listbox.pack(side="left")

        self.buttonEnter = tk.Button(self.frameButton, text="Mostrar Informações")
        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonEnter.pack(side="left")
        self.buttonFecha.pack(side="bottom")

        self.buttonFecha.bind("<Button>", controle.ConsFechaHandler)
        self.buttonEnter.bind("<Button>", controle.ConsMostraHandler)

    def atualizaListaJogos(self, event):
        lista = []
        nota = self.combobox.get()
        for x in self.controle.listaJogos:
            if x.med == int(nota):
                lista.append(x.titulo)
        self.jogos.set(lista)

    def mostraJanela(self, str):
        messagebox.showinfo("Informações", str)

class LimiteAvaliaJogo(tk.Toplevel):
    def __init__ (self, controle):
        
        tk.Toplevel.__init__(self)
        self.geometry = ("250x300")
        self.title = ("Avaliar")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameAvaliar = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameAvaliar.pack()
        self.frameButton.pack()

        self.listaAvaliacoes = [1, 2, 3, 4, 5]

        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.labelCodigo.pack(side="left")
        self.inputCodigo.pack(side="left")

        self.labelAvaliar = tk.Label(self.frameAvaliar, text="Estrelas: ")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameAvaliar, width=17, values=self.listaAvaliacoes, textvariable=self.escolhaCombo)
        self.labelAvaliar.pack(side="left")
        self.combobox.pack(side="left")

        self.enterButton = tk.Button(self.frameButton, text="Avaliar")
        self.clearButton = tk.Button(self.frameButton, text="Clear")
        self.closeButton = tk.Button(self.frameButton, text="Concluído")
        self.enterButton.pack(side="left")
        self.clearButton.pack(side="left")
        self.closeButton.pack(side="left")

        self.enterButton.bind("<Button>", controle.AvaEnterHandler)
        self.clearButton.bind("<Button>", controle.AvaClearHandler)
        self.closeButton.bind("<Button>", controle.AvaCloseHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlJogo():
    def __init__ (self):
        if not os.path.isfile("jogo.pickle"):
            self.listaJogos = []
        else:
            with open("jogo.pickle", "rb") as f:
                self.listaJogos = pickle.load(f)

    def salvaJogo(self):
        if len(self.listaJogos) != 0:
            with open("jogo.pickle","wb") as f:
                pickle.dump(self.listaJogos, f)

    def cadastraJogo(self):
        self.limiteCad = LimiteInsereJogo(self)

    def avaliaJogo(self):
        self.limiteAva = LimiteAvaliaJogo(self)

    def consultaJogo(self):
        self.limiteCons = LimiteConsultaJogo(self)

    def getListaJogos(self):
        return self.listaJogos

    def InsSubmitHandler(self, event):
        codigo = int(self.limiteCad.inputCodigo.get())
        titulo = self.limiteCad.inputTitulo.get()
        console = self.limiteCad.inputConsole.get()
        genero = self.limiteCad.inputGenero.get()
        preco = float(self.limiteCad.inputPreco.get())

        try:
            jogo = Jogo(codigo, titulo, console, genero, preco)
            self.listaJogos.append(jogo)
            self.InsClearHandler(event)
            #feedback
            self.limiteCad.mostraJanela("Sucesso", "Jogo cadastrado")
        
        except ValueError as error:
            self.limiteCad.mostraJanela("Error", error)

    def InsClearHandler(self, event):
        self.limiteCad.inputCodigo.delete(0, len(self.limiteCad.inputCodigo.get()))
        self.limiteCad.inputTitulo.delete(0, len(self.limiteCad.inputTitulo.get()))
        self.limiteCad.inputConsole.delete(0, len(self.limiteCad.inputConsole.get()))
        self.limiteCad.inputGenero.delete(0, len(self.limiteCad.inputGenero.get()))
        self.limiteCad.inputPreco.delete(0, len(self.limiteCad.inputPreco.get()))

    def InsCloseHandler(self, event):
        self.limiteCad.destroy()
    
    def AvaEnterHandler(self, event):
        codigo = int(self.limiteAva.inputCodigo.get())
        avaliacao = int(self.limiteAva.combobox.get())
        for jogo in self.listaJogos:
            if jogo.codigo == codigo:
                jogo.avaliar(avaliacao)
        self.AvaClearHandler(event)
        #feedback
        self.limiteAva.mostraJanela("Sucesso", "Jogo Avaliado")

    def AvaClearHandler(self, event):
        self.limiteAva.inputCodigo.delete(0, len(self.limiteAva.inputCodigo.get()))
        self.limiteAva.combobox.delete(0, len(self.limiteAva.combobox.get()))

    def AvaCloseHandler(self, event):
        self.limiteAva.destroy()

    def ConsFechaHandler(self, event):
        self.limiteCons.destroy()

    def ConsMostraHandler(self, event):
        titulo = self.limiteCons.listbox.get(tk.ACTIVE)
        for jogo in self.listaJogos:
            if jogo.titulo == titulo:
                str = "Código: " + "{}".format(jogo.codigo) + "\n"
                str += "Título: " + jogo.titulo + "\n"
                str += "Console: " + jogo.console + "\n"
                str += "Gênero: " + jogo.genero + "\n"
                str += "Preço: " + "R${:.2f}".format(jogo.preco) + "\n"
                self.limiteCons.mostraJanela(str)
