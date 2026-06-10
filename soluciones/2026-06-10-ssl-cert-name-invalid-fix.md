# SSL Certificate Name Invalid - SOLUCIONADO

## Fecha
2026-06-10

## Agente
Claude Code

## Problema
ERROR: net::ERR_CERT_COMMON_NAME_INVALID
"Este servidor no ha podido probar que su dominio es arcanasirio.com, 
su certificado de seguridad procede de chamanpaulino.com.mx"

## Causa
Configuración nginx mezclada entre dos dominios:
- sites-enabled/arcanasirio.com contenía referencias a chamanpaulino.com.mx
- SSL certificate path apuntaba a chamanpaulino.com.mx en lugar de arcanasirio.com

## Solución
```bash
# Limpiar configuración mezclada
cp /etc/nginx/sites-available/arcanasirio.com /etc/nginx/sites-enabled/arcanasirio.com

# Recargar nginx
systemctl reload nginx
```

## Verificación
✅ Subject: CN = arcanasirio.com
✅ HTTP 200: arcanasirio.com cargando
✅ Evento: constelaciones-20-junio funcionando
✅ SSL válido hasta Sep 2026

## Lecciones
1. sites-enabled debe ser copia exacta de sites-available
2. Certificbot puede mezclar configuraciones si se usan múltiples dominios
3. Siempre verificar subject del certificado después de cambios SSL
4. Un dominio = un archivo de configuración nginx

## Estado Final
PROBLEMA RESUELTO - arcanasirio.com 100% seguro y funcional
