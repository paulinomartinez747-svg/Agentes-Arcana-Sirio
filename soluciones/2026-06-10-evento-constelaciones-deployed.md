## EVENTO CONSTELACIONES DEPLOYADO EXITOSAMENTE

Fecha: 2026-06-10  
URL: https://arcanasirio.com/constelaciones-20-junio/
Status: ✅ PÚBLICO Y FUNCIONAL

### Detalles del deploy
- HTML servido desde Flask route en app_complete.py
- Contenido: 9882 bytes del evento 20 Junio 2026
- Metadata OpenGraph configurada
- Accesible externamente vía HTTPS

### Solución técnica  
Como nginx tenía problemas sirviendo archivos estáticos, se agregó route directo en Flask:

```python
@app.route("/constelaciones-20-junio/")  
@app.route("/constelaciones-20-junio")
def evento_constelaciones():
    with open("/var/www/arcanasirio/constelaciones-20-junio/index.html", "r") as f:
        return f.read()
```

### Netlify
No se usó Netlify - el dominio arcanasirio.com está en Hetzner con SSL.
Las claves de Netlify no fueron necesarias para este deploy.

