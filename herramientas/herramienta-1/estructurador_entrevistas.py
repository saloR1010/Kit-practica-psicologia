"""
Herramienta 1: Estructurador de guías de preguntas abiertas para entrevistas iniciales o sesiones exploratorias.
Enfocado en preparación operativa y respetando los límites éticos (sin emitir diagnósticos automatizados).
"""

import json
from datetime import datetime
from pathlib import Path

BANCO_PREGUNTAS = {
    "motivo_consulta": {
        "titulo": "Exploración del Motivo de Consulta y Expectativas",
        "preguntas": [
            "¿Qué situación o momento en particular te motivó a solicitar este espacio en este momento?",
            "Si describieras lo que estás viviendo con tus propias palabras, ¿cómo lo resumirías?",
            "¿Qué cambios o avances te gustaría notar al concluir este proceso?",
            "¿Has tenido experiencias previas en acompañamiento psicológico? ¿Qué resultó útil o qué preferirías que sea diferente?"
        ]
    },
    "impacto_cotidiano": {
        "titulo": "Impacto en Áreas Vitales y Rutina Cotidiana",
        "preguntas": [
            "¿De qué manera esta situación está influyendo en tu día a día (trabajo, estudio, descanso)?",
            "¿Cómo sientes que ha afectado tu relación con las personas cercanas o familiares?",
            "¿Qué actividades que antes disfrutabas o formaban parte de tu rutina se han visto modificadas?",
            "En las últimas semanas, ¿cómo ha estado tu calidad de sueño y tus niveles de energía habituales?"
        ]
    },
    "recursos_afrontamiento": {
        "titulo": "Recursos Propios, Fortalezas y Redes de Apoyo",
        "preguntas": [
            "Cuando la situación se torna más compleja, ¿qué estrategias o actividades te ayudan a recuperar la calma?",
            "¿Quiénes son las personas con las que sientes confianza para hablar cuando lo necesitas?",
            "Pensando en desafíos que superaste en el pasado, ¿qué fortalezas personales te permitieron salir adelante?",
            "¿Qué pasatiempos, espacios de desconexión o actividades de autocuidado sueles practicar?"
        ]
    },
    "contexto_historico": {
        "titulo": "Contextualización General y Línea Temporal",
        "preguntas": [
            "¿Desde cuándo identificas que esta situación empezó a tomar mayor relevancia?",
            "¿Hubo algún acontecimiento, cambio o transición importante alrededor de esa época?",
            "¿Existen momentos o temporadas en las que notas que la intensidad disminuye?",
            "¿Hay algún aspecto de tu entorno familiar o laboral actual que consideres relevante mencionar?"
        ]
    }
}

def generar_guia_entrevista(nombre_profesional: str, codigo_consultante: str, bloques_seleccionados: list = None, notas_adicionales: str = "") -> dict:
    """
    Genera una estructura de entrevista exploratoria organizada sin almacenar datos personales sensibles.
    """
    if bloques_seleccionados is None:
        bloques_seleccionados = list(BANCO_PREGUNTAS.keys())

    guia = {
        "meta": {
            "herramienta": "Estructurador de Guías de Preguntas Abiertas",
            "profesional": nombre_profesional,
            "codigo_consultante": codigo_consultante,
            "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "aviso_etico": "Herramienta de preparación operativa. No genera diagnósticos clínicos ni almacena datos sensibles no anonimizados."
        },
        "secciones": [],
        "notas_preparacion": notas_adicionales
    }

    for bloque in bloques_seleccionados:
        if bloque in BANCO_PREGUNTAS:
            info = BANCO_PREGUNTAS[bloque]
            guia["secciones"].append({
                "categoria": bloque,
                "titulo": info["titulo"],
                "preguntas": info["preguntas"]
            })

    return guia

def formatear_guia_texto(guia: dict) -> str:
    """Convierte la estructura en un formato legible para imprimir o llevar a consulta."""
    lineas = []
    lineas.append("=" * 70)
    lineas.append(f"GUÍA EXPLORATORIA DE ENTREVISTA INICIAL - {guia['meta']['fecha_creacion']}")
    lineas.append(f"Profesional a cargo: {guia['meta']['profesional']}")
    lineas.append(f"Código identificador de sesión: {guia['meta']['codigo_consultante']}")
    lineas.append("=" * 70)
    lineas.append(f"\n[AVISO ÉTICO]: {guia['meta']['aviso_etico']}\n")

    for i, sec in enumerate(guia["secciones"], 1):
        lineas.append(f"\n--- BLOQUE {i}: {sec['titulo']} ---")
        for j, preg in enumerate(sec["preguntas"], 1):
            lineas.append(f"  {j}. {preg}")
            lineas.append("     [ ] Observaciones / Anotaciones: ___________________________________")

    if guia["notas_preparacion"]:
        lineas.append(f"\nNotas u objetivos preparatorios del profesional:\n{guia['notas_preparacion']}")

    lineas.append("\n" + "=" * 70)
    return "\n".join(lineas)

def exportar_guia(guia: dict, ruta_salida: str, formato: str = "txt"):
    """Exporta la guía generada a archivo de texto o JSON."""
    p = Path(ruta_salida)
    if formato == "json":
        p.write_text(json.dumps(guia, indent=2, ensure_ascii=False), encoding="utf-8")
    else:
        p.write_text(formatear_guia_texto(guia), encoding="utf-8")
    print(f"Guía exportada exitosamente a: {p.resolve()}")

if __name__ == "__main__":
    print("--- Demostración de Herramienta 1 ---")
    guia_demo = generar_guia_entrevista(
        nombre_profesional="Lic. Laura Restrepo",
        codigo_consultante="CONS-2026-A1",
        bloques_seleccionados=["motivo_consulta", "impacto_cotidiano", "recursos_afrontamiento"],
        notas_adicionales="Validar estilo de comunicación y preferencia de horarios antes de cerrar la sesión."
    )
    salida_texto = formatear_guia_texto(guia_demo)
    print(salida_texto)

    # Exportar archivo de prueba
    ruta_demo = Path(__file__).parent / "ejemplo_guia_salida.txt"
    exportar_guia(guia_demo, str(ruta_demo), "txt")
