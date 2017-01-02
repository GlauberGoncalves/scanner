from tkinter import *
import socket
import os, platform

#
# Função ping retorna true se IP estiver ativo na rede e False se não estiver
#-------------------------------------------------------------------------------#

def ping(host):    
    # ping de acordo com SO
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"

    # Ping
    relatorio = (os.popen("ping -n 1 "+host).read())
    if (relatorio[-5]+relatorio[-4]) != 'da':
        return True
    else: return False
#
# retorna uma lista com cada valor do ip
#-------------------------------------------------------------------------------#
def iphost(host):
    ip = socket.gethostbyname(host)
    ip = ip.split('.')
    return ip
#
# 
#-------------------------------------------------------------------------------#
def verifAparelho(ip,dmin,dmax,cmin,cmax):
    if(ip[0] == '10'):
        for i in range(dmin,dmax+1):
            ip[3] = str(i)
            mont = ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]
            print(mont)
            if(ping(mont)):
                visor.insert('insert',"AP ativo: " + mont + "\n")
                janela.update()                
    else:
        for i in range(cmin,cmax+1):        
            ip[3] = str(i)
            mont = ip[0]+"."+ip[1]+"."+ip[2]+"."+ip[3]
            print(mont)
            if(ping(mont)):
                visor.insert('insert',"AP ativo: " + mont + "\n")
                janela.update()

#
# 
#-------------------------------------------------------------------------------#
             
#
# Layout do sistema
#-------------------------------------------------------------------------------#

def verificaAP():
    ip = iphost(et.get())
    verifAparelho(ip,161,165,80,86)

def verificaRD():
    ip = iphost(et.get())
    verifAparelho(ip,166,175,87,89)

def verificaTM():
    ip = iphost(et.get())
    verifAparelho(ip,176,189,234,246)

def verificaTD():
    ip = iphost(et.get())
    verificaAP()
    verificaTM()
    verificaRD()

# configuração da janela
janela = Tk()
janela.geometry("485x400+400+200")
janela["bg"] = "#2196f3"
janela.title("Scan de Rede - Nimal Tecnologia")

# config botões
btn1 = Button(janela, text="Access point", bg="white", command=verificaAP)
btn2 = Button(janela, text="Rádio Frequencia", bg="white", command=verificaRD)
btn3 = Button(janela, text="Terminal de consulta", bg="white", command=verificaTM)
btn4 = Button(janela, text="Todos", bg="white", command=verificaTD)

btn1.place(x=10, y=40)
btn2.place(x=90, y=40)
btn3.place(x=195, y=40)
btn4.place(x=320, y=40)

# label
lb = Label(janela, text="Número da loja:")
lb.place(x=10, y=10)

visor = Text(janela, width="58", height=20)
visor.place(x=10, y=70)


# entry
et = Entry(janela, width=5)
et.place(x=110,y=10)

janela.mainloop()
#------------------------------------------------------------------------------#