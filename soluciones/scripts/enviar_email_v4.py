import json, urllib.request, sqlite3, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

KEY = "sk-5402bd3954494db88904766a3ff923c7"
API = "https://api.deepseek.com/v1/chat/completions"
DB = "/root/Proyecto_Artemis/artemis.db"
GMAIL = "paulinomartinez747@gmail.com"
PW = open("/root/Proyecto_Artemis/.gmail_app_password").read().strip()

HOY = datetime.now()
DIA = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"][HOY.weekday()]
TEMAS = ["Constelaciones Ancestrales","Psicoterapia Gestalt","Protección Energética","Código de Jade","Sanación del Alma","Integración","El Espíritu"]
TEMA = TEMAS[HOY.weekday()]

conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("SELECT DISTINCT nombre, email FROM suscriptores WHERE activo=1 AND email IS NOT NULL AND email != '' AND email != 'None' AND (telefono IS NULL OR telefono NOT LIKE 'tg_%')")
users = list(set(cur.fetchall()))  # deduplicate
conn.close()

print(f"Enviando a {len(users)} emails...")

ok = 0
for nombre, email in users:
    prompt = f"Eres el Dr. Paulino Martinez Gallaga. Genera prediccion diaria COMPLETA para HOY {DIA}.\n\nTEMA: {TEMA}.\nPACIENTE: {nombre}.\n\nDATOS: Fase lunar Cuarto menguante. Sol en Geminis, Luna en Aries.\nTAROT: El Carro.\n\nESTRUCTURA: 1.FRASE 2.TU CIELO HOY 3.QUE CONVIENE 4.EVITAR 5.TAROT (breve) 6.CONSEJO CHAMAN.\nLenguaje sencillo, secundaria, directo, cero frases genericas."
    
    data = json.dumps({"model": "deepseek-v4-flash", "messages": [{"role": "user", "content": prompt}], "max_tokens": 2048, "temperature": 0.7}).encode()
    req = urllib.request.Request(API, data=data, headers={"Content-Type": "application/json", "Authorization": "Bearer " + KEY})
    
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            content = json.loads(resp.read())['choices'][0]['message']['content']
    except Exception as e:
        print(f"  {nombre}: API ERR")
        continue
    
    # Build HTML email
    html = f"""<html><body style="font-family:Georgia,serif;max-width:600px;margin:0 auto;background:#0a0e1a;color:#e6e0d0;padding:20px">
    <div style="text-align:center;padding:20px;border-bottom:1px solid #c9a959">
    <h1 style="color:#c9a959;letter-spacing:3px;margin:0">ARCANA SIRIO</h1>
    <p style="color:#8a8a80;font-size:12px">{DIA} · {TEMA}</p></div>
    <h2 style="color:#f0e6d3;text-align:center">{nombre}</h2>
    <div style="background:#1a2744;padding:20px;border-radius:8px;margin:15px 0;white-space:pre-line;line-height:1.7">{content.replace(chr(10),'<br>')}</div>
    <p style="text-align:center;color:#8a8a80;font-size:11px;margin-top:20px">Dr. Paulino Martínez Gallaga<br>arcanasirio.com · @Arcana_sirio_bot</p>
    </body></html>"""
    
    msg = MIMEMultipart()
    msg['From'] = f"Arcana Sirio <{GMAIL}>"
    msg['To'] = email
    msg['Subject'] = f"{nombre}, tu predicción de {DIA} | Arcana Sirio"
    msg.attach(MIMEText(html, 'html'))
    
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(GMAIL, PW)
        s.sendmail(GMAIL, email, msg.as_string())
        s.quit()
        ok += 1
        print(f"  {nombre}: EMAIL OK")
    except Exception as e:
        print(f"  {nombre}: EMAIL ERR - {str(e)[:50]}")

print(f"\nTOTAL: {ok}/{len(users)} emails enviados")
