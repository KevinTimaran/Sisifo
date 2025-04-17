import smtplib
import time
from decouple import config

EMAIL_REMITE = config("EMAIL_REMITE")
EMAIL_PASSWORD = config("EMAIL_PASSWORD")
def darMensaje (cuntaUsuario, Productos):
    try:
        InicioTiempo = time.time()
        
        Gmail = smtplib.SMTP("smtp.gmail.com", 587)

        Gmail.starttls()

        Gmail.login(EMAIL_REMITE, EMAIL_PASSWORD)

        Asunto = ("Validacion compra")
        Mensaje = (f"Subject:{Asunto}\n\n Gracias por su compra\n usted a comprado\n,\n {Productos}")

        Gmail.sendmail(EMAIL_REMITE, cuntaUsuario, Mensaje)
        Gmail.quit()

        finalTiempo = time.time()
        tiempoTotal = finalTiempo - InicioTiempo
        if tiempoTotal ==3:
            print (f"La compra se a realizado con exito en un tiempo {tiempoTotal:2f} segundos")
        else:
            print (f"La compra se a realizado con exito en un tiempo {tiempoTotal:2f} segundos(Mayor a lo esperado)")
    except Exception:
        print(f"Erros: no se a eviado el Mensaje al correo{cuntaUsuario}")

darMensaje("kevinstiventimaran@gmail.com", "Pan, Huevos, Leche, Queso")











    
