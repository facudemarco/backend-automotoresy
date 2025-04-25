from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

class FormData(BaseModel):
    nombre_apellido: str
    telefono: int
    mail: str
    cuit: str
    estado_tributario: str
    estado_civil: str
    modelo_car: str
    marca_car: str
    price_car: str

def enviar_email(form_data: FormData):
    sender_email = "iweb.contacto@gmail.com"
    sender_password = os.environ.get("SENDER_PASSWORD")
    if not sender_password:
        raise HTTPException(status_code=500, detail="La contraseña del remitente no está configurada")
    receiver_email = "automotoresyrigoyen@gmail.com"
    subject = f"Nuevo mensaje de financiamiento desde la Web de {form_data.nombre_apellido}"
    body = f"Datos de la consulta: \nNombre y apellido: {form_data.nombre_apellido}\nMail: {form_data.mail}\nTeléfono: {form_data.telefono}\nCUIT: {form_data.cuit}\nEstado tributario: {form_data.estado_tributario} \nEstado civil: {form_data.estado_civil}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Correo enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        raise HTTPException(status_code=500, detail="Error al enviar el correo")

@router.post("/financial")
async def financial(form_data: FormData):
    enviar_email(form_data)
    return {"message": "Formulario enviado exitosamente"}
