from fastapi import FastAPI, HTTPException, Request, APIRouter
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

class FormData(BaseModel):
    year_model: str
    marca: str
    modelo: str
    nombre_apellido: str
    mail: str
    telefono: str
    imagen: str
    detalles: str

def vender_auto(form_data: FormData):
    sender_email = "fac.demarco37@gmail.com"
    sender_password = os.environ.get("SENDER_PASSWORD")
    if not sender_password:
        raise HTTPException(status_code=500, detail="La contraseña del remitente no está configurada")
    receiver_email = "fac.demarco37@gmail.com"
    subject = f"Nuevo mensaje de contacto desde la Web para venta de auto de {form_data.nombre_apellido}"
    body = f"Nombre y apellido: {form_data.nombre_apellido}\nMail: {form_data.mail}\nTeléfono: {form_data.telefono}\nAño del modelo: {form_data.year_model}\nMarca: {form_data.marca}\nModelo: {form_data.modelo}\nImagen: {form_data.imagen}\nDetalles: {form_data.detalles}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Correo de venta de autoenviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        raise HTTPException(status_code=500, detail="Error al enviar el correo")

@router.post("/sell_car")
async def sell_car(form_data: FormData):
    vender_auto(form_data)
    return {"message": "Formulario de venta de auto enviado exitosamente"}
