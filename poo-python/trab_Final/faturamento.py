import tkinter as tk
from tkinter import messagebox
from model import *
from datetime import date

class LimiteFatProd(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Faturamento")
        self.controle = controle

        self.frameCPF = tk.Frame(self)
        self.frameButton  = tk.Frame(self)

        self.frameCPF.pack()
        self.frameButton.pack()

        self.labelCod = tk.Label(self.frameCPF, text="Insira o código do produto: ")
        self.labelCod.pack(side="left")

        self.inputCod = tk.Entry(self.frameCPF, width=10)
        self.inputCod.pack(side="left")

        self.buttonEnter = tk.Button(self.frameButton, text="Enter")
        self.buttonEnter.pack(side="left")
        self.buttonEnter.bind("<Button>", self.controle.imprimeFatProd)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", self.controle.clearHandlerCod)


class LimiteFatCliente(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Faturamento")
        self.controle = controle

        self.frameCPF = tk.Frame(self)
        self.frameButton  = tk.Frame(self)

        self.frameCPF.pack()
        self.frameButton.pack()

        self.labelCPF = tk.Label(self.frameCPF, text="Insira o CPF do cliente: ")
        self.labelCPF.pack(side="left")

        self.inputCPF = tk.Entry(self.frameCPF, width=12)
        self.inputCPF.pack(side="left")

        self.buttonEnter = tk.Button(self.frameButton, text="Enter")
        self.buttonEnter.pack(side="left")
        self.buttonEnter.bind("<Button>", self.controle.imprimeFatCliente)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", self.controle.clearHandlerCPF)


class LimiteFatPeriodo(tk.Toplevel):
     def __init__(self, controle):
        tk.Toplevel.__init__(self)

        self.geometry('200x200')
        self.title('Adicione a data')
        self.controle = controle

        tk.Frame(self).pack(pady=20)
        self.framePeriodo = tk.Frame(self)
        self.frameData = tk.Frame(self)
        self.frameDataFinal = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.framePeriodo.pack()
        self.frameData.pack()
        self.frameDataFinal.pack()
        self.frameButton.pack()

        tk.Label(self.framePeriodo, text="Data Inicial - Data Final").pack(side="left")

        tk.Label(self.frameData, text="Dia: ").pack(side='left')
        self.inputDia = tk.Entry(self.frameData, width=3)
        self.inputDia.pack(side="left")

        tk.Label(self.frameData, text="Mês: ").pack(side='left')
        self.inputMes = tk.Entry(self.frameData, width=3)
        self.inputMes.pack(side="left")

        tk.Label(self.frameData, text="Ano: ").pack(side='left')
        self.inputAno = tk.Entry(self.frameData, width=6)
        self.inputAno.pack(side="left")

        tk.Label(self.frameDataFinal, text="Dia: ").pack(side="left")
        self.inputDiaFinal = tk.Entry(self.frameDataFinal, width=3)
        self.inputDiaFinal.pack(side="left")

        tk.Label(self.frameDataFinal, text="Mês: ").pack(side="left")
        self.inputMesFinal = tk.Entry(self.frameDataFinal, width=3)
        self.inputMesFinal.pack(side="left")

        tk.Label(self.frameDataFinal, text="Ano: ").pack(side="left")
        self.inputAnoFinal = tk.Entry(self.frameDataFinal, width=6)
        self.inputAnoFinal.pack(side="left")

        self.buttonEnter = tk.Button(self.frameButton, text="Enter")
        self.buttonClear = tk.Button(self.frameButton, text="Clear")

        self.buttonEnter.pack(side="left")
        self.buttonClear.pack(side="left")

        self.buttonEnter.bind("<Button>", self.controle.imprimiFatPeriodo)
        self.buttonClear.bind("<Button>", self.controle.clearHandlerData)

        
class CtrlFaturamento():
    def __init__(self, controlador):
        self.controlador = controlador

    def faturamentoProd(self):
        self.limiteFatProd = LimiteFatProd(self)

    def faturamentoCliente(self):
        self.limiteFatCliente = LimiteFatCliente(self)

    def faturamentoPeriodo(self):
        self.limiteFatPeriodo = LimiteFatPeriodo(self)

    def imprimeFatProd(self, event):
        text = "Faturamento do Produto:" + "\n\n"
        cod = self.limiteFatProd.inputCod.get()

        for prod in self.controlador.produtos:
            if cod == prod.codigo:
                text += "Descrição: " + prod.descricao + "\n" + "Quantidade vendida: " + str(round(prod.qtdVendida, 3)) + " " + "Kg" + "\n" + "Valor total: R$" + " " + str(round(prod.faturamento, 2))
                break
        messagebox.showinfo("Faturamento", text)
        self.clearHandlerCod(event)

    def clearHandlerCod(self, event):
        self.limiteFatProd.inputCod.delete(0, len(self.limiteFatProd.inputCod.get()))

    def imprimeFatCliente(self, event):
        fat = 0
        cpf = self.limiteFatCliente.inputCPF.get()

        for cliente in self.controlador.clientes:
            if cpf == cliente.cpf:
                for nota in cliente.compras:
                    fat += nota.calcular_valorNota()
                text = "Faturamento do Cliente: R$" + " " + str(round(fat, 2))
                break
        messagebox.showinfo("Faturamento", text)
        self.clearHandlerCPF(event)

    def clearHandlerCPF(self, event):
        self.limiteFatCliente.inputCPF.delete(0, len(self.limiteFatCliente.inputCPF.get()))

    def imprimiFatPeriodo(self, event):
        data1 = date(int(self.limiteFatPeriodo.inputAno.get()), int(self.limiteFatPeriodo.inputMes.get()), int(self.limiteFatPeriodo.inputDia.get()))
        data2 = date(int(self.limiteFatPeriodo.inputAnoFinal.get()), int(self.limiteFatPeriodo.inputMesFinal.get()), int(self.limiteFatPeriodo.inputDiaFinal.get()))

        if data1 > data2:
            messagebox.showerror("Erro", "Período Inválido")
        else:
            fat = 0
            for nota in self.controlador.vendas:
                if data1 <= nota.data and data2 >= nota.data:
                    fat += nota.calcular_valorNota()
            text = "Faturamento do Período: R$" + " " + str(round(fat, 2))
            messagebox.showinfo("Faturamento", text)

    def clearHandlerData(self, event):
        self.limiteFatPeriodo.inputDia.delete(0, len(self.limiteFatPeriodo.inputDia.get()))
        self.limiteFatPeriodo.inputMes.delete(0, len(self.limiteFatPeriodo.inputMes.get()))
        self.limiteFatPeriodo.inputAno.delete(0, len(self.limiteFatPeriodo.inputAno.get()))
        self.limiteFatPeriodo.inputDiaFinal.delete(0, len(self.limiteFatPeriodo.inputDiaFinal.get()))
        self.limiteFatPeriodo.inputMesFinal.delete(0, len(self.limiteFatPeriodo.inputMesFinal.get()))
        self.limiteFatPeriodo.inputAnoFinal.delete(0, len(self.limiteFatPeriodo.inputAnoFinal.get()))