"""
Herramienta 2: Generador de plantillas de psicoeducación y tareas entre sesiones.
Diseñado para facilitar la entrega de material claro, respetuoso y estructurado al consultante.
"""

from datetime import datetime
from pathlib import Path

PLANTILLAS_BASE = {
    "circulo_vicioso_ansiedad": {
        "tema": "Comprensión del Ciclo de Activación y Evitación",
        "objetivo": "Identificar cómo los pensamientos de alarma, sensaciones físicas y la evitación se retroalimentan.",
        "contenido_psicoeducativo": (
            "Cuando percibimos una situación como amenazante, nuestro cuerpo activa mecanismos de defensa naturales:\n"
            "1. Pensamiento de alarma ('No seré capaz', 'Algo malo pasará').\n"
            "2. Respuesta corporal (aceleración cardíaca, tensión muscular, respiración rápida).\n"
            "3. Impulso a evitar o huir de la situación.\n\n"
            "Aunque evitar produce alivio a corto plazo, a mediano plazo refuerza la creencia de que la situación es inmanejable.\n"
            "Aprender a observar estas sensaciones con calma permite desarmar el circuito de alarma progresivamente."
        ),
        "tarea_entre_sesiones": {
            "nombre_tarea": "Registro de Momentos de Malestar y Respuesta",
            "instrucciones": (
                "Durante los próximos días, cuando notes que la tensión aumenta, registra brevemente:\n"
                "a) ¿Qué estaba sucediendo justo antes?\n"
                "b) ¿Qué sensaciones físicas notaste en el cuerpo?\n"
                "c) ¿Qué hiciste en respuesta (respirar, distraerte, retirarte)?"
            ),
            "columnas_tabla": ["Día y Hora", "Situación / Detonante", "Sensación Corporal", "Pensamiento Presente", "¿Qué hice? (Acción)"]
        }
    },
    "pausa_respiracion": {
        "tema": "Entrenamiento en Pausa Consciente y Respiración Diafragmática",
        "objetivo": "Incorporar pausas intencionales breves en la rutina diaria para facilitar la autorregulación fisiológica.",
        "contenido_psicoeducativo": (
            "La respiración diafragmática envía señales de seguridad al sistema nervioso autónomo (activación parasimpática):\n"
            "1. Coloca una mano sobre el pecho y otra sobre el abdomen.\n"
            "2. Inhala lentamente por la nariz (3-4 segundos), sintiendo cómo se expande la zona del abdomen.\n"
            "3. Exhala suavemente por la boca (4-6 segundos) como si soplaras una vela sin apagarla.\n"
            "4. Repite este ciclo de 3 a 5 veces consecutivas."
        ),
        "tarea_entre_sesiones": {
            "nombre_tarea": "Práctica Diaria de Micro-Pausas de Calma",
            "instrucciones": (
                "Elige 2 momentos fijos del día (por ejemplo: antes de almorzar y al regresar a casa) "
                "para realizar 3 minutos de respiración diafragmática. Anota tus observaciones."
            ),
            "columnas_tabla": ["Fecha", "Momento del Día", "Nivel de Tensión Inicial (1-10)", "Nivel de Tensión Final (1-10)", "Sensación Post-ejercicio"]
        }
    },
    "registro_gratitud_logros": {
        "tema": "Ampliación del Foco Atencional: Registro de Agradecimientos y Logros Diarios",
        "objetivo": "Fomentar el reconocimiento de eventos positivos cotidianos y avances personales.",
        "contenido_psicoeducativo": (
            "Nuestra mente tiende naturalmente a fijarse en los errores, peligros o tareas pendientes (sesgo de negatividad).\n"
            "Dedicar unos minutos al final del día a notar intencionalmente aspectos amables o logros propios "
            "ayuda a construir una perspectiva más equilibrada y compasiva de nuestra realidad cotidiana."
        ),
        "tarea_entre_sesiones": {
            "nombre_tarea": "Bitácora Nocturna de Tres Agradecimientos o Logros",
            "instrucciones": (
                "Cada noche antes de dormir, anota tres detalles sencillos que salieron bien hoy o por los cuales sientas gratitud."
            ),
            "columnas_tabla": ["Fecha", "Agradecimiento / Logro 1", "Agradecimiento / Logro 2", "Agradecimiento / Logro 3", "Reflexión Breve"]
        }
    }
}

def generar_plantilla_psicoeducativa(tipo_plantilla: str, codigo_consultante: str, indicaciones_personalizadas: str = "") -> str:
    """
    Genera un documento claro, visual y estructurado para entregar al consultante.
    """
    plantilla = PLANTILLAS_BASE.get(tipo_plantilla)
    if not plantilla:
        raise ValueError(f"Plantilla no reconocida. Disponibles: {list(PLANTILLAS_BASE.keys())}")

    fecha_hoy = datetime.now().strftime("%d/%m/%Y")
    tarea = plantilla["tarea_entre_sesiones"]

    lineas = []
    lineas.append("=" * 72)
    lineas.append(f"MATERIAL DE APOYO Y TAREA INTER-SESIÓN")
    lineas.append(f"Código Consultante: {codigo_consultante} | Fecha de Entrega: {fecha_hoy}")
    lineas.append("=" * 72)
    lineas.append(f"\n📌 TEMA: {plantilla['tema']}")
    lineas.append(f"🎯 OBJETIVO: {plantilla['objetivo']}\n")
    lineas.append("-" * 72)
    lineas.append("📖 INFORMACIÓN CLAVE:")
    lineas.append(plantilla["contenido_psicoeducativo"])
    lineas.append("-" * 72)
    lineas.append(f"\n📝 TAREA ENTRE SESIONES: {tarea['nombre_tarea']}")
    lineas.append(f"Instrucciones:\n{tarea['instrucciones']}\n")
    lineas.append("FORMATO DE REGISTRO SUGERIDO:")
    lineas.append(" | ".join(tarea["columnas_tabla"]))
    lineas.append("-" * 72)

    for i in range(1, 4):
        lineas.append(f"[{i}] " + " | ".join(["____________________" for _ in tarea["columnas_tabla"]]))

    if indicaciones_personalizadas:
        lineas.append(f"\n💡 Indicación Específica del Profesional:\n{indicaciones_personalizadas}")

    lineas.append("\n" + "=" * 72)
    lineas.append("Nota: Este material es de apoyo práctico y colaborativo entre consultante y terapeuta.")
    return "\n".join(lineas)

def guardar_plantilla(contenido: str, ruta_destino: str):
    p = Path(ruta_destino)
    p.write_text(contenido, encoding="utf-8")
    print(f"Plantilla guardada en: {p.resolve()}")

if __name__ == "__main__":
    print("--- Demostración de Herramienta 2 ---")
    doc_ansiedad = generar_plantilla_psicoeducativa(
        tipo_plantilla="circulo_vicioso_ansiedad",
        codigo_consultante="CONS-2026-09",
        indicaciones_personalizadas="Enfocarse únicamente en notar la respiración sin intentar cambiarla a la fuerza."
    )
    print(doc_ansiedad)

    ruta_salida = Path(__file__).parent / "ejemplo_tarea_psicoeducativa.txt"
    guardar_plantilla(doc_ansiedad, str(ruta_salida))
