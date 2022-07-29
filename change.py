from ftplib import FTP

host = "10.89.104.179"
user = "ftpuser"
password = "4690tcpip"
try:
    ftp = FTP(host,user,password)
    print("Conexion establecida")
    print("Nos encontramos en la carpeta  "+ftp.pwd())
    print(+ftp.dir())
except Exception as e:
    print("Conexion errada: "+str(e))
