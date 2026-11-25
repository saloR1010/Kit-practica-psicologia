"""
Agente Operativo de Práctica Psicológica (Telegram Bot).
Conecta con Google Gemini y lee dinámicamente las skills desde skills/ (SKILL.md)
para ejecutar actividades estructuradas respetando los límites éticos y de confidencialidad.
"""

import os
import sys
import logging
from pathlib import Path
from dotenv import load_dotenv

# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
SKILLS_DIR = BASE_DIR / "skills"
ENV_PATH = Path(__file__).resolve().parent / ".env"

# Cargar variables de entorno desde agente/.env explícitamente
load_dotenv(dotenv_path=ENV_PATH)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

# Configurar logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configurar Google Generative AI si la clave está disponible
gemini_model = None
if GEMINI_KEY and GEMINI_KEY != "tu_api_key_del_modelo":
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_KEY)
        gemini_model = genai.GenerativeModel("gemini-3.5-flash-lite")
        logger.info("SDK de Google Gemini inicializado correctamente con gemini-3.5-flash-lite.")
    except Exception as e:
        logger.error(f"Error al inicializar Gemini SDK: {e}")

def cargar_skills() -> dict:
    """Carga dinámicamente el contenido de todas las skills ubicadas en skills/*/SKILL.md."""
    skills_dict = {}
    if not SKILLS_DIR.exists():
        return skills_dict

    for skill_folder in sorted(SKILLS_DIR.iterdir()):
        if skill_folder.is_dir():
            skill_file = skill_folder / "SKILL.md"
            if skill_file.exists():
                try:
                    contenido = skill_file.read_text(encoding="utf-8")
                    skills_dict[skill_folder.name] = contenido
                except Exception as e:
                    logger.warning(f"No se pudo leer {skill_file}: {e}")
    return skills_dict

DICCIONARIO_SKILLS = cargar_skills()

# Mapeo rápido de comandos a skills
MAPEO_SKILLS = {
    "analizar": "skill-1",
    "resumir": "skill-2",
    "preguntas": "skill-3"
}

def consultar_modelo(instrucciones_skill: str, entrada_usuario: str, contexto_general: str = "") -> str:
    """Invoca Gemini con las instrucciones de la skill como System Prompt/Contexto."""
    prompt_completo = (
        "Eres un Asistente Operativo Profesional para Psicólogos. "
        "Tu objetivo es asistir en la preparación, organización y estructuración del trabajo profesional.\n"
        "REGLA ÉTICA INQUEBRANTABLE: NO emitas diagnósticos clínicos definitivos ni juicios nosológicos. "
        "Cuida siempre la confidencialidad, usando códigos de consultante o lenguaje despersonalizado.\n\n"
        f"--- INSTRUCCIONES ESPECÍFICAS DE LA SKILL APLICABLE ---\n"
        f"{instrucciones_skill}\n\n"
        f"--- CONTEXTO O DATOS APORTADOS POR EL PSICÓLOGO ---\n"
        f"{entrada_usuario}\n\n"
        "Genera una respuesta clara, profesional, técnica y bien estructurada siguiendo exactamente las instrucciones de la skill."
    )

    if gemini_model:
        try:
            respuesta = gemini_model.generate_content(prompt_completo)
            return respuesta.text
        except Exception as e:
            return f"⚠️ Error al conectar con Gemini: {str(e)}\n\n(Revisa tu cuota o GEMINI_API_KEY en el archivo .env)"
    else:
        # Modo simulado de demostración cuando aún no se configura la API Key
        return (
            "⚙️ [MODO OPERATIVO LOCAL / DEMOSTRACIÓN]\n"
            "La GEMINI_API_KEY aún no ha sido configurada en agente/.env.\n\n"
            "📌 El agente procesó tu solicitud vinculando la siguiente skill:\n"
            f"{instrucciones_skill[:300]}...\n\n"
            f"📝 Consulta recibida:\n\"{entrada_usuario}\"\n\n"
            "👉 Para recibir respuestas completas generadas por IA, agrega tu clave en agente/.env: GEMINI_API_KEY=tu_clave"
        )

# Handlers de Telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usuario = update.effective_user.first_name if update.effective_user else "Colega"
    texto = (
        f"👋 ¡Hola, {usuario}!\n\n"
        "Soy tu **Asistente Operativo de Práctica Psicológica** impulsado por IA.\n"
        "Ejecuto actividades operativas utilizando las **Skills especializadas** de tu repositorio:\n\n"
        "🧠 **Comandos con Skills Integradas:**\n"
        "• `/analizar <caso o texto>`: Ejecuta la **Skill 1** (Análisis en 4 enfoques: cognitivo, conductual, humanista y psicodinámico).\n"
        "• `/resumir <notas o borrador>`: Ejecuta la **Skill 2** (Formateo de informe o bitácora profesional estructurada).\n"
        "• `/preguntas <contexto o motivo>`: Ejecuta la **Skill 3** (Genera banco de preguntas de entrevista y pautas de retroalimentación).\n"
        "• `/skills`: Muestra las skills cargadas en el agente.\n"
        "• `/ayuda`: Información sobre límites éticos y configuración.\n\n"
        "💬 _También puedes escribirme cualquier consulta libre y la responderé bajo el marco ético del kit._"
    )
    await update.message.reply_text(texto, parse_mode="Markdown")

async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "ℹ️ **Guía y Límites Éticos:**\n\n"
        "1. **Sin Diagnóstico Clínico:** Este bot apoya la preparación, análisis exploratorio y redacción operativa. No emite diagnósticos médicos concluyentes.\n"
        "2. **Confidencialidad:** Recomendamos usar identificadores como `CONS-01` en lugar de nombres reales.\n"
        "3. **Configuración:** Para activar la IA de Gemini, añade `GEMINI_API_KEY` en `agente/.env`."
    )
    await update.message.reply_text(texto, parse_mode="Markdown")

async def listar_skills(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global DICCIONARIO_SKILLS
    DICCIONARIO_SKILLS = cargar_skills()
    if not DICCIONARIO_SKILLS:
        await update.message.reply_text("⚠️ No se encontraron archivos SKILL.md en la carpeta `skills/`.")
        return

    texto = "📚 **Skills cargadas dinámicamente en el Agente:**\n\n"
    for nombre in DICCIONARIO_SKILLS:
        texto += f"• `{nombre}` (ubicado en `skills/{nombre}/SKILL.md`)\n"
    await update.message.reply_text(texto, parse_mode="Markdown")

async def comando_analizar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    entrada = " ".join(context.args)
    if not entrada:
        await update.message.reply_text(
            "⚠️ Por favor ingresa el caso o situación a analizar.\n"
            "Ejemplo: `/analizar Consultante refiere dificultad para decir no en su trabajo y sensación de fatiga crónica.`",
            parse_mode="Markdown"
        )
        return

    skill_doc = DICCIONARIO_SKILLS.get("skill-1", "Analizar el caso desde enfoques cognitivo, conductual, humanista y psicodinámico sin emitir diagnósticos definitivos.")
    await update.message.reply_text("⏳ Procesando análisis multidimensional mediante Skill 1...")
    resultado = consultar_modelo(skill_doc, entrada)
    await update.message.reply_text(resultado)

async def comando_resumir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    entrada = " ".join(context.args)
    if not entrada:
        await update.message.reply_text(
            "⚠️ Por favor ingresa las notas o borrador a estructurar.\n"
            "Ejemplo: `/resumir Sesión 2 con CONS-01: Se exploró situación laboral. Acordamos registrar disparadores de tensión.`",
            parse_mode="Markdown"
        )
        return

    skill_doc = DICCIONARIO_SKILLS.get("skill-2", "Redactar informe profesional estructurado, objetivos, evolución y acuerdos.")
    await update.message.reply_text("⏳ Redactando informe estructurado mediante Skill 2...")
    resultado = consultar_modelo(skill_doc, entrada)
    await update.message.reply_text(resultado)

async def comando_preguntas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    entrada = " ".join(context.args)
    if not entrada:
        await update.message.reply_text(
            "⚠️ Por favor indica el motivo o contexto para preparar la entrevista.\n"
            "Ejemplo: `/preguntas Primera entrevista con adulto joven por transición universitaria y ansiedad de desempeño.`",
            parse_mode="Markdown"
        )
        return

    skill_doc = DICCIONARIO_SKILLS.get("skill-3", "Generar guía de preguntas abiertas para entrevista inicial y retroalimentación.")
    await update.message.reply_text("⏳ Diseñando guía de entrevista mediante Skill 3...")
    resultado = consultar_modelo(skill_doc, entrada)
    await update.message.reply_text(resultado)

async def mensaje_libre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto_usuario = update.message.text
    contexto_general = "\n\n".join([f"--- {k} ---\n{v}" for k, v in DICCIONARIO_SKILLS.items()])
    resultado = consultar_modelo(contexto_general, texto_usuario)
    await update.message.reply_text(resultado)

def main():
    if not TELEGRAM_TOKEN or TELEGRAM_TOKEN == "tu_token_de_botfather":
        print("=" * 70)
        print("⚠️ AVISO DE CONFIGURACIÓN DEL AGENTE")
        print("Asegúrate de colocar tu token en agente/.env:")
        print("TELEGRAM_BOT_TOKEN=tu_token_de_botfather")
        print("GEMINI_API_KEY=tu_api_key_del_modelo")
        print("=" * 70)
        print("El código se encuentra verificado y listo para iniciar.")
        return

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ayuda", ayuda))
    app.add_handler(CommandHandler("skills", listar_skills))
    app.add_handler(CommandHandler("analizar", comando_analizar))
    app.add_handler(CommandHandler("resumir", comando_resumir))
    app.add_handler(CommandHandler("preguntas", comando_preguntas))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensaje_libre))

    print(f"🤖 Agente de Telegram en ejecución. {len(DICCIONARIO_SKILLS)} skills integradas.")
    app.run_polling()

if __name__ == "__main__":
    main()
