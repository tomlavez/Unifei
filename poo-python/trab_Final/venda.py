import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import date
from model import *
from random import randrange
import nfe


class SubmitCliente(tk.Frame):
    def __init__(self,root,controle):
        tk.Frame.__init__(self,root)

        tk.Frame(self).pack(pady=20)
        self.frameCpf = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCpf.pack()
        self.frameButton.pack()

        tk.Label(self.frameCpf, text="CPF: ").pack(side='left',pady=25)
        self.inputCpf = tk.Entry(self.frameCpf, width=18)

        self.inputCpf.pack(side="left")

        self.buttonEnter = tk.Button(self.frameButton, text="Adicionar")
        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClose = tk.Button(self.frameButton, text="Concluído")

        self.buttonEnter.pack(side="left")
        self.buttonClear.pack(side="left")
        self.buttonClose.pack(side="left")

        self.buttonEnter.bind("<Button>", controle.submit_cliente)
        self.buttonClear.bind("<Button>", controle.clear_cliente)
        self.buttonClose.bind("<Button>", controle.close)


class AddProduto(tk.Frame):
    def __init__(self, root, controle, nome, lista):
        tk.Frame.__init__(self,root)

        tk.Frame(self).pack(pady=5)
        self.frameNome = tk.Frame(self)
        self.frameProduto = tk.Frame(self)
        self.frameQtd = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameButton2 = tk.Frame(self)

        tk.Label(self.frameNome, text="Cliente: " + str(nome)).pack(side='left',pady=10)
        tk.Label(self.frameProduto, text="Produto: ").pack(side='left')
        tk.Label(self.frameQtd, text='Quantidade em Kg: ').pack(side='left')

        self.inputQtd = tk.Entry(self.frameQtd,width=20)
        self.inputProduto = tk.StringVar()

        self.combo = ttk.Combobox(self.frameProduto, textvariable=self.inputProduto)
        self.combo['values'] = lista

        self.buttonAdd = tk.Button(self.frameButton, text="Adicionar Produto")
        self.buttonDel = tk.Button(self.frameButton, text="Remover Produto")
        self.buttonCancel = tk.Button(self.frameButton2, text="Cancelar Compra")
        self.buttonDone = tk.Button(self.frameButton2, text="Finalizar Compra")

        self.inputQtd.pack(side='left')
        self.combo.pack(side='left')

        self.buttonAdd.pack(side="left")
        self.buttonDel.pack(side="left")
        self.buttonCancel.pack(side="left")
        self.buttonDone.pack(side="left")


        self.frameNome.pack()
        self.frameProduto.pack(pady=2)
        self.frameQtd.pack(pady=2)
        self.frameButton.pack(pady=5)
        self.frameButton2.pack(pady=5)

        self.buttonAdd.bind('<Button>',controle.add_prod)
        self.buttonDel.bind('<Button>',controle.remove_prod)
        self.buttonCancel.bind('<Button>',controle.close)
        self.buttonDone.bind('<Button>',controle.gerar_nf)


class GerarNF(tk.Toplevel):
    def __init__(self,controle):
        tk.Toplevel.__init__(self)

        self.geometry('200x200')
        self.title('Adicione a data')

        tk.Frame(self).pack(pady=20)
        self.frameData = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameData.pack()
        self.frameButton.pack()

        tk.Label(self.frameData, text="Dia: ").pack(side='left')
        self.inputDia = tk.Entry(self.frameData, width=3)
        self.inputDia.pack(side="left")

        tk.Label(self.frameData, text="Mês: ").pack(side='left')
        self.inputMes = tk.Entry(self.frameData, width=3)
        self.inputMes.pack(side="left")

        tk.Label(self.frameData, text="Ano: ").pack(side='left')
        self.inputAno = tk.Entry(self.frameData, width=6)
        self.inputAno.pack(side="left")

        self.buttonEnter = tk.Button(self.frameButton, text="Gerar NF")
        self.buttonClose = tk.Button(self.frameButton, text="Cancelar")

        self.buttonEnter.pack(side="left")
        self.buttonClose.pack(side="left")

        self.buttonEnter.bind("<Button>", controle.gerar_nf)
        self.buttonClose.bind("<Button>", controle.cancel_nf)


class LimiteVenda(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self,controle.main.root)
        self.geometry("200x200")
        self.title("Criar Venda")
        self.controle = controle

        self.submitCliente = SubmitCliente(self,self.controle)

    def submit_cliente_view(self):
        self.submitCliente.pack()

    def add_prod(self, nome, lista):
        self.geometry('300x200')
        self.submitCliente.pack_forget()
        self.addProd = AddProduto(self, self.controle, nome, lista)
        self.addProd.pack()


class LimiteBuscarVenda(tk.Toplevel):
    def __init__(self, controle, lista):
        tk.Toplevel.__init__(self,controle.main.root)

        self.title('Buscar Venda')
        self.geometry('200x200')

        tk.Frame(self).pack(pady=20)
        self.frameCombo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCombo.pack(pady=10)
        self.frameButton.pack()

        tk.Label(self.frameCombo, text="Identificador: ",anchor=tk.W).pack(anchor='w')
        self.inputIden = tk.StringVar()

        self.combo = ttk.Combobox(self.frameCombo, textvariable=self.inputIden)
        self.combo['values'] = lista

        self.combo.pack()

        self.buttonEnter = tk.Button(self.frameButton, text="Buscar")
        self.buttonClose = tk.Button(self.frameButton, text="Cancelar")

        self.buttonEnter.pack(side="left")
        self.buttonClose.pack(side="left")

        self.buttonEnter.bind("<Button>", controle.buscar)
        self.buttonClose.bind("<Button>", controle.cancel)


class CtrlVenda():
    def __init__(self, mainCtrl):
        self.main = mainCtrl

    def inserir_venda(self):
        self.limiteVenda = LimiteVenda(self)
        self.limiteVenda.submit_cliente_view()

    def buscar_venda(self):
        lista = []

        for venda in self.main.vendas:
            lista.append(venda.identificador)

        self.limiteBusca = LimiteBuscarVenda(self,lista)

    # Limite SubmitCliente
    def submit_cliente(self, event):
        self.data = False
        temp = True
        cpf = self.limiteVenda.submitCliente.inputCpf.get()

        for cliente in self.main.clientes:
            if str(cpf) == str(cliente.cpf):
                self.clienteEscolhido = cliente
                self.listaAtt = []
                for prod in self.main.produtos:
                    self.listaAtt.append(prod.codigo)

                self.listaProdutos = []
                self.listaQtd = []
                self.limiteVenda.add_prod(cliente.nome,self.listaAtt)
                temp = False

        if temp:
            messagebox.showerror('Erro',"Cliente não encontrado, por favor cadastre-o e tente novamente!")
            self.main.addCliente()

        self.clear_cliente(event)

    def clear_cliente(self, event):
        self.limiteVenda.submitCliente.inputCpf.delete(0, tk.END)

    # Limite AddProduto
    def gerar_nf(self, event):
        if len(self.listaProdutos) != 0:
            if not self.data: ## view addProduto
                self.limiteVenda.destroy()
                self.data = True
                self.limiteData = GerarNF(self)

            else: ## view addData
                dia = int(self.limiteData.inputDia.get())
                mes = int(self.limiteData.inputMes.get())
                ano = int(self.limiteData.inputAno.get())

                while True:
                    random = randrange(1000,9999)
                    aux = True
                    for venda in self.main.vendas:
                        if random == venda.identificador:
                            aux = False
                    if aux:
                        break

                nota = NotaFiscal(self.clienteEscolhido,date(ano,mes,dia),random)

                i = 0
                for prod in self.listaProdutos:
                    nota.add_produto(prod,float(self.listaQtd[i]))
                    i+=1

                self.main.vendas.append(nota)
                print('teste')
                nfe.PrintNotaFiscal(self.main.root,nota)
                self.limiteData.destroy()

        else:
            messagebox.showerror('Erro','Deve ser adicionado pelo menos um produto para gerar a nota')

    def cancel_nf(self,event):
        self.limiteData.destroy()

    def add_prod(self, event):
        if len(self.listaProdutos) < 10:
            getProd = self.limiteVenda.addProd.inputProduto.get()
            getQtd = self.limiteVenda.addProd.inputQtd.get()


            if len(getProd) != 0 and len(getQtd):
                if float(getQtd) < 0:
                    messagebox.showerror('Erro','A quantidade deve ser positiva')
                else:
                    for prod in self.main.produtos:
                        if prod.codigo == getProd:
                            self.listaProdutos.append(prod)
                            self.listaQtd.append(getQtd)
                            messagebox.showinfo('Sucesso','Produto adicionado:'+\
                                                '\nDescrição: ' + str(prod.descricao)+\
                                                '\nPreço por Kg: ' + str(prod.precoKg))

                            self.listaAtt.pop(self.listaAtt.index(prod.codigo))
                            self.limiteVenda.addProd.combo.delete(0,tk.END)
                            self.limiteVenda.addProd.combo['values'] = self.listaAtt

                            return
                    messagebox.showerror('Erro','Não há nenhum produto registrado com esse código')

        else:
            messagebox.showerror('Erro','Podem ser adicionados até 10 produtos')

    def remove_prod(self, event):
        if len(self.listaProdutos) == 0:
            messagebox.showerror('Erro','A lista de compras já esta vazia')
            return 

        get = self.limiteVenda.addProd.inputProduto.get()

        if len(get)!=0:
            for prod in self.listaProdutos:
                if get == prod.codigo:
                    i = self.listaProdutos.index(prod)

                    self.listaProdutos.pop(i)
                    self.listaQtd.pop(i)

                    messagebox.showinfo('Remoção','O produto foi removido com sucesso')
                    return 

            messagebox.showerror('Erro','O produto não foi adicionado para ser removido')

    # Limite BuscarVenda
    def buscar(self,event):
        get = self.limiteBusca.inputIden.get()

        for venda in self.main.vendas:
            if int(venda.identificador) == int(get):
                nfe.PrintNotaFiscal(self.main.root, venda)
                return

        messagebox.showerror('Erro','Número identificador inválido')

    def cancel(self,event):
        self.limiteBusca.destroy()

    def close(self, event):
        self.limiteVenda.destroy()