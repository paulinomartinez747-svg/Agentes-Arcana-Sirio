# Protocolo de Comunicación entre Agentes

## Reglas
1. **Leer antes de actuar:** Todo agente consulta `soluciones/` antes de resolver un problema nuevo.
2. **Escribir después de resolver:** Toda solución va a `soluciones/` con fecha y nombre del agente.
3. **Memoria diaria:** Cada agente escribe un resumen del día en `memoria/YYYY-MM-DD.md`.
4. **Un solo cerebro:** No hay islas. Todo conocimiento se comparte vía este repo.
5. **Pull antes de push:** Siempre `git pull` antes de escribir para evitar conflictos.

## Flujo
```
Agente A resuelve X
  → escribe soluciones/X.md
  → git add, commit, push

Agente B enfrenta X
  → git pull
  → lee soluciones/X.md
  → aplica la solución (no reinventa)
```

## Ubicación del cerebro en cada sistema
| Agente | Ruta local |
|--------|-----------|
| Windows (DeepSeek) | C:\Users\pauli\cerebro\ |
| Hetzner (Hermes) | /root/cerebro/ |
| Hostinger (Claude) | /opt/data/cerebro/ |

## Sincronización
Repositorio Git remoto en GitHub: `paulinomartinez747/cerebro-arcana-sirio`
Cada agente tiene el repo clonado y hace git pull/push para sincronizar.
