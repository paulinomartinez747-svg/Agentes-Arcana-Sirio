# Sesión 2026-06-11 — Hermes en Mac Mini (Setup Inicial)

## Agente: Hermes (deepseek-v4-flash)
## Ubicación: Mac Mini local

## Acciones del día

### 1. Verificación del cerebro
- `~/cerebro` ya clonado de `git@github.com:paulinomartinez747-svg/Agentes-Arcana-Sirio.git`
- Leídos: protocolo.md, CLAVES.md, quien-soy.md, metodo.md
- git pull exitoso: 6 archivos nuevos (motor predicciones, landing, pacientes)

### 2. Diagnóstico y configuración Hermes CLI
- Hermes v0.15.1 instalado en `/Users/macmini/.local/bin/hermes`
- 987 commits atrasados (pendiente `hermes update`)
- Configurado para DeepSeek:
  - model.default: deepseek-chat
  - model.provider: custom
  - model.base_url: https://api.deepseek.com/v1 (DIRECTO)
  - model.context_length: 131072
  - model.api_key: sk-5402bd3954494db88904766a3ff923c7
- **Problema**: Proxy alemán 100.121.93.120:4000 NO alcanzable desde Mac Mini
  - IP en rango CGNAT (100.64.0.0/10), sin ruta desde red local
  - Solución temporal: DeepSeek API directo
  - Pendiente: configurar VPN/Tailscale para alcanzar el proxy
- **Hermes chat funcional** ✅

### 3. Limpieza Claude
- Sin archivo `.env` en home
- Línea ANTHROPIC comentada eliminada de `/Users/macmini/.hermes/.env`
- Sin procesos Claude activos

### 4. Sincronización
- git pull: ✅
- Memoria escrita: ✅ (este archivo)
- git push: ✅

## Próximos pasos
- Actualizar Hermes (987 commits atrasados)
- Conectar Mac Mini a Tailscale para acceder al proxy en Hetzner
- Verificar skills de astrología (artemis-astrology, arcana-cirio)
- Pipeline de cartas astrales desde Mac Mini
