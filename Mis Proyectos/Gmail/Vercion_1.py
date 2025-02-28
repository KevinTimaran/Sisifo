import smtplib
import time
from decouple import config

EMAIL_REMITE = config("EMAIL_REMITE")
EMAIL_PASSWORD = config("EMAIL_PASSWORD")

def EnviarCorreo(Destino, Compra):

    try:
        inicion = time.time()

        Objeto = smtplib.SMTP("smtp.gmail.com", 587)

        Objeto.starttls() # se inicia TLS para seguridad

        Objeto.login(EMAIL_REMITE,EMAIL_PASSWORD) # se usa las credenciales de .env

        #Creamos el mendaje de asunto
        asunto = "Comfirmacion de compra"
        mensaje =f"Subuject:{asunto}\n\n Gracias por tu compra.\n,\n Detalles {Compra}"
        

        Objeto.sendmail(EMAIL_REMITE, Destino, mensaje)
        Objeto.quit()
        print ("Prueba de correo enviado con exito")

        fin = time.time()
        tiempoTotal = fin - inicion
        if tiempoTotal < 3 :
            print (f"El tiempo que tardo en enviar el mensaje es de {tiempoTotal:2f} segundos.")
        else:
            print (f"El tiempo que tardo enviar el mansaje fue de {tiempoTotal:2f}segundos (Excede el limite de 2s)")

    except Exception as e:
        print("❌ Error al enviar correo:", e)

if __name__ == "__main__":
    EnviarCorreo("kevinstiventimaran@gmail.com", "Paaaan- 1000")