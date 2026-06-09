# DNS de arcanasirio.com — De caído a funcional

## Fecha
2026-06-09

## Agente que lo resolvió
DeepSeek V4 Flash (laptop Windows — Deep Chip Tweet)

## Problema
arcanasirio.com no cargaba para nadie. El dominio estaba en Porkbun con un ALIAS 
apuntando a Cloudflare (uixie.porkbun.com). Netlify tenía el dominio secuestrado 
y lo regresaba a su servidor aunque los registros DNS se cambiaran.

3 intentos fallaron:
1. Hermes (yo) intentó cambiar DNS desde Porkbun API → 403 Forbidden
2. Claude Code intentó forzar desde Netlify → logró soltar el dominio pero DNS no propagaba
3. Cambiar nameservers a Hetzner/Cloudflare → Porkbun los rechazaba

El resultado: arcanasirio.com servía la página vieja de Netlify mientras la 
nueva estaba en Hetzner CX53.

## Solución
DeepSeek (desde Windows laptop) logró:
1. Acceder a Porkbun (posiblemente desde una IP autorizada)
2. Eliminar el ALIAS problemático
3. Configurar el registro A directo a 178.104.101.154 (Hetzner)
4. Configurar CNAME para www
5. Forzar la propagación

## Comandos usos
No disponibles — DeepSeek trabajó desde su sesión privada en Windows.

## Archivos modificados/creados
- No disponibles

## Lecciones aprendidas
1. Porkbun NO es confiable para DNS. Cambiar a Cloudflare Registrar cuando sea posible.
2. El ALIAS de Porkbun a Cloudflare uixie.porkbun.com bloqueaba cualquier cambio directo.
3. DeepSeek fue el único que pudo acceder a Porkbun y hacer el cambio.
4. La IP desde la que se hace el cambio en Porkbun debe estar autorizada en su API.
5. No intentar más de 3 enfoques diferentes para un mismo problema — escalar al agente correcto.
