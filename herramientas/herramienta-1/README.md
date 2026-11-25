# Herramienta 1: Estructurador de Guías de Preguntas Abiertas

## Objetivo Operativo
Facilitar al psicólogo la preparación sistemática de entrevistas iniciales o sesiones exploratorias, organizando preguntas abiertas adaptables al motivo general de consulta, cuidando la confidencialidad (mediante códigos identificadores anónimos) y respetando los límites éticos sin formular ningún tipo de diagnóstico automatizado.

## Archivos
- `estructurador_entrevistas.py`: Módulo principal que contiene el banco modular de preguntas abiertas organizadas por áreas de indagación y funciones de exportación.
- `ejemplo_guia_salida.txt`: Muestra generada en texto plano lista para consulta o impresión.

## Bloques Temáticos Incluidos
1. **Motivo de Consulta y Expectativas**: Indagación respetuosa sobre qué trajo al consultante y qué cambios espera vivenciar.
2. **Impacto en Áreas Vitales**: Preguntas abiertas acerca de rutina, relaciones interpersonales, energía y descanso.
3. **Recursos Propios y Redes de Apoyo**: Exploración de fortalezas previas, apoyos comunitarios/familiares y autocuidado.
4. **Contextualización Histórica**: Línea temporal y transiciones relevantes en el entorno.

## Instrucciones Breves de Uso

1. Ejecuta el archivo directamente para generar una guía de ejemplo:
   ```bash
   python estructurador_entrevistas.py
   ```
2. Para usarlo dentro de tus propios scripts o integraciones:
   ```python
   from estructurador_entrevistas import generar_guia_entrevista, exportar_guia

   guia = generar_guia_entrevista(
       nombre_profesional="Tu Nombre",
       codigo_consultante="ID-CONS-01",
       bloques_seleccionados=["motivo_consulta", "recursos_afrontamiento"],
       notas_adicionales="Enfoque en validación emocional."
   )
   exportar_guia(guia, "guia_sesion.txt")
   ```
