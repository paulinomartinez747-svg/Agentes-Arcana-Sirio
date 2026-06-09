# Harness Arcana Sirio — Sistema de Arnés para Agentes

> Versión: 1.0
> Fecha: 2026-06-09
> Autor: Hermes/DeepSeek (Mac Mini)
> Basado en: Harness Engineering (Mitchell Hashimoto, Stanford/Tsinghua, Microsoft RHO)

## ¿Qué es este arnés?

Este archivo define el SISTEMA completo que rodea a cualquier modelo de IA
que trabaje para Arcana Sirio. El modelo puede cambiar (DeepSeek, Claude, GPT),
pero el arnés NO. Como dice el estudio de Stanford: el mismo modelo con
distinto arnés varía su desempeño hasta 6 VECES.

## Los 6 componentes del arnés

### 1. MODELO (Motor de inteligencia)
```
Primario:   DeepSeek V4 Flash (rápido, barato, ~$0.14/M tokens)
Secundario: Claude Opus 4.7 (solo tareas complejas, ~$3/M tokens)
Local:      Phi-4 14B (Ollama, $0, backup sin internet)
```
Regla: DeepSeek para 95% del trabajo. Claude solo cuando DeepSeek no pueda.

### 2. MEMORIA (Cerebro Compartido)
```
Repositorio: github.com/paulinomartinez747-svg/Agentes-Arcana-Sirio
Nodos:
  - Windows (DeepSeek):  C:\Users\pauli\cerebro\
  - Mac Mini (Hermes):   ~/cerebro/
  - Hetzner (Hermes):    /root/cerebro/
  - Hostinger (Claude):  /opt/cerebro/

Estructura:
  paulino/          → Quién es el Dr. Paulino, su método
  agentes/           → Protocolo de comunicación
  soluciones/        → Bugs resueltos (CONSULTAR antes de actuar)
  memoria/           → Bitácora diaria de cada agente
  obras/             → Libros, cursos (pendiente)
```
Regla: Siempre `git pull` antes de actuar. Siempre documentar después de resolver.

### 3. SKILLS (Habilidades especializadas)
```
19 skills instaladas en Hermes (Mac Mini):
  BUSINESS:
    - proyecto-artemis      → Sistema principal, BD, envíos, referidos
    - marco-2026            → Marketing digital, estrategia
    - plantilla-carta       → Template HTML profesional
    - modulo-jung           → Psicología Junguiana
    - artemis-astrology     → Cálculos Swiss Ephemeris
    - artemis-content       → Contenido redes sociales
    - artemis-psychology    → Interpretación Junguiana
    - artemis-rituals       → Diseño de rituales
    - artemis-tarot         → 78 cartas Rider-Waite

  ASTROLOGY:
    - arcana-cirio          → Asistente astrológico premium
    - decodificacion        → Epigrafía de talismanes
    - agente-financiero     → Astrología financiera
    - agente-genealogia     → Astrogenealogía
    - agente-karmico        → Astrología kármica
    - agente-medico         → Astrología médica
    - agente-rayos          → 7 Rayos Cósmicos
    - agente-talismanes     → Diseño de talismanes

  DEVOPS:
    - supervisor-artemis    → Monitoreo 24/7
```
Regla: Cada skill tiene SKILL.md con instrucciones. Cargar con `skill_view()`.

### 4. HERRAMIENTAS (Lo que el agente puede usar)
```
Infraestructura:
  - Hetzner CX53 (178.104.101.154)  → Servidor producción (€26.49/mes)
  - Hetzner CX23 (116.203.122.171)  → Servidor legacy (€4.99/mes)
  - Hostinger VPS                   → Workspace con 12 agentes
  - Mac Mini M4 (local)             → Desarrollo, skills, BD local

Servicios:
  - Swiss Ephemeris (de421.bsp)     → Efemérides NASA/JPL
  - DeepSeek API                    → Modelo principal
  - Anthropic API                   → Claude (solo para emergencias)
  - Bot Telegram (@Arcana_sirio_bot) → Canal de comunicación
  - Netlify                         → Landing pages (legacy)
  - Porkbun / Cloudflare            → DNS y dominios
  - GitHub                          → Cerebro compartido

Bases de Datos:
  - artemis.db (SQLite)             → 30 suscriptores activos
  - pacientes_completo.csv          → 552 pacientes
  - contactos_limpios.csv           → 3,888 contactos
```

### 5. VERIFICACIÓN (Control de calidad)
```
Automático:
  - Supervisor Artemis (cada hora)  → Bot vivo, DB sana, disco libre
  - Push al cerebro después de      → Cada solución documentada
    cada solución

Manual (Dr. Paulino):
  - Aprueba toda decisión grande
  - Revisa cartas natales antes de entrega
  - Confirma despliegues a producción

Protocolo de verificación:
  1. El agente ejecuta la tarea
  2. Verifica que funcionó (NO asumir)
  3. Documenta en soluciones/ o memoria/
  4. Hace git push al cerebro
  5. Reporta al Dr. Paulino
```

### 6. CICLO DE RETROALIMENTACIÓN (RHO simplificado)
```
Basado en el paper de Microsoft Research Asia:

1. Cuando un agente falla:
   - Documenta el error en soluciones/ con fecha y detalles
   - Describe qué salió mal y por qué

2. Cuando un agente encuentra una solución:
   - La documenta en soluciones/
   - Los otros agentes hacen git pull y la aprenden

3. Cada semana:
   - Revisar soluciones/ para identificar patrones de error
   - Actualizar skills si es necesario
   - Limpiar memoria obsoleta

4. Regla de oro:
   "El mismo error no debe ocurrir dos veces.
    Si ocurre, el arnés está mal diseñado."
```

## Flujo de trabajo diario

```
1. INICIO
   git pull (cerebro)
   Leer memoria/ del día anterior
   Leer soluciones/ nuevas

2. EJECUCIÓN
   Dr. Paulino da una orden
   Consultar skill relevante (skill_view)
   Ejecutar con herramientas disponibles
   VERIFICAR que funcionó

3. DOCUMENTACIÓN
   Escribir en memoria/YYYY-MM-DD.md
   Si resolvió un bug: escribir en soluciones/
   git add, commit, push

4. CIERRE
   Reportar al Dr. Paulino
   Preguntar si aprueba
   Si aprueba: listo
   Si no: corregir y repetir
```

## Recordatorio final

El modelo es solo una parte de la máquina.
El arnés es lo que convierte capacidad en productividad repetible.
Un agente sin arnés es frágil. Un agente con arnés es una empresa.

— Arcana Sirio · Dr. Paulino Martínez Gallaga
