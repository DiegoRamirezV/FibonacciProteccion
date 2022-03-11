import datetime
import smtplib

hora = datetime.datetime.now()

def fibonacci(hora):
    serie= [int(x) for x in str(hora.minute)]
    if len(serie) ==1:
        serie.append(serie[0])
        serie[0] = 0
    cantidad = hora.second
    resultado = 0
       
    for i in range(2,cantidad+2):
        resultado = serie[i-2]+serie[i-1]
        serie.append(resultado)

    return  serie  

def enviaMail():

    conexion = smtplib.SMTP(host = 'smtp.gmail.com', port=587)
    conexion.ehlo
    conexion.starttls()

    mail = 'diegopruebaproteccion@gmail.com'
    contr = '123456789p!'
    horaf = hora.strftime('%H:%M:%S')
    serie = fibonacci(hora)

    conexion.login(user=mail , password= contr)

    mensaje = "Subject: Prueba fibonacci\n\nHora de ejecucion: "+ horaf + "\nSerie generada: "+ str(serie)

    conexion.sendmail(from_addr=mail, to_addrs='juan.gomezh@proteccion.com.co', msg=mensaje)

    conexion.quit()


enviaMail()