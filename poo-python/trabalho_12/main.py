import tkinter as tk
from tkinter import messagebox
import equipe

class LimitePrincipal():
    def __init__ (self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry("300x300")
        self.menubar = tk.Menu(self.root)
        self.menuEquipe = tk.Menu(self.menubar)
        self.menuCamp = tk.Menu(self.menubar)

        self.menuEquipe.add_command(label="Criar Equipe", command=self.controle.cadastrarEquipe)
        self.menuEquipe.add_command(label="Consultar Equipe", command=self.controle.consultarEquipe)
        self.menubar.add_cascade(label="Equipe", menu=self.menuEquipe)

        self.menuCamp.add_command(label="Imprimir dados", command=self.controle.imprimirDados)
        self.menubar.add_cascade(label="Campeonato", menu=self.menuCamp)

        self.menubar.add_command(label="Salvar", command=self.controle.salvar)

        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlEquipe = equipe.ctrlEquipe()

        self.limite = LimitePrincipal(self.root, self)

        self.root.title("Trabalho 12")

        self.root.mainloop()

    def cadastrarEquipe(self):
        self.ctrlEquipe.cadastraEquipe()
    
    def consultarEquipe(self):
        self.ctrlEquipe.consultarEquipe()

    def imprimirDados(self):
        self.ctrlEquipe.imprimirDados()

    def salvar(self):
        self.ctrlEquipe.salvaEquipe()

if __name__ == "__main__":
    c = ControlePrincipal()
        