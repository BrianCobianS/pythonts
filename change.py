from ftplib import FTP
from pickle import TRUE
host = "10.89.105.98"
user = "ftpuser"
password = "4690tcpip"
try:
    ftp = FTP(host,user,password)
    print("Conexion establecida")
    print("Nos encontramos en la carpeta  "+ftp.pwd())
    ftp.dir()
    ftp.mkd("ola")
    print("Se creo la carpeta ola")
    ftp.dir()
    ftp.cwd("ola")
    ftp.dir()
    texto="Hola Mundo!!!!"
    archivo = open('Saludo.txt','w')
    archivo.write(texto)
    archivo.close()
    archivo = open("Saludo.txt",'rb')
    if ftp.storbinary('STOR Saludo.txt',archivo):
        print('\nArchivo creado y enviado con exito...\n')
        ftp.dir()
    
except Exception as e:
    print("Conexion cerrada: "+str(e))
