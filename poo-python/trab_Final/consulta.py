from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date


class SubmitCliente(Frame):
    def __init__(self,root,controle,lista):
        Frame.__init__(self,root)


        Frame(self).pack(pady=10)
        self._frameCliente = Frame(self)
        self._frameButton = Frame(self)

        Label(self._frameCliente, text="Cliente: ",pady=10).pack(anchor=W)

        self.inputCliente = StringVar()

        self._combo = ttk.Combobox(self._frameCliente,width=18,textvariable=self.inputCliente)
        self._combo['values'] = lista
        self._combo.pack()

        self._buttonEnter = Button(self._frameButton, text='Enter')
        self._buttonClose = Button(self._frameButton, text='Fechar')

        self._buttonEnter.pack(side='right',padx=2)
        self._buttonClose.pack(side='right',padx=2)

        self._buttonEnter.bind("<Button>", controle.submit_cliente)
        self._buttonClose.bind("<Button>", controle.close)

        self._frameCliente.pack(fill=X)
        self._frameButton.pack(fill=X,pady=15)



class SubmitData(Frame):
    def __init__(self,root,controle):
        Frame.__init__(self,root)

        Frame(self).pack(pady=10)
        self.frameData1 = Frame(self)
        self.frameData2 = Frame(self)
        self.frameButton = Frame(self)

        Label(self,text='Início',anchor=W,font=('Arial',9,'bold')).pack(fill=X,padx=1)

        Label(self.frameData1, text="Dia: ").pack(side='left')
        self.inputDia1 = Entry(self.frameData1, width=3)
        self.inputDia1.pack(side="left")

        Label(self.frameData1, text="Mês: ").pack(side='left')
        self.inputMes1 = Entry(self.frameData1, width=3)
        self.inputMes1.pack(side="left")

        Label(self.frameData1, text="Ano: ").pack(side='left')
        self.inputAno1 = Entry(self.frameData1, width=6)
        self.inputAno1.pack(side="left")

        self.frameData1.pack()

        Label(self,height=1).pack(pady=1)

        Label(self,text='Fim',anchor=W,font=('Arial',9,'bold')).pack(fill=X,padx=1)

        Label(self.frameData2, text="Dia: ").pack(side='left')
        self.inputDia2 = Entry(self.frameData2, width=3)
        self.inputDia2.pack(side="left")

        Label(self.frameData2, text="Mês: ").pack(side='left')
        self.inputMes2 = Entry(self.frameData2, width=3)
        self.inputMes2.pack(side="left")

        Label(self.frameData2, text="Ano: ").pack(side='left')
        self.inputAno2 = Entry(self.frameData2, width=6)
        self.inputAno2.pack(side="left")

        self.frameData2.pack()

        Label(self,height=1).pack(pady=1)

        self.buttonEnter = Button(self.frameButton, text="Enter")
        self.buttonClose = Button(self.frameButton, text="Fechar")

        self.buttonClose.pack(side="left",padx=1)
        self.buttonEnter.pack(side="left",padx=1)

        self.buttonEnter.bind("<Button>", controle.submit_periodo)
        self.buttonClose.bind("<Button>", controle.close)

        self.frameButton.pack(pady=10)



class ViewVendasPeriodo(Toplevel):
    def __init__(self, controller):
        Toplevel.__init__(self)
        self.ctrl = controller

        self.title('Vendas por período')
        self.geometry('200x200')
        self.resizable(False,False)

    def cliente(self,lista):
        self.submitCliente = SubmitCliente(self,self.ctrl,lista)
        self.submitCliente.pack(fill=X,padx=32)

    def periodo(self):
        self.submitCliente.pack_forget()
        self.submitData = SubmitData(self,self.ctrl)
        self.submitData.pack()



class CtrlConsulta:
    def __init__(self,mainCtrl):
        self._main = mainCtrl

    def vendas_periodo(self):
        self._viewVendas = ViewVendasPeriodo(self)
        lista = []

        for cli in self._main.clientes:
            lista.append(cli.nome)

        self._viewVendas.cliente(lista)

    def submit_periodo(self,event):
        dia = int(self._viewVendas.submitData.inputDia1.get())
        mes = int(self._viewVendas.submitData.inputMes1.get())
        ano = int(self._viewVendas.submitData.inputAno1.get())

        data1 = date(ano,mes,dia)

        dia = int(self._viewVendas.submitData.inputDia2.get())
        mes = int(self._viewVendas.submitData.inputMes2.get())
        ano = int(self._viewVendas.submitData.inputAno2.get())

        data2 = date(ano,mes,dia)

        if data2 < data1:
            self._viewVendas.submitData.inputDia2.delete(0,END)
            self._viewVendas.submitData.inputMes2.delete(0,END)
            self._viewVendas.submitData.inputAno2.delete(0,END)

            messagebox.showerror('Erro','A data final do período deve ser posterior à inicial')

        else:
            text = 'Notas fiscais:\nPeríodo:'
            text += str(data1.day) + ' / ' + str(data1.month) + ' / ' + str(data1.year) + '  -  '
            text += str(data2.day) + ' / ' + str(data2.month) + ' / ' + str(data2.year) + '\n'
            text += 'Cliente: ' + str(self._listaVendas[0].cliente.nome) + '\n'

            aux = False
            for venda in self._listaVendas:
                if venda.data >= data1 and venda.data <= data2:
                    aux = True
                    text += '\n. Identificador: ' + str(venda.identificador)
                    text += '\n\t\t R$ ' + str('%.2f'%float(venda.calcular_valorNota()))

            if aux:
                messagebox.showinfo('Notas por Período',text)
            else:
                messagebox.showerror('Erro','Não há nenhuma nota nesse período')

    def submit_cliente(self,vent):
        get = str(self._viewVendas.submitCliente.inputCliente.get())

        controle = False

        for cli in self._main.clientes:
            if str(cli.nome) == get:
                controle = True
                break

        if controle:
            controle = False
            self._listaVendas = []

            for venda in self._main.vendas:
                if str(venda.cliente.nome) == get:
                    controle = True
                    self._listaVendas.append(venda)


            if controle:
                self._viewVendas.periodo()
            else:
                messagebox.showerror('Erro','Não há nenhuma venda registrada para esse cliente')
        else:
            messagebox.showerror('Erro','Não há nenhum cliente cadastrado com esse nome')

    def close(self,event):
        self._viewVendas.destroy()

    def prod_vendidos(self):
        if len(self._main.produtos) != 0:
            lista = []

            for i in range(5):
                i_maior = -1
                maior = -1

                for prod in self._main.produtos:
                    if prod.qtdVendida > maior and not prod in lista:
                        maior = prod.qtdVendida
                        i_maior = self._main.produtos.index(prod)

                if i_maior != -1:
                    lista.append(self._main.produtos[i_maior])

            text = 'Produtos mais vendidos:\n'

            i = 1
            for prod in lista:
                text += ' ' + str(i) + '. ' + str(prod.codigo)
                text += ' - ' + str(prod.descricao)
                text += ' - R$ ' + str('%.2f'%prod.precoKg) + '\n'
                text += '\t\tquantidade: ' + str(prod.qtdVendida) + '\n'
                text += '\t\tvalor total: ' + str(prod.faturamento) + '\n\n'
                i+=1

            messagebox.showinfo('Mais vendidos',text)
        else:
            messagebox.showerror('Erro','Não há nenhum produto cadastrado')