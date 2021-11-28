####### written by R3dBlck  #########
########################################################## Import 
import socket
########################################################## Input for which IP adrs
ip = input('enter target :  XXX.XXX.XXX.XXX')
########################################################## To scan your own PC ip = "127.0.0.1"

for port in range(1, 10000):############################## There Port 1 to 10000
    sock = socket.socket()
    sock.settimeout(0.5)
    val=sock.connect_ex((ip, port))
    if val == 0:
        print("Port opened on %d" % port)
    else :
        print("*",end="") ############################### You can delete this line, is just to see the progress 
