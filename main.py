# importando tkinter
from tkinter import *
from tkinter import ttk

# cores
cor1 = "#3b3b3b" #preta
cor2 = "#feffff" #branca
cor3 = "#38576b" #azul carregado
cor4 = "#ECEFF1" #cinza
cor5 = "#FFAB40" #laranja

#tamanho da janela
janela = Tk()
janela.title("Calculadora") #o titulo 
janela.geometry("235x314") #definir o tamanho
janela.config(bg=cor1) #cor do fundo da calculadora

#criando frames / janela de exibição de calculo
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#variavel todos valores
todos_valores=''
valor_texto = StringVar()

#criando função
def entrar_valores(event):
    global todos_valores  
    todos_valores= todos_valores + str(event) 
    valor_texto.set(todos_valores)  #passando o valor na tela

# função de calculo
def calcular():
    resultado = eval(todos_valores) # calcula os valores
    valor_texto.set(str(resultado)) # mostra o valor na tela

#função de limpar tela e valores
def limpar_tela():
    global todos_valores # limpar os valores da tela
    todos_valores = "" 
    valor_texto.set("") # limpa a tela somente

#criando label
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0,)

#criando botões 

#primeira linha
b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #criando o tamanho
b_1.place(x=1, y=0) #vertical e lateral da tela

b_2 = Button(frame_corpo, command=lambda:entrar_valores('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=119, y=0)

b_3 = Button(frame_corpo, command=lambda:entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=179, y=0)

#segunda linha
b_4 = Button(frame_corpo, command=lambda:entrar_valores('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=53)

b_5 = Button(frame_corpo, command=lambda:entrar_valores('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=53)

b_6 = Button(frame_corpo, command=lambda:entrar_valores('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=119, y=53)

b_7 = Button(frame_corpo, command=lambda:entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=179, y=53)

#terceira linha
b_8 = Button(frame_corpo, command=lambda:entrar_valores('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=106)

b_9 = Button(frame_corpo, command=lambda:entrar_valores('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=106)

b_10 = Button(frame_corpo, command=lambda:entrar_valores('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=119, y=106)

b_11 = Button(frame_corpo, command=lambda:entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=179, y=106)

#quarta linha
b_12 = Button(frame_corpo, command=lambda:entrar_valores('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=159)

b_13 = Button(frame_corpo, command=lambda:entrar_valores('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=159)

b_14 = Button(frame_corpo, command=lambda:entrar_valores('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=119, y=159)

b_15 = Button(frame_corpo, command=lambda:entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=179, y=159)

#quinta linha
b_16 = Button(frame_corpo, command=lambda:entrar_valores('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #criando o tamanho
b_16.place(x=1, y=212) #vertical e lateral da tela

b_17 = Button(frame_corpo, command=lambda:entrar_valores('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=119, y=212)

b_18 = Button(frame_corpo, command=calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=179, y=212)

janela.mainloop()