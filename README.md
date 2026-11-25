# 🧠 Kit Profesional de Psicología: Preparación y Gestión Operativa

> **Kit de Herramientas, Agente Inteligente en Telegram y Skills Especializadas para Profesionales y Estudiantes de Psicología.**  
> *Diseñado para optimizar la preparación de consultas, organización operativa y redacción técnica, cuidando rigurosamente los límites éticos y garantizando la confidencialidad sin emitir diagnósticos clínicos automatizados.*

---

## 🌐 Enlace en Vivo a la Landing Page

La presentación interactiva y el catálogo visual del kit se encuentran alojados en la carpeta `docs/`, listos para GitHub Pages o visualización directa en el navegador:

- **Landing Page en GitHub Pages:** [https://salor1010.github.io/Kit-practica-psicologia/](https://salor1010.github.io/Kit-practica-psicologia/)
- **Archivo Local:** [docs/index.html](file:///c:/Users/USER/Documents/Parcial_Final/docs/index.html) *(ábrelo en cualquier navegador web)*.

---

## 📖 Descripción General

El **Kit Profesional de Psicología** es una solución integral orientada a la carrera de **Psicología** (en sus ámbitos clínico, formativo y de consultoría). Su propósito central es resolver las demandas operativas y administrativas cotidianas del profesional:

1. **Preparación estructurada de sesiones:** Diseñar entrevistas exploratorias ordenadas y adaptables al motivo de consulta.
2. **Material didáctico para el consultante:** Generar fichas pedagógicas de auto-observación y ejercicios inter-sesión libres de tecnicismos estigmatizantes.
3. **Sistematización y seguimiento de metas:** Llevar bitácoras y registros longitudinales del avance terapéutico sin vulnerar la privacidad.
4. **Asistente inteligente 24/7:** Disponer de un agente conversacional en Telegram que procesa casos y textos aplicando modelos teóricos reconocidos mediante **Google Gemini** y **Skills personalizadas**.

> ⚖️ **Compromiso Ético y Deontológico:**  
> Ningún componente del kit emite diagnósticos nosológicos cerrados, recetas ni juicios clínicos automatizados. El sistema funciona como una herramienta de preparación y apoyo administrativo, manteniendo siempre el juicio profesional humano y la anonimización de consultantes mediante códigos de identificación (`CONS-01`).

---

## 🏛️ Arquitectura del Repositorio

```text
kit-practica-psicologia/
├── herramientas/                  # Módulos funcionales ejecutables en Python
│   ├── herramienta-1/             # Estructurador de guías de preguntas abiertas
│   │   ├── estructurador_entrevistas.py
│   │   ├── ejemplo_guia_salida.txt
│   │   └── README.md
│   ├── herramienta-2/             # Generador de plantillas de psicoeducación y tareas
│   │   ├── generador_psicoeducacion.py
│   │   ├── ejemplo_tarea_psicoeducativa.txt
│   │   └── README.md
│   └── herramienta-3/             # Organizador de notas temáticas y seguimiento de objetivos
│       ├── organizador_seguimiento.py
│       ├── registro_casos.json
│       └── README.md
├── agente/                        # Asistente inteligente con integración a Telegram y Gemini
│   ├── bot_telegram.py            # Servidor del bot con carga dinámica de skills
│   ├── requirements.txt           # Dependencias (python-telegram-bot, google-generativeai, python-dotenv)
│   ├── .env.example               # Plantilla segura de variables de entorno
│   ├── .env                       # Credenciales privadas (ignorado en git)
│   └── README.md                  # Documentación operativa del agente
├── skills/                        # Skills operativas en formato estándar (para entrega)
│   ├── skill-1/SKILL.md           # Análisis técnico multidimensional de casos
│   ├── skill-2/SKILL.md           # Redacción de informes y bitácoras profesionales
│   └── skill-3/SKILL.md           # Preparación de preguntas de entrevista y evaluación
├── .opencode/skills/              # Réplica de skills para pruebas en vivo en entornos OpenCode
│   ├── skill-1/SKILL.md
│   ├── skill-2/SKILL.md
│   └── skill-3/SKILL.md
├── docs/                          # Landing page de presentación del proyecto
│   └── index.html                 # Página HTML responsiva lista para GitHub Pages
├── .vscode/                       # Configuración del entorno del IDE
│   └── settings.json              # Configuración del intérprete de Python y rutas de módulos
├── .gitignore                     # Protección de archivos confidenciales (.env, cachés, venv)
└── README.md                      # Documentación maestra del proyecto
```

---

## 🛠️ Detalle de las 3 Herramientas Funcionales

Cada herramienta funciona de forma independiente sin dependencias externas complejas y cuenta con su propia documentación interna:

### 1. [Herramienta 1: Estructurador de Guías de Preguntas Abiertas](file:///c:/Users/USER/Documents/Parcial_Final/herramientas/herramienta-1/README.md)
* **Archivo principal:** [herramientas/herramienta-1/estructurador_entrevistas.py](file:///c:/Users/USER/Documents/Parcial_Final/herramientas/herramienta-1/estructurador_entrevistas.py)
* **¿Qué hace?**  
  Permite al profesional diseñar una guía modular de preguntas abiertas para entrevistas iniciales o sesiones de exploración. Organiza las preguntas en 4 bloques temáticos esenciales: *Motivo de Consulta y Expectativas*, *Impacto en Áreas Vitales (sueño, relaciones, rutina)*, *Recursos Propios y Redes de Apoyo*, y *Contextualización Histórica/Línea Temporal*.
* **¿Cómo ejecutarla y usarla?**
  ```bash
  python herramientas/herramienta-1/estructurador_entrevistas.py
  ```
  Genera un archivo formateado en texto (`ejemplo_guia_salida.txt`) listo para llevar a consulta o imprimir. También puede importarse como módulo en otros scripts.

---

### 2. [Herramienta 2: Generador de Plantillas de Psicoeducación y Tareas](file:///c:/Users/USER/Documents/Parcial_Final/herramientas/herramienta-2/README.md)
* **Archivo principal:** [herramientas/herramienta-2/generador_psicoeducacion.py](file:///c:/Users/USER/Documents/Parcial_Final/herramientas/herramienta-2/generador_psicoeducacion.py)
* **¿Qué hace?**  
  Genera documentos pedagógicos claros y amables para entregar al consultante. Incluye explicaciones didácticas sobre fenómenos psicológicos habituales acompañadas de formatos estructurados de registro para tareas entre sesiones (ej. ciclo de activación y evitación ante la ansiedad, entrenamiento en respiración diafragmática consciente, y bitácora nocturna de agradecimientos y logros).
* **¿Cómo ejecutarla y usarla?**
  ```bash
  python herramientas/herramienta-2/generador_psicoeducacion.py
  ```
  Produce de inmediato el archivo de trabajo `ejemplo_tarea_psicoeducativa.txt` con tablas delimitadas de fácil diligenciamiento.

---

### 3. [Herramienta 3: Organizador de Notas Temáticas y Seguimiento](file:///c:/Users/USER/Documents/Parcial_Final/herramientas/herramienta-3/README.md)
* **Archivo principal:** [herramientas/herramienta-3/organizador_seguimiento.py](file:///c:/Users/USER/Documents/Parcial_Final/herramientas/herramienta-3/organizador_seguimiento.py)
* **¿Qué hace?**  
  Sistema ligero de gestión de expedientes anonimizados. Permite registrar metas terapéuticas acordadas colaborativamente, actualizar su estado evolutivo (`Pendiente`, `En progreso`, `Alcanzado`), documentar acuerdos inter-sesión en formato JSON (`registro_casos.json`) y generar una **Ficha Operativa de Preparación** con un solo clic antes de que el consultante ingrese a consulta.
* **¿Cómo ejecutarla y usarla?**
  ```bash
  python herramientas/herramienta-3/organizador_seguimiento.py
  ```

---

## 🤖 Detalle del Agente Inteligente y Conexión a Telegram

El bot (**[@asistente_psico_salome_bot](https://t.me/asistente_psico_salome_bot)**) actúa como un asistente operativo personal para el psicólogo. Integra el SDK oficial de **Google Gemini** (`gemini-3.5-flash-lite`) y lee en tiempo de ejecución las instrucciones de los archivos `SKILL.md` de la carpeta `skills/`.

### Actividades que Automatiza:
- **Análisis multidimensional de casos:** Examina situaciones o casos complejos contrastando hipótesis cognitivas, conductuales, humanistas y psicodinámicas.
- **Estructuración y redacción técnica:** Convierte apuntes rápidos de consulta en resúmenes profesionales, bitácoras ordenadas o informes académicos.
- **Preparación de entrevistas:** Genera pautas de preguntas y rúbricas de retroalimentación constructiva antes de una sesión.
- **Consultas profesionales libres:** Responde dudas metodológicas manteniendo en todo momento el marco deontológico.

### Comandos Disponibles en Telegram:
| Comando | Descripción | Skill Asociada |
| :--- | :--- | :--- |
| `/start` | Mensaje de bienvenida, encuadre ético y menú de comandos. | — |
| `/skills` | Lista las skills cargadas dinámicamente desde `skills/`. | Todas |
| `/analizar <caso>` | Ejecuta un análisis cualitativo en 4 enfoques teóricos. | `Skill 1` |
| `/resumir <notas>` | Redacta un informe o bitácora profesional con acuerdos de sesión. | `Skill 2` |
| `/preguntas <contexto>` | Diseña un banco de preguntas abiertas y pautas de feedback. | `Skill 3` |
| `/ayuda` | Despliega los lineamientos de confidencialidad y guía técnica. | — |
| *Mensaje Libre* | Consulta abierta a Gemini contextualizada con las 3 skills del kit. | Integrada |

### Configuración y Puesta en Marcha del Bot:

1. **Instalación de dependencias:**
   ```bash
   pip install -r agente/requirements.txt
   ```
2. **Configuración de Variables de Entorno (`.env`):**
   Copia el archivo `.env.example` en la carpeta `agente/` con el nombre `.env`:
   ```bash
   cp agente/.env.example agente/.env    # En Linux / macOS
   copy agente\.env.example agente\.env  # En Windows PowerShell / CMD
   ```
   Rellena tus credenciales privadas dentro de `agente/.env`:
   ```env
   TELEGRAM_BOT_TOKEN="tu_token_de_botfather"
   GEMINI_API_KEY="tu_api_key_de_google_ai_studio"
   ```
   *(Nota: `agente/.env` está protegido en `.gitignore` para evitar filtraciones accidentales).*

3. **Ejecución del Bot:**
   ```bash
   python agente/bot_telegram.py
   ```
   Verás en consola el mensaje de inicio:
   ```text
   INFO - SDK de Google Gemini inicializado correctamente con gemini-3.5-flash-lite.
   INFO - Application started
   ```

---

## 💡 Detalle de las 3 Skills Especializadas

Cada skill está documentada con encabezados YAML válidos y reglas metodológicas detalladas en `skills/*/SKILL.md` (y replicada en `.opencode/skills/`):

1. **[Skill 1: Análisis Técnico Multidimensional de Casos](file:///c:/Users/USER/Documents/Parcial_Final/skills/skill-1/SKILL.md)**
   * **Identificador YAML:** `analisis-tecnico-casos-psicologia`
   * **Propósito:** Proporciona un marco sistemático para examinar situaciones clínicas o textos teóricos. Estructura el análisis en cuatro secciones independientes: *Hipótesis Cognitiva* (distorsiones y esquemas nucleares), *Análisis Conductual* (antecedentes y consecuencias mantenedoras), *Lectura Humanista* (autorrealización y congruencia) y *Comprensión Psicodinámica* (defensas y dinámicas vinculares), cuidando de no emitir diagnósticos médicos concluyentes.

2. **[Skill 2: Redacción y Formateo de Informes y Bitácoras](file:///c:/Users/USER/Documents/Parcial_Final/skills/skill-2/SKILL.md)**
   * **Identificador YAML:** `redaccion-informes-bitacoras-profesionales`
   * **Propósito:** Estandariza la elaboración de informes operativos, resúmenes de sesión y bitácoras académicas. Define secciones obligatorias para objetivos observables, descripción temática, avances registrados y compromisos inter-sesión, aplicando anonimización y tono deontológico objetivo.

3. **[Skill 3: Preparación de Preguntas de Entrevista y Retroalimentación](file:///c:/Users/USER/Documents/Parcial_Final/skills/skill-3/SKILL.md)**
   * **Identificador YAML:** `preparacion-entrevistas-evaluacion-retroalimentacion`
   * **Propósito:** Guía la formulación de bancos de preguntas abiertas no inductivas organizadas por bloques (apertura, impacto y recursos), rúbricas de observación cualitativa y protocolos estructurados para emitir retroalimentación validante y constructiva.

---

## 🔒 Confidencialidad y Seguridad

- **Protección de Secretos:** El archivo `.gitignore` excluye deliberadamente cualquier variante de `.env`, entornos virtuales (`venv/`, `.venv/`) y archivos temporales de Python.
- **Datos Anonimizados:** Todas las herramientas y ejemplos están construidos bajo identificadores despersonalizados (`CONS-01`, `CONS-2026-A1`), previniendo la exposición de información privada de consultantes reales.

---

## 👩‍💻 Autora y Créditos

* **Proyecto:** Parcial Final - Kit de Herramientas y Agente de Inteligencia Artificial para la Práctica en Psicología.
* **Repositorio GitHub:** [saloR1010/Kit-practica-psicologia](https://github.com/saloR1010/Kit-practica-psicologia)
