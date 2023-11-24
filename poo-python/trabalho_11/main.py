import tkinter as tk
from tkinter import messagebox
import jogo
import math

class LimitePrincipal():
    def __init__(self, root, controle):
        self.root = root
        self.controle = controle
        self.root.geometry("300x300")
        self.menubar = tk.Menu(self.root)
        self.jogoMenu = tk.Menu(self.menubar)

        self.jogoMenu.add_command(label="Cadastrar", command=self.controle.cadastraJogo)
        self.jogoMenu.add_command(label="Consultar", command=self.controle.consultaJogo)
        self.jogoMenu.add_command(label="Avaliar", command=self.controle.avaliaJogo)
        self.jogoMenu.add_command(label="Salvar", command=self.controle.salvaJogo)
        self.menubar.add_cascade(label="Jogo", menu=self.jogoMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlJogo = jogo.CtrlJogo()

        self.limite = LimitePrincipal(self.root, self)

        self.root.title("Trabalho 11")

        self.root.mainloop()

    def cadastraJogo(self):
        self.ctrlJogo.cadastraJogo()

    def consultaJogo(self):
        self.ctrlJogo.consultaJogo()

    def avaliaJogo(self):
        self.ctrlJogo.avaliaJogo()

    def salvaJogo(self):
        self.ctrlJogo.salvaJogo()

if __name__ == "__main__":
    c = ControlePrincipal()