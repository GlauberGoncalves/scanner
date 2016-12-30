from tkinter import *
from socket import *
import os, platform


#-------------------------------------------------------------------------------#
def ping(host):    
    # ping de acordo com SO
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"

    # Ping
    relatorio = (os.popen("ping -n 1 "+host).read())
    if (relatorio[-5]+relatorio[-4]) != 'da':
        return True
    else: return False
#-------------------------------------------------------------------------------#
    
for i in range(256):
    host = "179.198.138." + str(i)
    if(ping(host)):
        print("host "+host+": Ativo na rede")
