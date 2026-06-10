import json, urllib.request, sqlite3

TOKEN = open("/root/Proyecto_Artemis/.telegram_token").read().strip()
KEY = "sk-5402bd3954494db88904766a3ff923c7"
API = "https://api.deepseek.com/v1/chat/completions"

conn = sqlite3.connect("/root/Proyecto_Artemis/artemis.db")
cur = conn.cursor()
cur.execute("SELECT nombre, fecha_nac, hora_nac, lugar_nac, telefono FROM suscriptores WHERE activo=1 AND telefono LIKE 'tg_%'")
users = cur.fetchall()
conn.close()

total = len(users)
ok = 0
costo = 0

for i, (nombre, fn, hn, lugar, tel) in enumerate(users):
    cid = int(tel.replace('tg_', ''))
    
    prompt = f"Eres el Dr. Paulino Martinez Gallaga. Genera prediccion diaria COMPLETA para HOY miercoles.\n\nTEMA: Proteccion Energetica.\nPACIENTE: {nombre}. Nacimiento: {fn}, {hn} hrs, {lugar}.\n\nDATOS: Fase lunar Cuarto menguante. Sol en Geminis, Luna en Aries.\nTAROT: El Carro.\n\nESTRUCTURA: 1.FRASE 2.TU CIELO HOY 3.QUE CONVIENE 4.EVITAR 5.TAROT (breve) 6.CONSEJO CHAMAN.\nLenguaje sencillo, secundaria, directo, cero frases genericas."
    
    data = json.dumps({"model": "deepseek-v4-flash", "messages": [{"role": "user", "content": prompt}], "max_tokens": 2048, "temperature": 0.7}).encode()
    req = urllib.request.Request(API, data=data, headers={"Content-Type": "application/json", "Authorization": "Bearer " + KEY})
    
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read())
            content = result['choices'][0]['message']['content']
            tokens = result['usage']['total_tokens']
            costo += tokens / 1_000_000 * 0.14
    except Exception as e:
        print(f"[{i+1}/{total}] {nombre[:30]}: API ERROR")
        continue
    
    msg = "\U0001f52e <b>ARCANA SIRIO</b>\nMiércoles · Protección Energética\n\n<b>" + nombre + "</b>\n\n" + content + "\n\n<b>Dr. Paulino Martínez Gallaga</b>\narcanasirio.com"
    
    data2 = json.dumps({"chat_id": cid, "text": msg, "parse_mode": "HTML"}).encode()
    req2 = urllib.request.Request("https://api.telegram.org/bot" + TOKEN + "/sendMessage", data=data2, headers={"Content-Type": "application/json"})
    
    try:
        with urllib.request.urlopen(req2, timeout=10) as resp2:
            if json.loads(resp2.read()).get('ok'):
                ok += 1
                print(f"[{i+1}/{total}] {nombre[:30]}: ENVIADO | {tokens} tok")
    except:
        print(f"[{i+1}/{total}] {nombre[:30]}: SEND FAIL")

print(f"\nTOTAL: {ok}/{total} | Costo: ${costo:.4f}")
