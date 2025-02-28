import smtplib
from decouple import config

EMAIL_REMITE = config("EMAIL_REMITE")
EMAIL_PASSWORD = config("EMAIL_PASSWORD")

# Mensaje con asunto (Subject)
mensaje = """\
Subject: Prueba de correo desde Python

Hola, este es un mensaje de prueba enviado con smtplib y python-decouple.
"""
try: 
    Objeto = smtplib.SMTP('smtp.gmail.com',587)

    Objeto.starttls() # se inicia TLS para seguridad

    Objeto.login(EMAIL_REMITE,EMAIL_PASSWORD) # se usa las credenciales de .env
    

    Objeto.sendmail(EMAIL_REMITE, 'kevinstiventimaran@gmail.com', mensaje)

    Objeto.quit()
    print ("Prueba de correo enviado con exito")

except Exception as e:
    print("❌ Error al enviar correo:", e)