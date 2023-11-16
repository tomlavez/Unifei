import tkinter as tk
from tkinter import messagebox

class Album():
    def __init__ (self, titulo, ano, artista):
        self.__titulo = titulo
        self.__ano = ano
        self.__artista = artista

        self.__listaMusicas = []

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def ano(self):
        return self.__ano

    @property
    def artista(self):
        return self.__artista

    @property
    def listaMusicas(self):
        return self.__listaMusicas
    
    @listaMusicas.setter
    def listaMusicas(self, musicas):
        self.listaMusicas = musicas
    
    def addFaixa(self, musica):
        self.__listaMusicas.append(musica)
    
class Musica():
    def __init__ (self, titulo, nroFaixa):
        self.__titulo = titulo
        self.__nroFaixa = nroFaixa

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def nroFaixa(self):
        return self.__nroFaixa

class LimiteInsereAlbum(tk.Toplevel): #Construtor da Janela
    def __init__ (self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("200x200")
        self.title("Album")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameAno.pack()
        self.frameArtista.pack()
        self.frameButton.pack()

        self.labelTitulo = tk.Label(self.frameTitulo,text="Titulo: ")
        self.inputTitulo = tk.Entry(self.frameTitulo,width=20)
        self.labelTitulo.pack(side="left")
        self.inputTitulo.pack(side="left")

        self.labelAno = tk.Label(self.frameAno,text="Ano: ")
        self.inputAno = tk.Entry(self.frameAno,width=20)
        self.labelAno.pack(side="left")
        self.inputAno.pack(side="left")

        self.labelArtista = tk.Label(self.frameArtista,text="Artista: ")
        self.inputArtista = tk.Entry(self.frameArtista,width=20)
        self.labelArtista.pack(side="left")
        self.inputArtista.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton,text="Enter")
        self.buttonClear = tk.Button(self.frameButton,text="Clear")
        self.buttonClose = tk.Button(self.frameButton,text="Concluido")
        self.buttonSubmit.pack(side="left")
        self.buttonClear.pack(side="left")
        self.buttonClose.pack(side="left")

        self.buttonSubmit.bind("<Button>", controle.submitHandler)
        self.buttonClear.bind("<Button>", controle.clearHandler)
        self.buttonClose.bind("<Button>", controle.closeHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraAlbum():
    def __init__ (self, str):
        messagebox.showinfo("Lista de albuns", str)

class LimiteInsereMusica(tk.Toplevel):
    def __init__ (self, controle):

        tk.Toplevel.__init__(self)
        self.geometry("250x100")
        self.title("Música")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameNro = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameNro.pack()
        self.frameButton.pack()

        self.labelTitulo = tk.Label(self.frameTitulo,text="Título: ")
        self.inputTitulo = tk.Entry(self.frameTitulo,width=20)
        self.labelTitulo.pack(side="left")
        self.inputTitulo.pack(side="left")

        self.labelNro = tk.Label(self.frameNro,text="Nro Faixa: ")
        self.inputNro = tk.Entry(self.frameNro,width=20)
        self.labelNro.pack(side="left")
        self.inputNro.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton,text="Enter")
        self.buttonClear = tk.Button(self.frameButton,text="Clear")
        self.buttonClose = tk.Button(self.frameButton,text="Concluido")
        self.buttonSubmit.pack(side="left")
        self.buttonClear.pack(side="left")
        self.buttonClose.pack(side="left")

        self.buttonSubmit.bind("<Button>", controle.submitHandlerM)
        self.buttonClear.bind("<Button>", controle.clearHandlerM)
        self.buttonClose.bind("<Button>", controle.closeHandlerM)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlAlbum():
    def __init__ (self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaAlbuns = []

    def insereAlbum(self):
        self.limiteIns = LimiteInsereAlbum(self)

    def mostraAlbum(self):
        str = "Albuns: \n"
        for alb in self.listaAlbuns:
            str += alb.titulo + ":\n"
            for music in alb.listaMusicas:
                str += " " + music.titulo + " - " + music.nroFaixa + "\n"
        self.limiteIns = LimiteMostraAlbum(str)

    def submitHandler(self, event):
        titulo = self.limiteIns.inputTitulo.get()
        ano = self.limiteIns.inputAno.get()
        self.artista = self.limiteIns.inputArtista.get()
        self.album = Album(titulo, ano, self.artista)
        self.listaMusicas = []
        #Criar janela pra add musicas
        self.limiteMus = LimiteInsereMusica(self)
        self.listaAlbuns.append(self.album)
        self.ctrlPrincipal.ctrlArtista.addAlbum(self.artista, self.album)
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputTitulo.delete(0, len(self.limiteIns.inputTitulo.get()))
        self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))
        self.limiteIns.inputArtista.delete(0, len(self.limiteIns.inputArtista.get()))

    def closeHandler(self, event):
        self.limiteIns.destroy()

    def submitHandlerM(self, event):
        titulo = self.limiteMus.inputTitulo.get()
        nroFaixa = self.limiteMus.inputNro.get()
        musica = Musica(titulo, nroFaixa)
        self.listaMusicas.append(musica)
        self.clearHandlerM(event)
        #feedback
        self.limiteMus.mostraJanela("Sucesso", "Musica cadastrada!")

    def clearHandlerM(self, event):
        self.limiteMus.inputTitulo.delete(0, len(self.limiteMus.inputTitulo.get()))
        self.limiteMus.inputNro.delete(0, len(self.limiteMus.inputNro.get()))

    def closeHandlerM(self, event):
        objetoArt = self.ctrlPrincipal.ctrlArtista.getArtista(self.artista)
        for mus in self.listaMusicas:
            self.album.listaMusicas.append(mus)
            objetoArt.listaMusicas.append(mus)
        self.clearHandler(event)
        self.limiteMus.destroy()
        #feedback
        self.limiteIns.mostraJanela("Sucesso", "Album cadastrado!")


