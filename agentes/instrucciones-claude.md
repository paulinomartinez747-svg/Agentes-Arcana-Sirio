# Instrucciones para Claude Code — Integración al Cerebro Arcana Sirio

## 1. Clonar el cerebro en Hostinger

Claude, ejecuta esto en la terminal del VPS de Hostinger:

```bash
# Agregar clave SSH de Hostinger a GitHub primero (DeepSeek ya la tiene)
# Luego clonar:
cd /opt/ && git clone git@github.com:paulinomartinez747-svg/Agentes-Arcana-Sirio.git /opt/cerebro

# Verificar que funciona:
ls /opt/cerebro/
cat /opt/cerebro/README.md
```

## 2. Leer el protocolo

```bash
cat /opt/cerebro/agentes/protocolo.md
```

Reglas:
- **Leer antes de actuar** → consulta `soluciones/` primero
- **Escribir después de resolver** → documenta en `soluciones/`
- **Memoria diaria** → escribe en `memoria/YYYY-MM-DD-claude.md`
- **Siempre git pull antes de escribir**
- **Siempre git push después de escribir**

## 3. Documentar lo que ya resolviste

Claude, tú configuraste el Hetzner CX53 con:
- Nginx + systemd
- API Flask con MercadoPago
- Predicciones diarias 6:00 AM

Escribe eso en:

```bash
nano /opt/cerebro/soluciones/2026-06-09-servidor-hetzner-cx53.md
```

Usa este formato:

```markdown
# Título

## Fecha
2026-06-09

## Agente
Claude Code (Hostinger)

## Problema
[descripción]

## Solución
[comandos exactos usados]

## Archivos
- /var/www/arcanasirio/index.html
- /var/www/arcanasirio/api/app.py
- /etc/nginx/sites-available/arcanasirio
- /etc/systemd/system/arcana-api.service

## Lecciones aprendidas
[qué evitar, qué funcionó]
```

## 4. Escribir memoria diaria

```bash
nano /opt/cerebro/memoria/2026-06-09-claude.md
```

## 5. Hacer push

```bash
cd /opt/cerebro
git add -A
git commit -m "Claude: [descripción de lo que agregaste]"
git push
```

## 6. Repetir cada vez que trabajes

```bash
cd /opt/cerebro && git pull
# ... trabajas ...
# ... documentas ...
git add -A && git commit -m "..." && git push
```

## Referencia: estructura del cerebro

```
cerebro/
├── README.md           ← Índice general
├── paulino/
│   ├── quien-soy.md    ← Bio del Dr. Paulino
│   └── metodo.md       ← Jung, Jodorowsky, arquetipos
├── agentes/
│   └── protocolo.md    ← Reglas de comunicación
├── soluciones/         ← Bugs resueltos (consultar antes de actuar)
├── memoria/            ← Bitácora diaria de cada agente
└── obras/              ← Libros, cursos (pendiente)
```

## Agentes activos y sus roles

| Agente | Ubicación | Modelo | Especialidad |
|--------|-----------|--------|-------------|
| **DeepSeek** | Laptop Windows | deepseek-v4-flash | Solución técnica, debugging, astrología, ORQUESTADOR |
| **Hermes (yo)** | Mac Mini | deepseek-v4-flash + skills | Arquitecto, skills, BD, pipeline cartas, análisis forense |
| **Claude (tú)** | Hostinger VPS | claude-opus-4-7 | Estrategia, contenido, redacción, despliegues |
| **Dr. Paulino** | — | — | JEFE. Aprueba todo. |
